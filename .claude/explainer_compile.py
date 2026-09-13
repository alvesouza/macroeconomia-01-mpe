#!/usr/bin/env python3
"""Compile an /explainer video project into ONE file, frame-accurately.

Takes a project directory holding beats.json (written by speechify_tts.py) and the rendered
Manim scenes, and produces <slug>.mp4 with the narration muxed in, plus a drift report.

Why this is a script and not a shell one-liner — three failure modes, all measured on this
machine on 2026-09-12:

  1. Manim quantises every animation to whole frames, and it rounds PER self.play() call.
     A beat whose fractions sum to 1.0 can therefore render SHORTER than its narration:
     BeatTwo asked for 16.656 s and rendered 16.600 s. Padding the audio to the video length
     would have cut 56 ms of speech off mid-word. So each beat's slot is
     max(video, audio) — the audio is padded with silence AND the video is extended by
     freezing its last frame, whichever is short.
  2. Concatenating AAC clips accumulates per-clip padding (10.1 ms over two clips), which
     desyncs a long video. Audio is therefore concatenated as lossless PCM and encoded to
     AAC exactly once, at the mux.
  3. ffmpeg on Windows cannot open the POSIX paths Git Bash's $PWD produces
     (/tmp/claude/... -> "No such file or directory"). Concat list entries are resolved
     relative to the list file, so this writes RELATIVE paths and sidesteps the issue.

Usage:
  python .claude/explainer_compile.py Videos/<slug>
  python .claude/explainer_compile.py Videos/<slug> --quality 1080p60 --name my-video
  python .claude/explainer_compile.py Videos/<slug> --no-audio      # silent + subtitles

Exit codes: 0 ok | 1 usage or missing input | 2 ffmpeg failure | 3 drift over tolerance
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

FFMPEG = shutil.which("ffmpeg")
FFPROBE = shutil.which("ffprobe")


def run(cmd: list[str]) -> None:
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"[2] ffmpeg failed:\n  {' '.join(cmd[:6])} ...\n{out.stderr.strip()[:800]}")


def duration(path: Path) -> float:
    out = subprocess.run(
        [FFPROBE, "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    if out.returncode != 0 or not out.stdout.strip():
        sys.exit(f"[1] cannot probe {path}: {out.stderr.strip()[:200]}")
    return float(out.stdout.strip())


def find_render_dir(project: Path, quality: str | None) -> Path:
    """Locate media/videos/<module>/<quality>/ — Manim nests by source module and resolution."""
    base = project / "media" / "videos"
    if not base.exists():
        sys.exit(f"[1] no render tree at {base}. Render the scenes first:\n"
                 f"    cd \"{project}\" && python -m manim render -ql --media_dir media scenes.py BeatOne")
    candidates = [d for d in base.glob("*/*") if d.is_dir() and any(d.glob("*.mp4"))]
    if quality:
        candidates = [d for d in candidates if d.name == quality] or candidates
    if not candidates:
        sys.exit(f"[1] no rendered .mp4 found under {base}")
    # Highest resolution wins when several exist (1080p60 beats 480p15).
    def rank(d: Path) -> tuple:
        digits = "".join(c if c.isdigit() else " " for c in d.name).split()
        return tuple(int(x) for x in digits) if digits else (0,)
    return sorted(candidates, key=rank)[-1]


def main() -> int:
    if not FFMPEG or not FFPROBE:
        sys.exit("[1] ffmpeg and ffprobe must be on PATH.")

    ap = argparse.ArgumentParser(description="Compile an /explainer project into one video.")
    ap.add_argument("project", help="the Videos/<slug> directory")
    ap.add_argument("--quality", help="render dir to use, e.g. 480p15 or 1080p60")
    ap.add_argument("--name", help="output basename (default: the project directory name)")
    ap.add_argument("--no-audio", action="store_true", help="video only, no narration track")
    ap.add_argument("--tolerance-ms", type=float, default=40.0,
                    help="fail if audio/video drift exceeds this (default 40 ms, ~1 frame at 25fps)")
    args = ap.parse_args()

    project = Path(args.project).resolve()
    if not project.is_dir():
        sys.exit(f"[1] not a directory: {project}")
    manifest_path = project / "beats.json"
    if not manifest_path.exists():
        sys.exit(f"[1] no beats.json in {project} — run speechify_tts.py --script first.")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    beats = manifest.get("beats") or []
    if not beats:
        sys.exit("[1] beats.json has no beats.")

    render_dir = find_render_dir(project, args.quality)
    work = project / "build"
    work.mkdir(exist_ok=True)
    use_audio = not args.no_audio and bool(manifest.get("voice"))

    print(f"project  {project.name}")
    print(f"renders  {render_dir.relative_to(project)}")
    print(f"audio    {'narration from beats.json' if use_audio else 'none (silent)'}\n")

    rows, video_parts, audio_parts = [], [], []

    for beat in beats:
        bid = beat["id"]
        video = render_dir / f"{bid}.mp4"
        if not video.exists():
            sys.exit(f"[1] beat {bid} is not rendered: {video}\n"
                     f"    Never compile a partial video — render it, then re-run.")
        v_len = duration(video)

        a_len, audio = 0.0, None
        if use_audio:
            audio = project / beat.get("audio", f"audio/{bid}.mp3")
            if not audio.exists():
                sys.exit(f"[1] beat {bid} has no audio at {audio}")
            a_len = duration(audio)

        slot = max(v_len, a_len)          # never truncate either stream

        # Video: freeze the last frame if the narration outlasts the animation.
        v_out = video
        if slot - v_len > 0.001:
            v_out = work / f"{bid}_ext.mp4"
            run([FFMPEG, "-v", "error", "-i", str(video),
                 "-vf", f"tpad=stop_mode=clone:stop_duration={slot - v_len:.6f}",
                 "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p",
                 "-an", str(v_out), "-y"])
        video_parts.append(v_out)

        # Audio: pad with silence to the slot, lossless so concatenation is sample-exact.
        if use_audio:
            a_out = work / f"{bid}_pad.wav"
            run([FFMPEG, "-v", "error", "-i", str(audio), "-af", "apad",
                 "-t", f"{slot:.6f}", "-c:a", "pcm_s16le", "-ar", "48000", "-ac", "2",
                 str(a_out), "-y"])
            audio_parts.append(a_out)

        rows.append((bid, a_len, v_len, slot, slot - v_len))
        print(f"  {bid:<16} narration {a_len:>8.3f}  render {v_len:>8.3f}  "
              f"slot {slot:>8.3f}  {'+video frozen' if slot - v_len > 0.001 else ''}")

    def concat(parts: list[Path], out: Path, listing: Path) -> None:
        # Relative paths: ffmpeg resolves concat entries against the list file's directory,
        # which avoids Git Bash's POSIX $PWD being handed to a native Windows binary.
        lines = []
        for p in parts:
            try:
                rel = p.relative_to(listing.parent)
            except ValueError:
                rel = Path("..") / p.relative_to(listing.parent.parent)
            lines.append(f"file '{rel.as_posix()}'\n")
        listing.write_text("".join(lines), encoding="utf-8")
        run([FFMPEG, "-v", "error", "-f", "concat", "-safe", "0",
             "-i", str(listing), "-c", "copy", str(out), "-y"])

    video_cat = work / "video.mp4"
    concat(video_parts, video_cat, work / "concat_video.txt")
    v_total = duration(video_cat)

    out_name = (args.name or project.name) + ".mp4"
    final = project / out_name

    if use_audio:
        track = work / "track.wav"
        concat(audio_parts, track, work / "concat_audio.txt")
        a_total = duration(track)
        run([FFMPEG, "-v", "error", "-i", str(video_cat), "-i", str(track),
             "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
             "-c:a", "aac", "-b:a", "192k", str(final), "-y"])
    else:
        a_total = 0.0
        shutil.copy2(video_cat, final)

    f_total = duration(final)
    drift_ms = abs(v_total - a_total) * 1000 if use_audio else 0.0

    print(f"\n  {'beat':<16} {'narration':>10} {'render':>10} {'slot':>10}")
    for bid, a, v, s, _ in rows:
        print(f"  {bid:<16} {a:>10.3f} {v:>10.3f} {s:>10.3f}")
    print(f"  {'TOTAL':<16} {a_total:>10.3f} {v_total:>10.3f} {f_total:>10.3f}")
    print(f"\n  drift  {drift_ms:.1f} ms (tolerance {args.tolerance_ms:.0f} ms)")

    probe = subprocess.run(
        [FFPROBE, "-v", "error", "-show_entries",
         "stream=codec_type,codec_name,width,height", "-of", "csv=p=0", str(final)],
        capture_output=True, text=True).stdout.strip().replace("\n", " | ")
    print(f"  streams {probe}")
    print(f"  output  {final}  ({final.stat().st_size / 1_048_576:.2f} MB, {f_total:.3f}s)")

    if drift_ms > args.tolerance_ms:
        print("\n[3] drift over tolerance — a beat's audio and animation disagree.")
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
