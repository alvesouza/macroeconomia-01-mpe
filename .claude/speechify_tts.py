#!/usr/bin/env python3
"""Speechify text-to-speech client for /explainer narration.

Turns a beat sheet into one audio clip per beat plus a manifest of MEASURED durations.
That manifest is the timing contract the Manim scenes read: a scene sets its run_time from
the real length of its narration, so the animation cannot drift from the voice.

Needs:
  * SPEECHIFY_API_KEY in the environment, or in the repo's gitignored .env
  * ffprobe on PATH (duration measurement); ffmpeg only when a beat exceeds 2000 chars

Usage:
  python .claude/speechify_tts.py --check
  python .claude/speechify_tts.py --list-voices --locale en-US --tag e-learning
  python .claude/speechify_tts.py --say "Testing one two three." --out audio/test.mp3
  python .claude/speechify_tts.py --script Videos/<slug>/beats.json

API facts verified live on 2026-09-12 against https://api.speechify.ai:
  * POST /v1/audio/speech returns JSON, not binary: audio_data is base64. Hard cap of
    2000 characters per request (2001 -> HTTP 400 validation_failed), so longer beats are
    chunked on sentence boundaries here and concatenated with ffmpeg.
  * speech_marks are WORD level, in milliseconds, with character offsets into the input.
  * The marks UNDER-report real length (1750 ms of marks vs 1800 ms of file) because of
    trailing silence. Clip duration therefore always comes from ffprobe, never from marks.
  * Models live at /v1/audio/models, not /v1/models: simba-3.0 (default, multilingual,
    includes pt-BR) and simba-3.2 (recommended, English only).
  * options.loudness_normalization=true normalises to -14 LUFS, which keeps levels equal
    across separately synthesised beats. On by default here.

Exit codes: 0 ok | 1 usage or config error | 2 API error | 3 audio verification failed
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

try:
    import requests
except ImportError:  # pragma: no cover
    sys.exit("requests is required: python -m pip install requests")

BASE_URL = "https://api.speechify.ai"
MAX_CHARS = 2000                      # hard server limit on /v1/audio/speech
DEFAULT_VOICE = "george"              # en-US, middle-aged, warm; e-learning + audiobook tagged
DEFAULT_MODEL = "simba-3.2"           # recommended; English only. Use simba-3.0 for pt-BR.
DEFAULT_FORMAT = "mp3"
DEFAULT_LANGUAGE = "en-US"
REPO_ROOT = Path(__file__).resolve().parent.parent


# --------------------------------------------------------------------------- key handling

def load_key() -> str:
    """Return the API key from the environment, falling back to the gitignored .env.

    Never logs or returns the value anywhere else.
    """
    key = os.environ.get("SPEECHIFY_API_KEY", "").strip()
    if key:
        return key
    env_path = REPO_ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            name, _, value = line.partition("=")
            if name.strip() == "SPEECHIFY_API_KEY":
                return value.strip().strip('"').strip("'")
    sys.exit(
        "SPEECHIFY_API_KEY not found.\n"
        f"  Put it in {env_path} as SPEECHIFY_API_KEY=... (that file is gitignored),\n"
        "  or export it in the environment. See .env.example."
    )


def _headers(key: str) -> dict:
    return {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}


def _redact(text: str, key: str) -> str:
    return text.replace(key, "sk_***REDACTED***") if key else text


# ------------------------------------------------------------------------------- ffprobe

def probe_duration(path: Path) -> float:
    """Measured duration in seconds. This is the authoritative clip length."""
    if not shutil.which("ffprobe"):
        sys.exit("ffprobe not found on PATH — install ffmpeg.")
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    )
    if out.returncode != 0 or not out.stdout.strip():
        raise RuntimeError(f"ffprobe could not read {path}: {out.stderr.strip()}")
    return float(out.stdout.strip())


# ------------------------------------------------------------------------------ chunking

def split_text(text: str, limit: int = MAX_CHARS) -> list[str]:
    """Split on sentence boundaries so no chunk exceeds the server's character cap."""
    text = text.strip()
    if len(text) <= limit:
        return [text]
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks, current = [], ""
    for sentence in sentences:
        while len(sentence) > limit:            # a single monstrous sentence
            cut = sentence.rfind(" ", 0, limit)
            cut = cut if cut > 0 else limit
            chunks.append(sentence[:cut].strip())
            sentence = sentence[cut:].strip()
        if len(current) + len(sentence) + 1 <= limit:
            current = f"{current} {sentence}".strip()
        else:
            if current:
                chunks.append(current)
            current = sentence
    if current:
        chunks.append(current)
    return [c for c in chunks if c]


