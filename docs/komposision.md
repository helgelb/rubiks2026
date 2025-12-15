# Komposisjon

## Del 1: Fortellingen

Tidsbruk: ca 2,5 - 3 minutter

**Tolv megabytee**:

(Ingen slides, eller kun tittelen på skjermen.)

Tolv megabyte

Filen kom en tirsdag. Tolv megabyte, komprimert. En CSV.
Kan dere bare gjøre disse dataene tilgjengelige for analyse? stod det i e-posten. Ikke mer.

Den første uken var møterommet fullt. Teamlederen åpnet møtet, arkitekten tegnet, sikkerhet stilte spørsmål før noen hadde rukket å svare, og plattformutvikleren nikket alvorlig til alt som handlet om drift. Dataingeniøren satt et stykke ned langs bordet. Han hadde åpnet fila, men lukket den igjen da møtet startet.

Arkitekturtegningen vokste raskt. Bokser, piler, farger. Noen foreslo streaming. Noen foreslo batch. Arkitekten foreslo begge deler. For sikkerhets skyld. Plattformutvikleren snakket om standarder. Sikkerhet minnet dem på logging og tilgang. Teamlederen noterte fremdrift.

– Vi må gjøre dette riktig, sa arkitekten.
– Vi må bruke plattformen.

Plattformen var et trygt ord. Det betydde at alle hadde bidratt, og at ingen måtte forklare for mye.

Uke to var filen borte. Den var blitt til et datasett, så til en strøm, så til et mellomlager. Ingen åpnet den lenger. De snakket om den i møter, pekte på den i diagrammer, men så den ikke. Koden lå i et repo ingen hadde klonet lokalt. Jobben kjørte i et miljø de færreste hadde tilgang til.

Når noe feilet, samlet de seg igjen.

– Det er nok noe med infrastrukturen.
– Det er sikkert rettigheter.
– Det må være skjemaet.

Ingen sa: Det er koden min.

Etter hvert ble det vanskelig å svare på enkle spørsmål. Hvor lang tid tar det å endre én kolonne? Hvem eier egentlig denne jobben? Kan vi teste dette lokalt? Diagrammet på veggen var tydeligere enn virkeligheten.

En kveld, etter at resten av teamet hadde gått, åpnet han fila igjen. Den var fortsatt tolv megabyte. Kolonnene var de samme. Innholdet hadde ikke blitt mer komplisert, bare veien dit. Han skrev litt kode. Ikke mye. Bare nok til å lese fila, gjøre det ene de faktisk trengte, og skrive resultatet ut igjen. Han kjørte det lokalt. Så én gang til. Input. Kode. Output. Alt var synlig.

Neste dag viste han det frem.
– Hvor kjører den? spurte teamlederen.
– Der det passer, svarte han.
– På hvilken plattform? spurte arkitekten.
– På nesten hvilken som helst.

Plattformutvikleren så opp.
– Men vi har jo en plattform?

Han nikket. Plattformen var fin. Robust. Viktig. Men dette var ikke bundet til den. Det var bare en prosess. Kode som kunne kjøres lokalt, i CI, i skyen, i et container-miljø, eller et annet sted senere. Den kunne flyttes uten å skrives om. Den kunne vokse hvis den måtte.

De kjørte koden sammen. For første gang på lenge visste alle hva som faktisk skjedde. Hvor dataene kom fra. Hva som ble endret. Hvor de endte. Ansvar var ikke lenger fordelt på roller, men samlet i prosessen.

Plattformen forsvant ikke etter det. Den sluttet bare å være startpunktet. Nå begynte de med det minste som fungerte. Med kode som kunne eies. Når behovene vokste, kunne prosessen vokse med dem – dit det ga mest mening.

Filen er borte nå. Løst, levert, arkivert. Men noe ble igjen. Når nye oppgaver kommer inn, spør de ikke først hvor dette skal kjøre. De spør hva som faktisk må skje. Og noen ganger, før de åpner møtekalenderen, åpner de dataene.

