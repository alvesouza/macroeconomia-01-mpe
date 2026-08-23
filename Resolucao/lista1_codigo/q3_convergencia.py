"""Lista 1, Questao 3 (Kurlat 3.3) -- convergencia dentro de regioes.

Fonte: Penn World Table 10.01 (Feenstra, Inklaar & Timmer, 2015), planilha 'Data'.
Crescimento: rgdpna/pop  (PIB real a precos nacionais constantes -> correto para
             comparar a MESMA economia ao longo do tempo).
Nivel 1960:  rgdpe/pop   (PIB real PPP em precos internacionais -> correto para
             comparar economias DIFERENTES num mesmo ano).
"""
import numpy as np
import pandas as pd

XLSX = "pwt1001.xlsx"
T0, T1 = 1960, 2014
N_ANOS = T1 - T0

EUROPA = """AUT BEL DNK FIN FRA DEU GRC ISL IRL ITA LUX NLD NOR PRT ESP SWE CHE
            GBR CYP MLT BGR HRV CZE EST HUN LVA LTU POL ROU SVK SVN ALB SRB""".split()

AMLAT = """ARG BOL BRA CHL COL CRI CUB DOM ECU SLV GTM HTI HND JAM MEX NIC PAN
           PRY PER TTO URY VEN BRB BHS""".split()

AFRICA = """DZA AGO BEN BWA BFA BDI CMR CPV CAF TCD COM COD COG CIV DJI EGY GNQ
            ETH GAB GMB GHA GIN GNB KEN LSO LBR MDG MWI MLI MRT MUS MAR MOZ NAM
            NER NGA RWA STP SEN SYC SLE ZAF SDN SWZ TZA TGO TUN UGA ZMB ZWE""".split()

REGIOES = {"Europa": EUROPA, "America Latina": AMLAT, "Africa": AFRICA}


def montar_painel(caminho=XLSX):
    d = pd.read_excel(caminho, sheet_name="Data")
    d = d[d.year.isin([T0, T1])].copy()
    d["y_na"] = d.rgdpna / d["pop"]   # serie temporal ('pop' e metodo do DataFrame)
    d["y_pp"] = d.rgdpe / d["pop"]    # comparavel entre paises
    w = d.pivot_table(index=["countrycode", "country"], columns="year",
                      values=["y_na", "y_pp"])
    w.columns = [f"{a}_{b}" for a, b in w.columns]
    w = w.dropna(subset=[f"y_na_{T0}", f"y_na_{T1}", f"y_pp_{T0}"])
    # crescimento medio anual composto (geometrico, NAO aritmetico)
    w["g"] = (w[f"y_na_{T1}"] / w[f"y_na_{T0}"]) ** (1 / N_ANOS) - 1
    w["ly60"] = np.log(w[f"y_pp_{T0}"])
    return w.reset_index()


def regressao(sub):
    """OLS de g sobre ln(y_1960). Devolve inclinacao, erro-padrao, t, R2, n."""
    x, y = sub.ly60.values, sub.g.values
    n = len(x)
    b, a = np.polyfit(x, y, 1)
    res = y - (a + b * x)
    s2 = res @ res / (n - 2)
    se = np.sqrt(s2 / ((x - x.mean()) @ (x - x.mean())))
    r2 = 1 - (res @ res) / ((y - y.mean()) @ (y - y.mean()))
    return dict(n=n, inclinacao=b, intercepto=a, se=se, t=b / se, r2=r2)


def meia_vida(b, T=N_ANOS):
    """Velocidade de convergencia lambda implicita e meia-vida do hiato, em anos.

    CUIDADO: a inclinacao b NAO e -lambda. Regredindo o crescimento MEDIO de T anos
    sobre ln y_0, o modelo de Solow log-linearizado da

        b = -(1 - e^{-lambda T}) / T   =>   lambda = -ln(1 + b T) / T,

    e so para lambda*T pequeno vale b ~ -lambda. Com T=54 a diferenca e grande
    (b=-0.0096 devolve lambda=1.35% a.a., nao 0.96%).

    Segunda ordem: a variavel dependente aqui e a taxa composta (y_T/y_0)^{1/T}-1 e
    nao (1/T)ln(y_T/y_0); a diferenca desloca lambda em muito menos que o erro-padrao.
    """
    if b >= 0 or 1 + b * T <= 0:
        return np.nan, np.nan       # divergencia: lambda nao definido
    lam = -np.log(1 + b * T) / T
    return lam, np.log(2) / lam


if __name__ == "__main__":
    w = montar_painel()
    print(f"Paises com dado em {T0} e {T1}: {len(w)}\n")

    linhas = []
    for nome, membros in {**REGIOES, "Mundo (amostra toda)": None}.items():
        sub = w if membros is None else w[w.countrycode.isin(membros)]
        r = regressao(sub)
        lam, hl = meia_vida(r["inclinacao"])
        linhas.append(dict(regiao=nome, **r, lambda_=lam, meia_vida=hl))
        print(f"{nome:22s} n={r['n']:3d}  b={r['inclinacao']:+.5f} "
              f"(ep {r['se']:.5f}, t={r['t']:+.2f})  R2={r['r2']:.3f}  "
              f"meia-vida={hl:6.1f} anos" if np.isfinite(hl) else
              f"{nome:22s} n={r['n']:3d}  b={r['inclinacao']:+.5f} "
              f"(ep {r['se']:.5f}, t={r['t']:+.2f})  R2={r['r2']:.3f}  meia-vida=  --")

    tab = pd.DataFrame(linhas)
    tab.to_csv("q3_resultados.csv", index=False)

    # extremos de cada regiao, para citar no texto
    for nome, membros in REGIOES.items():
        sub = w[w.countrycode.isin(membros)].sort_values("g")
        print(f"\n--- {nome} (n={len(sub)}) ---")
        print("  menores g:", ", ".join(
            f"{r.country} {100*r.g:.2f}%" for r in sub.head(3).itertuples()))
        print("  maiores g:", ", ".join(
            f"{r.country} {100*r.g:.2f}%" for r in sub.tail(3).itertuples()))
        print("  mais pobre em 1960:", sub.loc[sub.ly60.idxmin()].country,
              f"({np.exp(sub.ly60.min()):,.0f})")
        print("  mais rico  em 1960:", sub.loc[sub.ly60.idxmax()].country,
              f"({np.exp(sub.ly60.max()):,.0f})")
        # razao entre o mais rico e o mais pobre, 1960 vs 2014 (dispersao)
        s60 = np.log(sub[f"y_pp_{T0}"]).std()
        s14 = np.log(sub[f"y_na_{T1}"] / sub[f"y_na_{T0}"] * sub[f"y_pp_{T0}"]).std()
        print(f"  desvio-padrao de ln(y): 1960 = {s60:.3f} -> 2014 = {s14:.3f} "
              f"({'sigma-convergencia' if s14 < s60 else 'sigma-divergencia'})")

    w.to_csv("q3_painel.csv", index=False)
