# Del 8 – Eksempelet: byggesteiner og oppsett

Her er byggeklossene vi bruker for å få det til, med lav friksjon og høy flyttbarhet:

- **Åpne formater (Parquet/Delta)** som kontrakt mellom prosesser – språkagnostisk og raskt.
- **DuckDB** som lokal motor: produksjonsnær SQL uten cluster.
- **Arrow** som datavei mellom Python/Rust/JVM, uten unødvendige kopier.
- **Transaksjonslag (delta-rs / Delta Lake)** for historikk, schema-evolusjon og reproduserbarhet.

Dette er ikke “cloud native” som buzzword.  
Dette er **portabilitet som designvalg**.

Oppgaven er enkel:
- Input: CSV  
- Én tydelig transformasjon  
- Output: analyseklar data (Delta)

Teknologi:
Python, DuckDB og Delta – men ikke Spark, ikke cluster, ikke cloud som startpunkt.

---
[← Forrige: Del 7 – Eksempelet (introduksjon og mål)](del-7-eksempelet-intro.md) | [Neste: Del 9 – Eksempelet (demoen)](del-9-eksempelet-demo.md)

[Til hovedoversikt](komposisjon.md)