## Del 2: Broen (stillhet og gjenkjennelse)

Tidsbruk: ca. 45–60 sekunder

(Pause. Se opp. La rommet være stille et øyeblikk.)

«Jeg tror de fleste her har vært i det møterommet.»

(kort pause)

«Og dette er ikke en historie om dårlige valg.
Det er en historie om gode intensjoner.»

(enda en kort pause)

«Alle gjorde det de mente var riktig.
Arkitekten. Teamlederen. Sikkerhet. Plattform.
Og nettopp derfor ble det så komplekst.»

## Del 3: Gjenkjennelsen (mønsteret)

Tidsbruk: ca. 3:00–3:30 minutter

(Rolig overgang. Første slide kan komme her, men stemmen bærer fortsatt.)

«Hvis denne historien føles kjent, er det ikke tilfeldig.»

«For dette handler ikke om én CSV-fil.
Det handler om et mønster.»

(kort pause)

«Vi starter ofte med det som er størst og tryggest.
Plattformen. Standardene. Arkitekturen.»

«Ikke fordi vi er late.
Men fordi vi er ansvarlige.»

«Rundt bordet sitter det mange roller.
Alle med gode grunner.»

«Arkitekten vil sikre helheten.
Teamlederen vil sikre fremdrift.
Sikkerhet vil sikre etterlevelse.
Plattform vil sikre drift og stabilitet.»

«Og dataingeniøren…
er bare én stemme blant mange.»

(liten pause)

«Så beslutningene blir kollektive.
Og ansvaret blir… diffust.»

«Det er her noe subtilt skjer.»

«Koden flytter lenger og lenger bort fra de som forstår dataene.
Dataene flytter lenger og lenger bort fra de som skriver koden.»

«Til slutt har vi et system som fungerer…
men som ingen helt eier.»

(Nesten siterende tone.)

«– Det er nok noe med infrastrukturen.»
«– Det er sikkert rettigheter.»
«– Det må være skjemaet.»

(kort pause)

«Men nesten aldri:
Det er koden min.»

«Dette er ikke et kulturproblem.
Det er et startpunkt-problem.»

«Vi har bygget veldig gode plattformer.
Men vi har også lært oss å gjemme enkelheten bak dem.»

(Tempo ned, klar for neste del.)

«Og det er nettopp her jeg mener vi trenger å tenke litt annerledes.»

«Ikke mindre seriøst.
Ikke mindre robust.
Bare… tidligere.»

## Del 4: Skriftet (fra plattform til prosess)

Tidsbruk: 3,5 - 4 minutter

(Rolig. Dette er vendepunktet i foredraget.)

«Så hva var det egentlig som endret seg i historien?»

(kort pause)

«Det var ikke teknologien.»

«Det var ikke teamet.»

«Det var rekkefølgen.»

«De sluttet å starte med hvor dette skulle kjøre,
og begynte å starte med hva som faktisk skulle skje.»

(Første tydelige definisjon – sakte, presist.)

«For meg er dette kjernen i det jeg kaller
Data Engineering as Code.»

(kort pause)

«Ikke som et nytt rammeverk.
Ikke som en erstatning for plattformer.»

«Men som et startpunkt.»

«I stedet for å spørre:
Hvilken plattform skal vi bruke?»

(liten pause)

«Spør vi:
Hva er den minste prosessen som løser dette – korrekt, tydelig og med eierskap?»

(Tempo litt opp – energi.)

«En prosess som er:»

«lesbar»

«kjørbar»

«testbar»

«flyttbar»

(kort pause)

«Kode som kan kjøres lokalt.
Kode som kan kjøres i CI.
Kode som kan kjøres i skyen.
Eller et annet sted, senere.»

«Poenget er ikke hvor den kjører.»

«Poenget er at den kan flyttes.»

(Knytt tydelig tilbake til historien.)

«I historien var det akkurat dette som skjedde.»

«Når prosessen først var tydelig –
da ble plattformen et valg, ikke et krav.»

