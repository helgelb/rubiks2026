# Komposisjon – Del 9: Eksempelet (demoen)

**Tidsbruk:** ca. 2,25–2,5 minutter

## 5. Demo – steg for steg

**Steg 0 — Sett premisset** *(10–15 sek)*

«Dette er ikke en demo av et rammeverk. Det er en demo av et startpunkt.»
«Vi skal lage analyseklar data med en prosess som kan flyttes nesten hvor som helst.»

**Steg 1 — Vis mappen** *(10–15 sek)*

Åpne `src/` og vis filene (kort).

«Dette er hele prosjektet. Ingen YAML. Ingen miljømagi.»
«Én inputfil, én prosess, én output.»

**Steg 2 — Vis inputdata** *(15–20 sek)*

Åpne `input/customers.csv`.

«Dette er tolv-megabyte-øyeblikket. Data er ofte enklere enn systemet rundt.»

**Steg 3 — Vis prosessen** *(45–60 sek)*

Åpne `process.py`. Pek på tre blokker: les → transform → skriv.

«Dette er hele prosessen.»
«Den leser CSV, gjør én transformasjon som er lett å forstå, og skriver et varig resultat.»
«Alt er eksplisitt. Ingenting skjer i bakgrunnen.»

Her kan du peke på:

- lesing
- transformasjon
- skriving

**Steg 4 — Kjør prosessen lokalt** *(20–30 sek)*

```bash
python process.py --input input/customers.csv --output output/customers.parquet
```

«Ingen deploy.
Ingen miljøvalg.»

«Bare kode.»

(La kommandoen fullføre.)

**Steg 5 — Bevis at output er ekte og brukbart** *(30–45 sek)*

```bash
python support/query_output.py
```

(Kommandoen printer rader + telling per land.)

«Nå har vi analyseklar data. Dette er ikke et mellomlager i et stort system.»
«Dette er et resultat du kan bygge videre på – analyse, rapportering, eller neste prosess.»

**Steg 6 — Bevis kontroll med pytest** *(30–45 sek)*

```bash
pytest -q
```

«Dette er ‘engineering’-delen.»
«Vi beviser at prosessen er korrekt og reproduserbar.»
«Det gjør den trygg å flytte, og trygg å drifte.»

**Steg 7 — Lever poenget** *(15–20 sek)*

«Poenget er ikke at dette kjører lokalt.»
«Poenget er at dette kan flyttes.»
«Plattformen er ikke borte – men den er ikke et krav for å komme i gang.»

Overgang til Del 10:

«Og når vi jobber slik, skjer det noen interessante ting – både teknisk og organisatorisk…»

## 6. Knyt demoen eksplisitt til poenget

(Denne delen er viktigere enn selve kjøringen.)

«Poenget er ikke at dette er fancy.»

«Poenget er at dette er flyttbart.»

«Den samme prosessen kan:»

- «kjøres i CI»
- «pakkes i en container»
- «kjøres i Kubernetes»
- «eller kjøres på en plattform – senere»
- «Plattformen er ikke borte.»

«Den er bare ikke et krav for å komme i gang.»

## 7. Ha klart til støtte

- én ferdig kjørt output-mappe
- én skjermdump av resultatet
- evt. en kort video du kan spille

Men: si aldri at du har det. Bare vit det.

## 8. Overgangen videre (manus)

(Etter demoen, rolig.)

«Dette er Data Engineering as Code for meg.»

«Små, kjørbare prosesser.
Med tydelig eierskap.»

«Og når vi jobber slik,
skjer det noen interessante ting.»

(Perfekt inngang til Del 10: Hvorfor dette faktisk er bedre.)

---
[← Forrige: Del 8 – Eksempelet (byggesteinene og oppsettet)](del-8-eksempelet-byggesteiner.md) | [Neste: Del 10 – Konsekvensene](del-10-konsekvensene.md)

[Til hovedoversikt](komposisjon.md)
