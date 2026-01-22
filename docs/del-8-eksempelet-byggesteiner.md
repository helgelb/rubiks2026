# Komposisjon – Del 8: Eksempelet (byggesteinene og oppsettet)

**Tidsbruk:** ca. 1,5–2 minutter

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

---
[← Forrige: Del 7 – Eksempelet (introduksjon og mål)](del-7-eksempelet-intro.md) | [Neste: Del 9 – Eksempelet (demoen)](del-9-eksempelet-demo.md)

[Til hovedoversikt](komposisjon.md)
