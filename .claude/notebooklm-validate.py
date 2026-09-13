# -*- coding: utf-8 -*-
"""Linter dos prompts do NotebookLM. Aplica as regras de rules/10_notebooklm_prompts.md.

Uso: python .claude/notebooklm-validate.py [-v]
"""
import re
import sys
from pathlib import Path

CAP, LO, HI = 5000, 4200, 4950
VERBOSE = "-v" in sys.argv

SOFT = ["be honest", "give credit", "say it plainly", "spend real time", "go slowly",
        "linger", "push past", "dwell on", "willing to raise", "take seriously"]
BANNED_AUDIO = ["bellman", "dsge", "rbc", "calvo", "dynamic programming"]
SKIP_MARKERS = ["skip entirely", "skip:", "do not attempt", "do not cover", "leave out"]
HOST_MARKERS = ["disagree", "objection", "one host", "have the hosts", "let the other",
                "ask whether", "raise the"]
# R12 - cada batida de video nomeia o que aparece na tela
VISUAL_MARKERS = ["on screen", "on-screen", "show ", "shows ", "panel", "chart", "axis",
                  "axes", "draw", "frame", "diagram", "plot", "table", "timeline",
                  "curve", "bar ", "image", "highlight"]
# R16 - fechamento com a imagem unica
CLOSE_MARKERS = ["single image", "one image", "redraw", "from memory", "final frame",
                 "closing image"]

root = Path(__file__).resolve().parent.parent / "NotebookLM"
files = sorted(list((root / "slides").glob("*.md"))
               + list((root / "audio").glob("*.md"))
               + list((root / "video").glob("*.md")))
if not files:
    print("nenhum prompt encontrado")
    sys.exit(1)

SEG_RE = re.compile(r"^[A-Z][A-Z0-9 \-,'—]{4,}[.—]")
rows, total_fail = [], 0

for f in files:
    text = f.read_text(encoding="utf-8")
    low = text.lower()
    is_audio = f.parent.name == "audio"
    is_video = f.parent.name == "video"
    paras = [x.strip() for x in text.split("\n\n") if x.strip()]
    segs = [x for x in paras if SEG_RE.match(x)]
    n = len(text)
    fails = []

    # R10 - orcamento
    if n > CAP:
        fails.append(f"R10 chars {n} > {CAP}")
    elif n < LO:
        fails.append(f"R10 subutilizado ({n})")

    # R6 - nudges nao verificaveis
    soft = [s for s in SOFT if s in low]
    if soft:
        fails.append(f"R6 estilo: {', '.join(soft)}")

    if is_audio:
        # R2 - no maximo 5 segmentos
        if len(segs) > 5:
            fails.append(f"R2 {len(segs)} segmentos > 5")
        # R3 - no maximo 3 numerais que o ouvinte precise ACOMPANHAR por segmento.
        # Nao contam: o numero do proprio segmento, anos (4 digitos), e
        # referencias a exercicios/secoes no formato N.N.
        heavy = []
        for s in segs:
            body = re.sub(r"^SEGMENT\s+\d+", "", s)          # rotulo do segmento
            body = re.sub(r"\b(1[5-9]|20)\d{2}\b", "", body)  # anos 1500-2099
            body = re.sub(r"\b\d+\.\d+\b(?!\s*percent)", "", body)  # exercicio 1.2, secao 4.3
            body = re.sub(r"(?i)\bchapters?\s+\d+(\s+and\s+\d+)?", "", body)  # "chapter 4"
            k = len(re.findall(r"\b\d[\d,\.]*\b", body))
            if k > 3:
                heavy.append(f"{s.split('.')[0][:22]}={k}")
        if heavy:
            fails.append(f"R3 numerais: {'; '.join(heavy)}")
        # R4 - diz o que pular
        if not any(m in low for m in SKIP_MARKERS):
            fails.append("R4 nao diz o que pular")
        # R5 - escopo negativo no audio
        banned = [b for b in BANNED_AUDIO if b in low]
        if banned:
            fails.append(f"R5 trava negativa: {', '.join(banned)}")
        # R7 - instrucao sem equivalente em slide
        if not any(m in low for m in HOST_MARKERS):
            fails.append("R7 sem instrucao propria de audio")
        # R11 - duracao no prompt
        if re.search(r"\d{2}\s*-\s*\d{2}\s*min", low):
            fails.append("R11 pede duracao")

    if is_video:
        # R13 - no maximo 6 batidas
        if len(segs) > 6:
            fails.append(f"R13 {len(segs)} batidas > 6")
        # R12 - cada batida nomeia um visual
        mudas = [x.split(".")[0][:22] for x in segs
                 if not any(m in x.lower() for m in VISUAL_MARKERS)]
        if mudas:
            fails.append(f"R12 batida sem visual: {'; '.join(mudas)}")
        # R16 - fecha com a imagem unica
        if not any(m in low for m in CLOSE_MARKERS):
            fails.append("R16 sem imagem de fechamento")
        # R5 - escopo negativo
        banned = [b for b in BANNED_AUDIO if b in low]
        if banned:
            fails.append(f"R5 trava negativa: {', '.join(banned)}")
        # R11 - duracao no prompt
        if re.search(r"\d{2}\s*-\s*\d{2}\s*min", low):
            fails.append("R11 pede duracao")

    rows.append((f, n, len(segs), fails))
    total_fail += bool(fails)

print(f"{'chars':>6} {'seg':>4}  {'status':<6} arquivo")
print("-" * 78)
for f, n, s, fails in rows:
    print(f"{n:6} {s:4}  {'FALHA' if fails else 'ok':<6} {f.parent.name}/{f.name}")
    if fails and VERBOSE:
        for x in fails:
            print(f"{'':14}  - {x}")
print("-" * 78)
print(f"{len(rows)-total_fail}/{len(rows)} conformes")
if total_fail and not VERBOSE:
    print("rode com -v para ver as violacoes")
sys.exit(1 if total_fail else 0)
