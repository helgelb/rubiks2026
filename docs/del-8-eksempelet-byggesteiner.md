# Del 8 – Eksempelet: byggesteiner og oppsett

Her er byggeklossene vi bruker for å få det til, med lav friksjon:
- åpne formater (Parquet/Delta) som kontrakt  
- en lokal motor (DuckDB) for SQL uten cluster  
- Arrow for effektiv dataflyt  
- et transaksjonslag (delta-rs / Delta Lake) for historikk og reproduserbarhet  

Poenget er at vi kan begynne lokalt, og likevel være “cloud native” senere.

Oppgaven er enkel:
- Input: CSV  
- Én enkel transformasjon  
- Output: analyseklar data (Delta)  

Teknologi:
Python, DuckDB, Delta – men ikke Spark, ikke cluster, ikke cloud.

---
[← Forrige: Del 7 – Eksempelet (introduksjon og mål)](del-7-eksempelet-intro.md) | [Neste: Del 9 – Eksempelet (demoen)](del-9-eksempelet-demo.md)

[Til hovedoversikt](komposisjon.md)