«Plattformen ble noe de brukte,
ikke noe de gjømte seg bak.»

(Viktig presisering – tydelig, moden.)

«Og dette er viktig:»

(pause)

«Dette handler ikke om å være imot plattformer.»

«Plattformer er bra.
Ofte helt nødvendige.»

«Men de er sjelden det riktige stedet å starte
når problemet fortsatt er lite, uklart –
og i konstant endring.»

(Ny formulering – noe publikum kan ta bilde av.)

«Plattformer skalerer løsninger.»

(kort pause)

«Prosesser skaper forståelse.»

(La den setningen lande.)

«Når vi starter med prosessen:»

«blir eierskapet tydelig»

«blir kompleksiteten synlig»

«blir arkitekturen et resultat – ikke et premiss»

(Rolig overgang videre.)

«Og det er her lette rammeverk og åpne formater
faktisk begynner å gi mening.»

«Ikke som mål i seg selv –
men som muliggjørere.»

(Tempo ned. Klar for neste del.)

«Så la oss se litt nærmere på
hvordan dette kan se ut i praksis.»

## Del 5: Eksempelet (den lille prosessen)

Tidsbruk: ca. 4–5 minutter

(Nå kan energien gå litt opp, men hold det rolig.)

### 1. Overgangen inn i demoen (manus)

«La oss gjøre dette helt konkret.»

«Ikke med et stort system.
Ikke med et diagram.»

«Men med en liten prosess.»

(kort pause)

«Dette er den typen kode dataingeniøren i historien skrev.»

### 2. Hva demoen skal illustrere (tydelig mål)

Demoen skal vise fire ting, og kun disse:

- Prosessen er liten og forståelig
- Den kan kjøres lokalt
- Den er ikke bundet til en plattform
- Den produserer et reelt, varig resultat

### 3. Demo-oppsett

Problem (samme som historien)

- Input: CSV
- En enkel transformasjon
- Output: analyseklar data (Delta)

Teknologi

- Python
- DuckDB
- Delta Lake (via delta-rs eller parquet + metadata)
- Ikke Spark. Ikke cluster. Ikke cloud.

4. Demo – steg for steg (manus + handling)

Steg 1 – Vis filen

(Åpne CSV i editor eller terminal)

«Dette er input.
Akkurat som i historien.»

«Tolv megabyte.
Ingen magi.»

Steg 2 – Vis koden

(Vis én fil, f.eks. process.py – maks 40–50 linjer)

Ikke les koden. Pek.

«Dette er hele prosessen.»

«Den gjør én ting.
Den gjør det tydelig.»

Her kan du peke på:

- lesing
- transformasjon
- skriving

Steg 3 – Kjør lokalt
python process.py input.csv output/

«Ingen deploy.
Ingen miljøvalg.»

«Bare kode.»

(La kommandoen fullføre.)

Steg 4 – Vis resultatet

åpne output (parquet / delta)

evt. kjør én enkel DuckDB-spørring

«Dette er resultatet.»

«Det er ikke midlertidig.
Det er ikke skjult.»

«Det kan brukes videre –
av analyse, av KI, eller av neste prosess.»

5. Knyt demoen eksplisitt til poenget

(Dette er viktigere enn selve kjøringen.)

«Poenget er ikke at dette er fancy.»

«Poenget er at dette er flyttbart.»

«Den samme prosessen kan:»

- «kjøres i CI»
- «pakkes i en container»
- «kjøres i Kubernetes»
- «eller kjøres på en plattform – senere»
- «Plattformen er ikke borte.»

«Den er bare ikke et krav for å komme i gang.»

7. Ha:

- én ferdig kjørt output-mappe
- én skjermdump av resultatet
- evt. en kort video du kan spille

Men: si aldri at du har det. Bare vit det.

8. Overgangen videre (manus)

(Etter demoen, rolig.)

«Dette er Data Engineering as Code for meg.»

«Små, kjørbare prosesser.
Med tydelig eierskap.»

