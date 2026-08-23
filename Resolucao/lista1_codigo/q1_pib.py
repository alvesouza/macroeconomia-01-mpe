"""Lista 1, Questao 1 -- PIB nominal, real, indices de precos e PPC.

Todos os numeros do gabarito sao produzidos aqui. Nada e afirmado sem conta.
Usa Fraction para que os resultados saiam exatos (sem erro de ponto flutuante).
"""
from fractions import Fraction as F
import numpy as np
import pandas as pd

# ---------------------------------------------------------------- 1) dados
# Brasil (reais)
p_br = pd.DataFrame({"bem1": [8, 2], "bem2": [4, 6]}, index=[2024, 2025])
q_br = pd.DataFrame({"bem1": [5, 12], "bem2": [4, 3]}, index=[2024, 2025])
# Colombia (pesos), so 2024
p_co = pd.Series({"bem1": 40, "bem2": 8})
q_co = pd.Series({"bem1": 1, "bem2": 2})
CAMBIO = 25.0        # pesos por real


def valor(precos, quantidades):
    """Soma_i p_i q_i, exata."""
    return sum(F(int(precos[b])) * F(int(quantidades[b])) for b in precos.index)


# ------------------------------------------------- (a) PIB nominal Brasil
pib_nom = {t: valor(p_br.loc[t], q_br.loc[t]) for t in (2024, 2025)}
print("(a) PIB nominal 2024 =", pib_nom[2024], "reais")
print("    PIB nominal 2025 =", pib_nom[2025], "reais")
print("    variacao nominal =", f"{float(pib_nom[2025]/pib_nom[2024]-1)*100:+.2f}%")

# ------------------------------- (b) PIB real a precos de 2024 (Laspeyres)
real_2025_p24 = valor(p_br.loc[2024], q_br.loc[2025])
real_2024_p24 = pib_nom[2024]
g_L = real_2025_p24 / real_2024_p24 - 1
print(f"\n(b) PIB real 2025 a precos de 2024 = {real_2025_p24} reais")
print(f"    PIB real 2024 a precos de 2024 = {real_2024_p24} reais (= nominal)")
print(f"    crescimento (base 2024) = {real_2025_p24}/{real_2024_p24} - 1 = "
      f"{g_L} = {float(g_L)*100:+.2f}%")

# --------------------------------- (c) PIB real a precos de 2025 (Paasche)
real_2024_p25 = valor(p_br.loc[2025], q_br.loc[2024])
real_2025_p25 = pib_nom[2025]
g_P = real_2025_p25 / real_2024_p25 - 1
print(f"\n(c) PIB real 2024 a precos de 2025 = {real_2024_p25} reais")
print(f"    PIB real 2025 a precos de 2025 = {real_2025_p25} reais (= nominal)")
print(f"    crescimento (base 2025) = {real_2025_p25}/{real_2024_p25} - 1 = "
      f"{g_P} = {float(g_P)*100:+.2f}%")

# indices de quantidade e de preco, e o encadeamento de Fisher
Q_L, Q_P = real_2025_p24 / real_2024_p24, real_2025_p25 / real_2024_p25
P_L, P_P = real_2024_p25 / real_2024_p24, real_2025_p25 / real_2025_p24
Q_F, P_F = np.sqrt(float(Q_L * Q_P)), np.sqrt(float(P_L * P_P))
print(f"\n    indice de QUANTIDADE  Laspeyres {float(Q_L):.6f} | "
      f"Paasche {float(Q_P):.6f} | Fisher {Q_F:.6f}  -> g = {100*(Q_F-1):+.2f}%")
print(f"    indice de PRECO       Laspeyres {float(P_L):.6f} | "
      f"Paasche {float(P_P):.6f} | Fisher {P_F:.6f}  -> pi = {100*(P_F-1):+.2f}%")
print(f"    deflator implicito 2025 (base 2024 = 100): "
      f"{100*float(pib_nom[2025]/real_2025_p24):.2f}")
# teste do produto: P_F * Q_F tem de reproduzir a razao dos PIBs nominais
razao_nom = float(pib_nom[2025] / pib_nom[2024])
print(f"    [check] P_F * Q_F = {P_F*Q_F:.10f}  vs  nominal_2025/nominal_2024 = "
      f"{razao_nom:.10f}  -> {'OK' if abs(P_F*Q_F - razao_nom) < 1e-12 else 'FALHOU'}")
print(f"    [check] Laspeyres_Q * Paasche_P = {float(Q_L*P_P):.10f} -> "
      f"{'OK' if abs(float(Q_L*P_P) - razao_nom) < 1e-12 else 'FALHOU'}")

