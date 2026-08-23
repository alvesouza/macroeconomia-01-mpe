"""Lista 2, Questao 2 -- Gotham: capital de seguranca, PTF medida e residuo de Solow.

Y = A K_P^alpha L^{1-alpha},  K_seg = theta*K_P,  K = (1+theta)K_P
=> Y = A (1+theta)^{-alpha} K^alpha L^{1-alpha}

Calibracao pedida: alpha = 1/3, theta = 0.5, theta' = theta/4 = 0.125.
"""
from fractions import Fraction as F
import numpy as np

ALPHA = F(1, 3)
THETA = F(1, 2)
THETA_L = THETA / 4          # theta' = (1/4) theta
A_TRUE = 1.0                 # normalizacao: os resultados sao todos RAZOES a A

af, tf, tlf = float(ALPHA), float(THETA), float(THETA_L)

# =============================================================== (a)
print("=" * 72)
print("(a) produto total, fracao de seguranca e perda de produto")
print("=" * 72)
print(f"  K = K_P + theta*K_P = (1+theta)K_P  =>  K_P = K/(1+theta)")
print(f"  Y = A (1+theta)^(-alpha) K^alpha L^(1-alpha)")
frac_seg = THETA / (1 + THETA)
print(f"\n  fracao do capital MEDIDO em seguranca = theta/(1+theta) = "
      f"{frac_seg} = {float(frac_seg)*100:.4f}%")
print(f"  fracao produtiva                      = 1/(1+theta)     = "
      f"{1/(1+THETA)} = {float(1/(1+THETA))*100:.4f}%")

perda = (1 + tf) ** (-af)
print(f"\n  Y(theta)/Y(theta=0) com o MESMO K = (1+theta)^(-alpha) = "
      f"1.5^(-1/3) = {perda:.6f}")
print(f"  => perde-se {100*(1-perda):.4f}% do produto por causa do crime")
# verificacao numerica direta
K, L = 1.0, 1.0
Y_crime = A_TRUE * (K / (1 + tf)) ** af * L ** (1 - af)
Y_sem = A_TRUE * K ** af * L ** (1 - af)
print(f"  [check] direto: Y_crime/Y_sem = {Y_crime/Y_sem:.6f} -> "
      f"{'OK' if abs(Y_crime/Y_sem - perda) < 1e-12 else 'FALHOU'}")

# =============================================================== (b)
print()
print("=" * 72)
print("(b) problema da firma e participacoes medidas")
print("=" * 72)
print("  max_{K_P,L}  A K_P^a L^(1-a) - r(1+theta)K_P - wL")
print("  CPO K_P: a A K_P^(a-1) L^(1-a) = r(1+theta)  =>  a Y/K_P = r(1+theta)")
print("           como K = (1+theta)K_P:  r = a Y / K")
print("  CPO L  : (1-a) Y / L = w")

Y = Y_crime
K_P = K / (1 + tf)
r = af * Y / K
w = (1 - af) * Y / L
# checar as CPO na forma original
cpo_K = af * A_TRUE * K_P ** (af - 1) * L ** (1 - af)
print(f"\n  numericamente (A=K=L=1): Y = {Y:.6f}, K_P = {K_P:.6f}")
print(f"    r = aY/K = {r:.6f}   |  [check] CPO: aA K_P^(a-1)L^(1-a) = {cpo_K:.6f}"
      f" = r(1+theta) = {r*(1+tf):.6f} -> "
      f"{'OK' if abs(cpo_K - r*(1+tf)) < 1e-12 else 'FALHOU'}")
print(f"    w = (1-a)Y/L = {w:.6f}")
print(f"\n  participacao do capital medida = rK/Y = {r*K/Y:.10f}  (alpha = {af:.10f})")
print(f"  participacao do trabalho medida = wL/Y = {w*L/Y:.10f}  (1-alpha = {1-af:.10f})")
print(f"  lucro = Y - rK - wL = {Y - r*K - w*L:.2e}  (zero: CRS em (K,L))")
print("\n  => as participacoes NAO sao distorcidas pelo crime.")

# =============================================================== (c)
print()
print("=" * 72)
print("(c) o 'riddler': development accounting a la Kurlat 5.3")
print("=" * 72)
A_hat = Y / (K ** af * L ** (1 - af))
print(f"  o riddler supoe Y = A_hat K^a L^(1-a) e inverte:")
print(f"    A_hat = Y/(K^a L^(1-a)) = {A_hat:.6f}")
print(f"    analitico: A_hat = A (1+theta)^(-alpha) = {A_TRUE*(1+tf)**(-af):.6f} -> "
      f"{'OK' if abs(A_hat - A_TRUE*(1+tf)**(-af)) < 1e-12 else 'FALHOU'}")
