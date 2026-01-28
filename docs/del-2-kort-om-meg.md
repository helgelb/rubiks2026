# Del 2 – Kort om meg

Jeg heter **Helge**, og jeg jobber med data og plattform i Equinor.

Jeg har jobbet med data engineering i snart åtte år, og jeg har kjent på hvordan faget har skiftet form – flere ganger.

Jeg startet med store helseregistre. Mye var SQL, SSIS og on-prem.  
Det var tungt, men det var tydelig: du så hele løpet.  
Input. Transformasjon. Output.

Så kom behovet for å levere raskere. Sky ble et valg fordi vi kunne levere på timer i stedet for dager.  
Vi brukte Data Factory for å få ting i produksjon fort – og for å orkestrere flyten.

Et par år senere var Synapse “det riktige”.  
Og så kom Fabric, og igjen kom det samme spørsmålet: skal vi migrere – eller bli stående?

Underveis bygde vi mer og mer blandet metodikk:
SQL-kode, klikk-baserte transformasjoner, data flows, og etter hvert notebooks med Spark.  
Alt kjørte i sky, og mer og mer av logikken ble bundet til arbeidsflaten og produktets måte å tenke på.

Det som overrasket meg, var hvor fort den tekniske gjelden kunne vokse i et slikt landskap.  
Transformasjoner som egentlig var enkle, endte opp som store JSON-definisjoner og pipeline-artefakter i repo – vanskelig å lese, vanskelig å teste, og ofte noe nye folk vegret seg for å røre.

Og når verktøy og UI endrer seg fra release til release – eller vi bytter produkt – så er det ikke bare migrering som koster.  
Det er kognitiv last: mer “hvor var det jeg skulle trykke”, mindre “hva er den riktige transformasjonen”.

Det er bakteppet for historien jeg skal fortelle nå.

---
[← Forrige: Del 1 – Åpningen](del-1-apningen.md) | [Neste: Del 3 – Fortellingen](del-3-fortellingen.md)

[Til hovedoversikt](komposisjon.md)