# --- por que Laspeyres != Paasche: a decomposicao de Bortkiewicz ------------
# r_i = relativo de preco, s_i = relativo de quantidade, w_i = peso no valor de 2024
r = np.array([float(p_br.loc[2025, b] / p_br.loc[2024, b]) for b in p_br.columns])
s = np.array([float(q_br.loc[2025, b] / q_br.loc[2024, b]) for b in q_br.columns])
v = np.array([float(p_br.loc[2024, b] * q_br.loc[2024, b]) for b in p_br.columns])
wts = v / v.sum()
cov = (wts * r * s).sum() - (wts * r).sum() * (wts * s).sum()
razao_QP_QL = 1 + cov / ((wts * r).sum() * (wts * s).sum())
print(f"\n    relativos de preco r = {r},  de quantidade s = {s},  pesos w = {wts.round(4)}")
print(f"    cov_w(r,s) = {cov:+.6f}  (negativa => substituicao)")
print(f"    Bortkiewicz: Q_P/Q_L = 1 + cov/(P_L*Q_L) = {razao_QP_QL:.6f}"
      f"   vs direto {float(Q_P/Q_L):.6f} -> "
      f"{'OK' if abs(razao_QP_QL - float(Q_P/Q_L)) < 1e-12 else 'FALHOU'}")

# ------------------------------------------- (d) PIB colombiano ao cambio
pib_co_pesos = valor(p_co, q_co)
pib_co_cambio = float(pib_co_pesos) / CAMBIO
print(f"\n(d) PIB Colombia 2024 = {pib_co_pesos} pesos")
print(f"    ao cambio de mercado = {pib_co_pesos}/{CAMBIO:.0f} = "
      f"{pib_co_cambio:.2f} reais  ({100*pib_co_cambio/float(pib_nom[2024]):.1f}% do PIB do Brasil)")

# ---------------------------------------------------- (e) PIB colombiano PPC
pib_co_ppc = valor(p_br.loc[2024], q_co)          # cesta colombiana a precos do Brasil
print(f"\n(e) PIB Colombia 2024 a precos brasileiros (PPC) = {pib_co_ppc} reais"
      f"  ({100*float(pib_co_ppc)/float(pib_nom[2024]):.1f}% do PIB do Brasil)")
print(f"    razao PPC/cambio = {float(pib_co_ppc)/pib_co_cambio:.3f}x")

# o mesmo problema de numero-indice, agora ENTRE PAISES: a que precos comparar?
rel_precos_br = float(pib_co_ppc) / float(pib_nom[2024])           # a precos do Brasil
pib_br_pesos_ = valor(p_co, q_br.loc[2024])
rel_precos_co = float(pib_co_pesos) / float(pib_br_pesos_)         # a precos da Colombia
print(f"    Colombia/Brasil a precos brasileiros  = {rel_precos_br:.4f}")
print(f"    Colombia/Brasil a precos colombianos  = {rel_precos_co:.4f}")
print(f"    media geometrica (Fisher)             = "
      f"{np.sqrt(rel_precos_br*rel_precos_co):.4f}")

# taxa de cambio PPC implicita, pelas duas cestas + media geometrica (Fisher)
ppc_cesta_co = float(pib_co_pesos) / float(pib_co_ppc)               # cesta da Colombia
pib_br_pesos = valor(p_co, q_br.loc[2024])                           # cesta do Brasil
ppc_cesta_br = float(pib_br_pesos) / float(pib_nom[2024])
print(f"    cambio PPC pela cesta colombiana = {float(pib_co_pesos)}/{float(pib_co_ppc)}"
      f" = {ppc_cesta_co:.3f} pesos/real")
print(f"    cambio PPC pela cesta brasileira = {float(pib_br_pesos)}/{float(pib_nom[2024])}"
      f" = {ppc_cesta_br:.3f} pesos/real")
print(f"    cambio PPC de Fisher = {np.sqrt(ppc_cesta_co*ppc_cesta_br):.3f} pesos/real"
      f"   vs cambio de mercado = {CAMBIO:.0f}")
print(f"    nivel de precos da Colombia (mercado/PPC) = "
      f"{np.sqrt(ppc_cesta_co*ppc_cesta_br)/CAMBIO:.3f}  (<1 => Colombia e barata)")

# precos relativos: a origem economica da diferenca
print(f"\n    preco relativo p1/p2 no Brasil  = {p_br.loc[2024,'bem1']/p_br.loc[2024,'bem2']:.1f}")
print(f"    preco relativo p1/p2 na Colombia = {p_co['bem1']/p_co['bem2']:.1f}")