print(f"  A_hat/A = {A_hat/A_TRUE:.6f}  =>  subestima a produtividade em "
      f"{100*(1-A_hat/A_TRUE):.4f}%")
print(f"  o alpha do riddler: calibrado pela participacao do capital = "
      f"{r*K/Y:.6f} = alpha verdadeiro -> CORRETO")
print("  => todo o erro cai sobre a PTF; nenhum dado de participacao denuncia o crime.")

# =============================================================== (d)
print()
print("=" * 72)
print("(d) WayneTech: theta -> theta' = theta/4, contabilidade do crescimento")
print("=" * 72)
razao = (1 + THETA) / (1 + THETA_L)
print(f"  theta = {THETA} -> theta' = {THETA_L}")
print(f"  (1+theta)/(1+theta') = ({1+THETA})/({1+THETA_L}) = {razao} = {float(razao):g}")

# residuo de Solow acumulado na decada = alpha * ln[(1+theta)/(1+theta')]
res_log = af * np.log(float(razao))
res_nivel = float(razao) ** af
print(f"\n  Kurlat (5.4.2):  g_Y = (part. capital) g_K + (part. trabalho) g_L + residuo")
print(f"  com as participacoes medidas = (alpha, 1-alpha) pelo item (b):")
print(f"    dlnY = alpha*dlnK + (1-alpha)*dlnL - alpha*dln(1+theta)")
print(f"    residuo = dlnY - alpha*dlnK - (1-alpha)*dlnL = -alpha*dln(1+theta)")
print(f"            = alpha*ln[(1+theta)/(1+theta')] = (1/3)*ln(4/3) = {res_log:.6f}")
print(f"\n  A_hat sobe por um fator (4/3)^(1/3) = {res_nivel:.6f} na decada"
      f"  ({100*(res_nivel-1):+.4f}%)")
print(f"  taxa anual composta = {res_nivel:.6f}^(1/10) - 1 = "
      f"{res_nivel**0.1 - 1:.6f} = {100*(res_nivel**0.1 - 1):.4f}% ao ano")
print(f"  taxa anual em log   = {res_log/10:.6f} = {100*res_log/10:.4f}% ao ano")

# INDEPENDENCIA de g_K e g_L: verificacao numerica com valores arbitrarios
print("\n  o residuo NAO depende de g_K nem de g_L -- verificacao:")
for gK, gL in [(0.0, 0.0), (0.03, 0.01), (0.10, -0.02), (0.005, 0.04)]:
    K0, L0 = 1.0, 1.0
    K1, L1 = K0 * (1 + gK) ** 10, L0 * (1 + gL) ** 10
    Y0 = A_TRUE * (K0 / (1 + tf)) ** af * L0 ** (1 - af)
    Y1 = A_TRUE * (K1 / (1 + tlf)) ** af * L1 ** (1 - af)
    residuo = (np.log(Y1 / Y0) - af * np.log(K1 / K0) - (1 - af) * np.log(L1 / L0))
    print(f"    g_K={gK:+.3f}, g_L={gL:+.3f} -> residuo na decada = {residuo:.8f}"
          f"  ({'OK' if abs(residuo - res_log) < 1e-10 else 'FALHOU'})")

# composicao do capital antes e depois
print(f"\n  capital de seguranca: {float(THETA/(1+THETA))*100:.2f}% -> "
      f"{float(THETA_L/(1+THETA_L))*100:.2f}% do estoque medido")
print(f"  capital produtivo   : {float(1/(1+THETA))*100:.2f}% -> "
      f"{float(1/(1+THETA_L))*100:.2f}%")

# e se o crime PIORASSE?
print("\n  contrafactual -- se o crime piorasse (theta -> 4*theta = 2):")
razao_pior = (1 + THETA) / (1 + 4 * THETA)
res_pior = af * np.log(float(razao_pior))
print(f"    (1+theta)/(1+theta'') = ({1+THETA})/({1+4*THETA}) = {razao_pior}")
print(f"    residuo = (1/3)*ln(0.5) = {res_pior:.6f} -> A_hat cai "
      f"{100*(1-float(razao_pior)**af):.2f}% na decada")
print(f"    = {100*((float(razao_pior)**af)**0.1 - 1):.4f}% ao ano -> "
      f"o exercicio reportaria REGRESSO tecnologico")
