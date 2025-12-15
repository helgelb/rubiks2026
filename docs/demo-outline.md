# Demo-outline

rekkefølge + replikker

Dette er designet for ~4 minutter, stabilt, og tett koblet til historien.

## Steg 0 — Sett premisset

(10–15 sek)

Du sier:

«Dette er ikke en demo av et rammeverk. Det er en demo av et startpunkt.»
«Vi skal lage analyseklar data med en prosess som kan flyttes nesten hvor som helst.»

## Steg 1 — Vis mappen

(10–15 sek)

Du gjør: åpner demo/ og viser filene (kort).
Du sier:

«Dette er hele prosjektet. Ingen YAML. Ingen miljømagi.»
«Én inputfil, én prosess, én output.»

## Steg 2 — Vis inputdata

(15–20 sek)

Du gjør: åpner input/customers.csv.
Du sier:

«Dette er tolv-megabyte-øyeblikket. Data er ofte enklere enn systemet rundt.»

## Steg 3 — Vis prosessen

(45–60 sek)

Du gjør: åpner process.py. Pek på tre blokker: les → transform → skriv.
Du sier:

«Dette er hele prosessen.»
«Den leser CSV, gjør én transformasjon som er lett å forstå, og skriver et varig resultat.»
«Alt er eksplisitt. Ingenting skjer i bakgrunnen.»

## Steg 4 — Kjør prosessen lokalt

(20–30 sek)

Du gjør:

```bash
python process.py
```

Du sier:

«Ingen deploy. Ingen plattformvalg.»
«Bare kode.»

(vent til “Done. Wrote: …”)

Steg 5 — Bevis at output er ekte og brukbart (30–45 sek)

Du gjør:

```bash
python support/query_output.py
```

(den printer rader + telling per land)

Du sier:

«Nå har vi analyseklar data. Dette er ikke et mellomlager i et stort system.»
«Dette er et resultat du kan bygge videre på – analyse, rapportering, eller neste prosess.»

Steg 6 — Bevis kontroll med pytest (30–45 sek)

Du gjør:

```bash
pytest -q
```

Du sier:

«Dette er ‘engineering’-delen.»
«Vi beviser at prosessen er korrekt og reproduserbar.»
«Det gjør den trygg å flytte, og trygg å drifte.»

Steg 7 — Lever poenget (15–20 sek)

Du sier (viktig):

«Poenget er ikke at dette kjører lokalt.»
«Poenget er at dette kan flyttes.»
«Plattformen er ikke borte – men den er ikke et krav for å komme i gang.»

Overgang til Del 6:

«Og når vi jobber slik, skjer det noen interessante ting – både teknisk og organisatorisk…»

Hvis du vil, kan jeg også lage en Windows-vennlig run_demo.ps1 og/eller en Dockerfile som bevarer “samme prosess, ny runtime” (som er et veldig sterkt portabilitetsbevis) — men jeg venter til du ber om det.