«Og når vi jobber slik,
skjer det noen interessante ting.»

(Perfekt inngang til Del 6: Hvorfor dette faktisk er bedre.)

## Del 6: Konsekvensene (Hvorfor dette faktisk er bedre)

Tidsbruk: ca. 3–4 minutter

(Tempo rolig. Dette er modningsdelen.)

«Når vi begynner med prosessen i stedet for plattformen,
skjer det noe interessant.»

(kort pause)

«Ikke bare teknisk.
Men organisatorisk.»

1. Eierskap blir tydelig

«Når en prosess er liten og kjørbar,
er det også tydelig hvem som eier den.»

«Det er ikke lenger systemet som feiler.»

(kort pause)

«Det er kode.
Og kode kan eies.»

«Plutselig kan noen faktisk si:
Det er koden min.»

2. Kompleksitet blir synlig – tidligere

«Kompleksitet forsvinner ikke.»

«Men når vi starter med prosessen,
ser vi den tidligere.»

«Vi ser:
– hva som er enkelt
– hva som er vanskelig
– og hva som bare ser vanskelig ut fordi det er pakket inn»

«Arkitekturen blir et resultat av behov,
ikke en antagelse om fremtid.»

3. Plattformen blir et valg – ikke et krav

«Når prosessen er flyttbar,
kan vi ta plattformvalget når vi faktisk trenger det.»

«Ikke for tidlig.
Ikke for sent.»

«Da bruker vi plattformer til det de er best på:»

«skalering»

«stabil drift»

«deling og gjenbruk»

«Ikke som et startpunkt.
Men som en forsterker.»

4. Lavere kognitiv last – høyere tempo

«Små prosesser er lettere å forstå.»

«De kan leses på fem minutter.»

«De kan endres på én dag, ikke tre sprinter.»

«Det gjør noe med tempo.»

«Ikke fordi vi løper fortere,
men fordi vi stopper å løpe i feil retning.»

5. Et bedre fundament for analyse og KI

(Knytt tydelig til salens tema.)

«Og dette er spesielt viktig
når vi snakker om analyse og KI.»

«Modeller bryr seg ikke om plattformer.»

(liten pause)

«De bryr seg om data.»

«Når dataene er:»

«tydelig transformert»

«reproduserbare»

«forståelige»

«da blir de også enklere å bruke videre –
enten det er til analyse, feature engineering eller KI.»

6. Viktig presisering (igjen)

(Rolig, tydelig.)

«Dette er ikke en oppskrift.»

«Og det er ikke en erstatning for det dere allerede har.»

«Det er en retning.»

«Et annet sted å starte.»

Avrunding – bro til avslutning

«Små prosesser.
Kjørbar kode.
Tydelig eierskap.»

(kort pause)

«Data engineering på lavgir.»

(liten pause)

«Men med full kontroll.»

## Avslutningen: Retningen videre

Tidsbruk: ca. 1–1,5 minutter

(Tempo ned. Dette er siste bilde publikum sitter igjen med.)

«Så… hva gjør vi med dette?»

(kort pause)

«Ikke i morgen.
Ikke på neste roadmap.»

«Men i neste lille oppgave.»

«Neste gang noen sier:
‘Det er bare en liten jobb’»

(liten pause)

«…så kan vi stille ett spørsmål først.»

(Tydelig, langsomt.)

«Hva er den minste prosessen som faktisk løser dette –
og som vi kan eie?»

«Ikke hvilken plattform.
Ikke hvilken standard.»

«Men hvilken kode.»

«Hvis vi starter der,
kan resten komme etter.»

(Knytt eksplisitt tilbake til starten.)

«Teamet i historien kastet ikke plattformen.»

«De sluttet bare å starte der.»

(Avsluttende linje – samme som i programteksten.)

«Data engineering på lavgir.»

(pause)

«Men med full kontroll.»

(Oppdatert slutt-tidsbilde som blir stående som folk kan ta bilde av)
