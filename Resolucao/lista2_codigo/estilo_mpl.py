"""Estilo comum das figuras da Lista 1.

Importar ANTES de 'matplotlib.pyplot'. Usa o backend pgf: o texto das figuras e
composto pelo proprio pdflatex, com lmodern + cmap. Sem isso o matplotlib embute
DejaVu como fonte Type 3 e o texto do PDF final deixa de ser copiavel -- o que a
regra global do projeto proibe.

Verificacao: pdffonts <arquivo>.pdf  ->  nenhuma linha 'Type 3'.
"""
import matplotlib

# Largura util do texto do documento, em polegadas: a4 (21 cm) menos 2x2,4 cm de
# margem = 16,2 cm. Gerar a figura JA nesse tamanho e inclui-la com
# width=\textwidth evita o reescalonamento que encolheria o texto da figura.
TEXTWIDTH_IN = 16.2 / 2.54

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "text.usetex": True,
    "pgf.rcfonts": False,
    "font.family": "serif",
    "font.size": 9,
    "axes.titlesize": 9,
    "axes.labelsize": 9,
    "legend.fontsize": 8,
    "xtick.labelsize": 7.5,
    "ytick.labelsize": 7.5,
    "pgf.preamble": "\n".join([
        r"\usepackage[utf8]{inputenc}",
        r"\usepackage[T1]{fontenc}",
        r"\usepackage{lmodern}",
        r"\usepackage{cmap}",
        r"\usepackage{amsmath}",
    ]),
})
