# Komposisjon – Del 5: Eksempelet (den lille prosessen)

**Tidsbruk:** ca. 4,5–5,5 minutter

(Nå kan energien gå litt opp, men hold det rolig.)

## 1. Overgangen inn i demoen (manus)

«La oss gjøre dette helt konkret.»

«Ikke med et stort system.
Ikke med et diagram.»

«Men med en liten prosess.»

(kort pause)

«Dette er den typen kode dataingeniøren i historien skrev.»

## 2. Hva demoen skal illustrere (tydelig mål)

Demoen skal vise fire ting, og kun disse:

- Prosessen er liten og forståelig
- Den kan kjøres lokalt
- Den er ikke bundet til en plattform
- Den produserer et reelt, varig resultat

## 3. Faglig del: byggesteinene (1,5–2 min)

**Slide-tittel:** «Små byggeklosser, stor effekt»

**Kjernepoeng (si dette):**
«Vi vil ha prosesser som er portable, testbare og lokale – med lavt overhead.»

**Tre egenskaper å fremheve:**
- **Portabilitet:** Samme prosess kan flyttes mellom laptop, CI, container og sky.
- **Testbarhet:** Små prosesser kan verifiseres med enkle tester og gir trygghet.
- **Lokal utvikling:** Kort feedback-loop uten å vente på cluster eller provisioning.

**To praktiske konsekvenser:**
- **Små byggeklosser:** Mindre kompleksitet og tydeligere eierskap.
- **Lite overhead:** Færre tjenester, lavere friksjon, enklere drift.

**Byggesteinene (slide som liste):**
- **Åpne formater (Parquet/Delta):** Kontrakt mellom prosesser, raskt og språkagnostisk.
- **Lokale motorer (DuckDB):** Produksjonslignende SQL uten cluster.
- **Arrow:** Effektiv dataflyt mellom Python, Rust og JVM.
- **Transaksjonslag (delta-rs/Delta Lake):** Historikk, schema-evolusjon, reproduserbarhet.

**Avsluttende setning (bro til demo):**
«Dette er grunnen til at vi kan begynne lokalt – og fortsatt være cloud native senere.»

## 4. Demo-oppsett

**Problem (samme som historien)**

- Input: CSV
- En enkel transformasjon
- Output: analyseklar data (Delta)

**Teknologi**

- Python
- DuckDB
- Delta Lake (via delta-rs eller parquet + metadata)
- Ikke Spark. Ikke cluster. Ikke cloud.

## 5. Demo – steg for steg

**Steg 0 — Sett premisset** *(10–15 sek)*

«Dette er ikke en demo av et rammeverk. Det er en demo av et startpunkt.»
«Vi skal lage analyseklar data med en prosess som kan flyttes nesten hvor som helst.»

**Steg 1 — Vis mappen** *(10–15 sek)*

Åpne `demo/` og vis filene (kort).

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
python process.py input/customers.csv output/
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

Overgang til Del 6:

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

(Perfekt inngang til Del 6: Hvorfor dette faktisk er bedre.)

---
[← Forrige: Del 4 – Skriftet](del-4-skriftet.md) | [Neste: Del 6 – Konsekvensene](del-6-konsekvensene.md)

[Til hovedoversikt](komposisjon.md)