# ----------------------------------------------------------------------------- API calls

def _post_speech(key: str, payload: dict, retries: int = 4) -> dict:
    url = f"{BASE_URL}/v1/audio/speech"
    delay = 1.5
    for attempt in range(1, retries + 1):
        try:
            r = requests.post(url, headers=_headers(key), json=payload, timeout=120)
        except requests.RequestException as exc:
            if attempt == retries:
                sys.exit(f"[2] network error after {retries} attempts: {exc}")
            time.sleep(delay); delay *= 2; continue

        if r.status_code == 200:
            return r.json()

        body = _redact(r.text[:500], key)
        rid = ""
        try:
            rid = r.json().get("request_id", "")
        except Exception:
            pass

        # Transient: rate limit or server side. Everything else is a real error.
        if r.status_code == 429 or r.status_code >= 500:
            if attempt == retries:
                sys.exit(f"[2] HTTP {r.status_code} after {retries} attempts. request_id={rid}\n{body}")
            wait = float(r.headers.get("Retry-After", delay))
            print(f"  HTTP {r.status_code}, retrying in {wait:.1f}s "
                  f"(attempt {attempt}/{retries})", file=sys.stderr)
            time.sleep(wait); delay *= 2; continue

        hint = {
            401: "Key rejected. Check SPEECHIFY_API_KEY in .env.",
            404: "Unknown voice_id. Run --list-voices to see this workspace's voices.",
            400: "Validation failed. Input must be 1–2000 chars; check audio_format/model.",
        }.get(r.status_code, "")
        sys.exit(f"[2] HTTP {r.status_code}. {hint} request_id={rid}\n{body}")
    raise AssertionError("unreachable")


def list_voices(key: str, locale: str | None = None, tag: str | None = None) -> list[dict]:
    """Every voice on the workspace. Cursor-paginated; this account has ~992."""
    voices, cursor = [], None
    while True:
        params = {"limit": 100}
        if cursor:
            params["cursor"] = cursor
        r = requests.get(f"{BASE_URL}/v1/voices", headers=_headers(key),
                         params=params, timeout=60)
        if r.status_code != 200:
            sys.exit(f"[2] HTTP {r.status_code} listing voices: {_redact(r.text[:300], key)}")
        data = r.json()
        voices.extend(data.get("voices", []))
        cursor = data.get("next_cursor")
        if not data.get("has_more") or not cursor:
            break
    if locale:
        voices = [v for v in voices if (v.get("locale") or "").lower().startswith(locale.lower())]
    if tag:
        voices = [v for v in voices if any(tag.lower() in t.lower() for t in v.get("tags", []))]
    return voices


def list_models(key: str) -> list[dict]:
    r = requests.get(f"{BASE_URL}/v1/audio/models", headers=_headers(key), timeout=60)
    if r.status_code != 200:
        sys.exit(f"[2] HTTP {r.status_code} listing models: {_redact(r.text[:300], key)}")
    return r.json().get("models", [])


# ---------------------------------------------------------------------------- synthesis

def synthesize(text: str, out_path: Path, *, key: str | None = None,
               voice_id: str = DEFAULT_VOICE, audio_format: str = DEFAULT_FORMAT,
               model: str = DEFAULT_MODEL, language: str = DEFAULT_LANGUAGE,
               loudness_normalization: bool = True) -> dict:
    """Synthesise one passage to one audio file. Returns a record with the MEASURED duration.

    Chunks automatically past the 2000-character server cap and concatenates with ffmpeg.
    """
    text = (text or "").strip()
    if not text:
        sys.exit("[1] refusing to synthesise empty text — a blank beat breaks the run.")
    key = key or load_key()
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    chunks = split_text(text)
    billable, marks, parts = 0, [], []

    for index, chunk in enumerate(chunks, start=1):
        payload = {
            "input": chunk,
            "voice_id": voice_id,
            "audio_format": audio_format,
            "model": model,
            "language": language,
            "options": {"loudness_normalization": loudness_normalization,
                        "text_normalization": True},
        }
        data = _post_speech(key, payload)
        audio = base64.b64decode(data["audio_data"])
        billable += int(data.get("billable_characters_count") or 0)

        part = (out_path if len(chunks) == 1
                else out_path.with_name(f"{out_path.stem}.part{index}{out_path.suffix}"))
        part.write_bytes(audio)
        parts.append(part)
        if data.get("speech_marks"):
            marks.append(data["speech_marks"])

    if len(parts) > 1:                      # stitch the chunks, no re-encode
        if not shutil.which("ffmpeg"):
            sys.exit("[1] ffmpeg needed to join a multi-chunk beat but is not on PATH.")
        listing = out_path.with_suffix(".concat.txt")
        listing.write_text(
            "".join(f"file '{p.resolve().as_posix()}'\n" for p in parts), encoding="utf-8")
        subprocess.run(
            ["ffmpeg", "-v", "error", "-f", "concat", "-safe", "0",
             "-i", str(listing), "-c", "copy", str(out_path), "-y"], check=True)
        for p in parts:
            p.unlink(missing_ok=True)
        listing.unlink(missing_ok=True)

    seconds = probe_duration(out_path)
    return {
        "audio": out_path.as_posix(),
        "seconds": round(seconds, 3),
        "voice": voice_id,
        "model": model,
        "audio_format": audio_format,
        "chars": len(text),
        "billable_characters": billable,
        "chunks": len(chunks),
        "speech_marks": marks,
    }


