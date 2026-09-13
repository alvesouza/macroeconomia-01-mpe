# Speechify API — verified facts

Established by probing the live API on 2026-09-12 with the project's own key. Not from
documentation. Client: `.claude/speechify_tts.py`.

## Auth and hosts

- Base URL **`https://api.speechify.ai`**. `https://api.sws.speechify.com` is a live legacy
  alias for the same backend (byte-identical responses); prefer the former.
- `Authorization: Bearer $SPEECHIFY_API_KEY`, plus `Content-Type: application/json` on POSTs.
  No version header, no workspace id.
- The key is genuinely Speechify's, confirmed from the API's own responses — a bogus `sk_…`
  key returns 401 on the same endpoint, so the 200 is attributable to the key.
- Every error body carries a `request_id`. Log it; support asks for it.

## Endpoints

| Endpoint | Verified | Notes |
|---|---|---|
| `POST /v1/audio/speech` | 200 | **The one to use.** JSON in, JSON out |
| `GET /v1/voices` | 200 | Cursor-paginated. 992 voices on this account, 125 English |
| `GET /v1/audio/models` | 200 | `simba-3.0` (default, multilingual incl. pt-BR), `simba-3.2` (recommended, English only) |
| `POST /v1/audio/stream` | 200 | Raw binary, **no speech marks** |
| `POST /v1/audio/stream/with-timestamps` | 200 | SSE, audio + marks, 20 000 char cap (cap itself UNVERIFIED) |
| `GET /v1/models`, `/v1/tts/models` | **404** | The correct path is `/v1/audio/models` |
| `GET /v1/api-keys/scopes` | **401** | No introspection endpoint exists — plan and quota cannot be read |

## The traps

1. **Audio is base64 inside JSON**, not binary: `base64.b64decode(body["audio_data"])`.
2. **Hard cap of 2 000 characters** on `input`. 2 001 returns HTTP 400 `validation_failed`.
   The client chunks on sentence boundaries and joins with ffmpeg concat.
3. **`speech_marks` are word-level, in milliseconds**, with character offsets into the input —
   but they **under-report length** (1 750 ms of marks against an 1 800 ms file). Clip duration
   must always come from `ffprobe`, never from the marks.
4. Empty `input` is a 400, so a blank beat breaks a run.
5. `output_format: "mp3_24000_192"` is **silently downgraded** to 160 kbps — the response
   echoes the lower value. Do not assume the bitrate you asked for.
6. Rate limits on this account: `ratelimit-limit: 20` (documented Starter tier: 20 req/s,
   15 concurrent).

## Billing

The response field is literally **`billable_characters_count`** — Speechify counts characters,
and the developer API is metered separately from the consumer reading app. There is no way to
read the balance (see the 401 above), so **report characters, never money**.

Spent on this key so far: ~6 500 (research probes) + 15 (`--check`) + 448 (2-beat test)
+ 46 112 (the 20-beat Aula 7 narration) ≈ **53 000 characters**.

The client caches per beat against a SHA-256 of `(text, voice, model, format)`, so
**re-rendering costs nothing** and only an edited beat's text re-synthesises.

## Settings that matter

`options.loudness_normalization: true` normalises to −14 LUFS, which keeps levels equal across
separately synthesised beats — without it you get a volume step at every beat boundary.
Default voice `george` (en-US, warm, e-learning + audiobook tagged).
