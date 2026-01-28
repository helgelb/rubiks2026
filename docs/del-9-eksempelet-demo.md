# Del 9 – Eksempelet: Demoen (to lag)

## A) Det jeg sier høyt (talekst)

Dette er ikke en demo av et rammeverk. Det er en demo av et startpunkt.

Vi har én input, én prosess og én output.  
Prosessen gjør tre ting: leser, transformerer og skriver.

Så kjører vi tester. Ikke fordi det er fancy, men fordi det gjør dette trygt å flytte.

Poenget er ikke at dette kjører lokalt.  
Poenget er at det kan flyttes.

Plattformen er ikke borte.  
Den er bare ikke et krav for å komme i gang.

---

## B) Hva jeg gjør (runbook / operator-manus)

**Steg 1 — Vis mappen**  
Åpne `src/` og vis filene kort.  
«Dette er hele prosjektet. Én input, én prosess, én output.»

**Steg 2 — Vis inputdata**  
Åpne `input/customers.csv`.  
«Data er ofte enklere enn systemet rundt.»

**Steg 3 — Vis prosessen**  
Åpne `process.py`. Pek på tre blokker: les → transform → skriv.  
«Alt er eksplisitt. Ingenting skjer i bakgrunnen.»

**Steg 4 — Kjør prosessen lokalt**
```bash
python process.py --input input/customers.csv --output output/customers.parquet
```

**Steg 5 — Bevis at output er ekte og brukbar**
```bash
python support/query_output.py
```

**Steg 6 — Bevis kontroll med tester**
```bash
pytest -q
```


**Steg 7 — Lever poenget (knyt tilbake)**  
«Poenget er ikke at dette kjører lokalt. Poenget er at det kan flyttes.»  
«Plattformen er ikke borte. Den er bare ikke et krav for å komme i gang.»

---
[← Forrige: Del 8 – Eksempelet (byggesteinene og oppsettet)](del-8-eksempelet-byggesteiner.md) | [Neste: Del 10 – Konsekvensene](del-10-konsekvensene.md)

[Til hovedoversikt](komposisjon.md)