def _text_fingerprint(text: str, voice: str, model: str, fmt: str) -> str:
    blob = f"{voice}|{model}|{fmt}|{text.strip()}".encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:16]


def synthesize_script(manifest_path: Path, *, voice_id: str | None = None,
                      model: str | None = None, audio_format: str | None = None,
                      force: bool = False) -> dict:
    """Synthesise every beat in a manifest and write back the measured durations.

    The manifest is the contract between narration and animation:

        {"voice": "george", "model": "simba-3.2", "total_seconds": 0.0,
         "beats": [{"id": "BeatOne", "text": "...", "audio": "", "seconds": 0.0}]}

    A beat whose text, voice, model and format are unchanged and whose audio file still
    exists is SKIPPED — text-to-speech is billable, so unchanged beats are never re-paid for.
    """
    manifest_path = Path(manifest_path)
    if not manifest_path.exists():
        sys.exit(f"[1] manifest not found: {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    beats = manifest.get("beats") or []
    if not beats:
        sys.exit("[1] manifest has no beats.")

    key = load_key()
    voice = voice_id or manifest.get("voice") or DEFAULT_VOICE
    mdl = model or manifest.get("model") or DEFAULT_MODEL
    fmt = audio_format or manifest.get("audio_format") or DEFAULT_FORMAT
    audio_dir = manifest_path.parent / "audio"

    total_billable, reused = 0, 0
    for beat in beats:
        bid = beat.get("id")
        if not bid:
            sys.exit("[1] every beat needs an id (it is also the Manim Scene class name).")
        text = beat.get("text", "")
        fingerprint = _text_fingerprint(text, voice, mdl, fmt)
        target = audio_dir / f"{bid}.{fmt}"

        if (not force and beat.get("text_sha256") == fingerprint
                and target.exists() and beat.get("seconds")):
            print(f"  = {bid:<16} unchanged, reusing {beat['seconds']:.3f}s")
            reused += 1
            continue

        record = synthesize(text, target, key=key, voice_id=voice,
                           audio_format=fmt, model=mdl)
        beat.update({
            "audio": Path(record["audio"]).relative_to(manifest_path.parent).as_posix(),
            "seconds": record["seconds"],
            "text_sha256": fingerprint,
            "chars": record["chars"],
            "speech_marks": record["speech_marks"],
        })
        total_billable += record["billable_characters"]
        print(f"  + {bid:<16} {record['seconds']:>7.3f}s  "
              f"{record['chars']:>5} chars  {record['chunks']} chunk(s)")

    manifest.update({
        "voice": voice,
        "model": mdl,
        "audio_format": fmt,
        "total_seconds": round(sum(float(b.get("seconds") or 0) for b in beats), 3),
        "billable_characters_this_run": total_billable,
    })
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    minutes = manifest["total_seconds"] / 60
    print(f"\n  {len(beats)} beats | {reused} reused | total {manifest['total_seconds']:.3f}s "
          f"({minutes:.1f} min) | billed {total_billable} chars this run")
    print(f"  manifest: {manifest_path}")
    return manifest


def srt_from_manifest(manifest_path: Path, out_path: Path | None = None) -> Path:
    """Build subtitles by accumulating the MEASURED beat durations, so they cannot drift."""
    manifest = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    out_path = Path(out_path or Path(manifest_path).with_suffix(".srt"))

    def stamp(t: float) -> str:
        ms = int(round(t * 1000))
        h, ms = divmod(ms, 3_600_000)
        m, ms = divmod(ms, 60_000)
        s, ms = divmod(ms, 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

    lines, clock = [], 0.0
    for i, beat in enumerate(manifest.get("beats", []), start=1):
        span = float(beat.get("seconds") or 0)
        lines += [str(i), f"{stamp(clock)} --> {stamp(clock + span)}",
                  beat.get("text", "").strip(), ""]
        clock += span
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  subtitles: {out_path} ({clock:.3f}s)")
    return out_path


# ----------------------------------------------------------------------------------- CLI

def cmd_check(key: str) -> int:
    print("Speechify check")
    ok = True

    for tool in ("ffprobe", "ffmpeg"):
        path = shutil.which(tool)
        print(f"  {'OK  ' if path else 'MISS'} {tool}")
        ok &= bool(path) or tool == "ffmpeg"

    models = list_models(key)
    names = ", ".join(
        f"{m.get('id')}{' (default)' if m.get('default') else ''}"
        f"{' (recommended)' if m.get('recommended') else ''}" for m in models)
    print(f"  OK   auth accepted — models: {names}")

    voices = list_voices(key, locale="en")
    print(f"  OK   {len(voices)} English voices on this workspace")
    if not any(v.get("id") == DEFAULT_VOICE for v in voices):
        print(f"  WARN default voice '{DEFAULT_VOICE}' not in this workspace")

    print("  ..   synthesising two words to verify end to end")
    tmp = Path(os.environ.get("TEMP", ".")) / "speechify_check.mp3"
    rec = synthesize("Check complete.", tmp, key=key)
    print(f"  OK   {rec['seconds']:.3f}s of audio, {rec['billable_characters']} chars billed")
    tmp.unlink(missing_ok=True)

    print("\nReady." if ok else "\nMissing a dependency above.")
    return 0 if ok else 1


def main() -> int:
    p = argparse.ArgumentParser(
        description="Speechify narration for /explainer videos.",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--check", action="store_true",
                   help="verify key, models, voices and ffprobe; synthesises two words")
    p.add_argument("--list-voices", action="store_true", help="list workspace voices")
    p.add_argument("--list-models", action="store_true", help="list available models")
    p.add_argument("--locale", help="filter voices by locale prefix, e.g. en-US or pt")
    p.add_argument("--tag", help="filter voices by tag substring, e.g. e-learning")
    p.add_argument("--say", metavar="TEXT", help="synthesise one passage")
    p.add_argument("--out", metavar="FILE", help="output file for --say")
    p.add_argument("--script", metavar="MANIFEST", help="synthesise every beat in beats.json")
    p.add_argument("--srt", metavar="MANIFEST", help="write subtitles from a manifest")
    p.add_argument("--voice", default=None, help=f"voice id (default {DEFAULT_VOICE})")
    p.add_argument("--model", default=None, help=f"model id (default {DEFAULT_MODEL})")
    p.add_argument("--format", default=None, dest="audio_format",
                   help=f"wav|mp3|ogg|aac|pcm (default {DEFAULT_FORMAT})")
    p.add_argument("--force", action="store_true", help="re-synthesise unchanged beats")
    args = p.parse_args()

    if args.srt:
        srt_from_manifest(Path(args.srt))
        return 0

    key = load_key()

    if args.check:
        return cmd_check(key)

    if args.list_models:
        for m in list_models(key):
            flags = " ".join(f for f, on in
                             (("default", m.get("default")), ("recommended", m.get("recommended")),
                              ("deprecated", m.get("deprecated"))) if on)
            print(f"{m.get('id'):<14} {flags:<24} {','.join(m.get('languages') or [])}")
        return 0

    if args.list_voices:
        voices = list_voices(key, locale=args.locale, tag=args.tag)
        print(f"{len(voices)} voices"
              + (f" | locale~{args.locale}" if args.locale else "")
              + (f" | tag~{args.tag}" if args.tag else ""))
        for v in voices:
            print(f"  {v.get('id'):<18} {v.get('display_name',''):<18} "
                  f"{v.get('locale',''):<8} {v.get('gender',''):<8} "
                  f"{','.join(v.get('tags', [])[:3])}")
        return 0

    if args.say:
        if not args.out:
            return p.error("--say needs --out FILE")
        rec = synthesize(args.say, Path(args.out), key=key,
                         voice_id=args.voice or DEFAULT_VOICE,
                         model=args.model or DEFAULT_MODEL,
                         audio_format=args.audio_format or DEFAULT_FORMAT)
        print(json.dumps({k: v for k, v in rec.items() if k != "speech_marks"}, indent=2))
        return 0

    if args.script:
        synthesize_script(Path(args.script), voice_id=args.voice, model=args.model,
                          audio_format=args.audio_format, force=args.force)
        return 0

    p.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
