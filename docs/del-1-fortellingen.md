# Komposisjon – Del 1: Fortellingen

**Tidsbruk:** ca. 2,5–3 minutter

**Åpning**

*(Ingen slides, eller kun tittelen på skjermen.)*

«Da jeg først skulle lage en presentasjon til Rubiks om data engineering,
hadde jeg lyst til å gå teknisk dypt ned i open source-rammeverk
for å drive data engineering – “localhost first” og cloud native:
Delta Lake, DuckDB, Arrow, delta-rs.»

«Men etter hvert som jeg jobbet med dette,
innså jeg at det er noe mer fundamentalt jeg vil dele.»

«Selve utgangspunktet for det jeg mener er viktigst for data engineering i 2026:
grensesnittet mellom dataingeniør, (data-)plattformutvikler og systemutvikler.»

«Og hvorfor systemutviklingsmentaliteten er helt avgjørende for en dataingeniør.»

**Kort om meg**

«Jeg heter [Navn], jobber med data og plattform på [Arbeidsplass].»
«Jeg liker å bygge små, flyttbare prosesser – og lære av det som fungerer.»

«La meg begynne med en kort historie.»

**Tolv megabyte**

Filen kom en tirsdag. Tolv megabyte, komprimert. En CSV.
«Kan dere bare gjøre disse dataene tilgjengelige for analyse?» stod det i e-posten.

Den første uken var møterommet fullt.
Teamleder, arkitekt, sikkerhet, plattformutvikler.
Dataingeniøren satt litt lenger ned langs bordet.
Han hadde åpnet fila, men lukket den igjen da møtet startet.

Arkitekturtegningen vokste raskt.
Bokser, piler, standarder.
Noen foreslo streaming, noen batch.
Arkitekten foreslo begge deler.
Plattformutvikleren snakket om drift.
Sikkerhet om tilgang.

– Vi må gjøre dette riktig, sa arkitekten.  
– Vi må bruke plattformen.

Plattformen var et trygt ord. Det betydde at alle hadde bidratt, og at ingen måtte forklare for mye.

Uke to var filen borte.
Den var blitt til et datasett, så en strøm, så et mellomlager.
Ingen åpnet den lenger.
Koden lå i et repo ingen hadde klonet lokalt.
Jobben kjørte i et miljø de færreste hadde tilgang til.

Når noe feilet, samlet de seg igjen.

– Det er nok noe med infrastrukturen.  
– Det er sikkert rettigheter.  
– Det må være skjemaet.

Ingen sa: Det er koden min.

Så kom spørsmålet fra forretning, dagen før styringsmøtet:
«Når kan vi få tallene?»

Og det var da det gikk opp for dem at ingen hadde sett på selve dataene
siden den første tirsdagen.

Etter hvert ble det vanskelig å svare på enkle spørsmål.
Hvor lang tid tar det å endre én kolonne?
Hvem eier egentlig jobben?
Kan vi teste dette lokalt?

En kveld, etter at resten av teamet hadde gått, åpnet han fila igjen.
Den var fortsatt tolv megabyte.
Kolonnene var de samme.
Innholdet hadde ikke blitt mer komplisert, bare veien dit.
Han skrev litt kode.
Bare nok til å lese fila, gjøre det ene de faktisk trengte, og skrive resultatet ut igjen.
Han kjørte det lokalt.
Input. Kode. Output. Alt var synlig.

Neste dag viste han det frem.  
– Hvor kjører den? spurte teamlederen.  
– Der det passer, svarte han.  
– På hvilken plattform? spurte arkitekten.  
– På nesten hvilken som helst.

Plattformutvikleren så opp.  
– Men vi har jo en plattform?

Han nikket.
Plattformen var fin. Robust. Viktig.
Men dette var ikke bundet til den.
Det var bare en prosess.
Kode som kunne kjøres lokalt, i CI, i skyen – eller et annet sted senere.
Den kunne flyttes uten å skrives om.

De kjørte koden sammen.
For første gang på lenge visste alle hva som faktisk skjedde.
Hvor dataene kom fra.
Hva som ble endret.
Hvor de endte.
Ansvar var ikke lenger fordelt på roller, men samlet i prosessen.

Plattformen forsvant ikke etter det.
Den sluttet bare å være startpunktet.
Nå begynte de med det minste som fungerte.
Med kode som kunne eies.
Når behovene vokste, kunne prosessen vokse med dem – dit det ga mest mening.

Filen er borte nå. Løst, levert, arkivert.
Men noe ble igjen.
Når nye oppgaver kommer inn, spør de ikke først hvor dette skal kjøre.
De spør hva som faktisk må skje.
Og noen ganger, før de åpner møtekalenderen, åpner de dataene.

---
[Neste: Del 2 – Broen](del-2-broen.md)

[Til hovedoversikt](komposisjon.md)
