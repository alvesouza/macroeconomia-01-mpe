"""Fetch the World Bank WDI series lecture 1 needs, with self-confirming names.

Python's TLS stack fails against api.worldbank.org in this environment (SSLEOFError), so
the request goes through curl. Each indicator's own name is read back out of the payload
and printed: no series is ever asserted to be something the source did not call itself.
"""
import json, csv, hashlib, pathlib, subprocess

INDICATORS = [
    "NY.GDP.PCAP.PP.KD",  # income per head, constant PPP -> levels and the convergence scatter
    "NE.GDI.TOTL.ZS",     # gross capital formation, % of GDP -> the model's s
    "SP.POP.GROW",        # population growth -> the model's n
]
COUNTRIES = "all"
OUT = pathlib.Path("data")


def get(url: str) -> list:
    """Return the parsed JSON body of url, fetched with curl. Raises on a non-zero exit."""
    r = subprocess.run(["curl", "-s", "-m", "90", url], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"curl failed ({r.returncode}) on {url}")
    return json.loads(r.stdout)


for code in INDICATORS:
    url = (f"https://api.worldbank.org/v2/country/{COUNTRIES}/indicator/{code}"
           f"?format=json&date=1960:2024&per_page=20000")
    rows = get(url)[1] or []
    name = rows[0]["indicator"]["value"] if rows else "<empty>"
    f = OUT / f"wdi_{code.lower().replace('.', '_')}.csv"
    with f.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["country", "iso3", "year", "value"])
        for d in sorted(rows, key=lambda d: (d["countryiso3code"], d["date"])):
            w.writerow([d["country"]["value"], d["countryiso3code"], d["date"], d["value"]])
    print(f"{code}\n  API name : {name}\n  rows={len(rows)}  "
          f"sha256={hashlib.sha256(f.read_bytes()).hexdigest()[:16]}  -> {f}")
