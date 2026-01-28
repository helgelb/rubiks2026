# Del 3 – Fortellingen: “Tolv megabyte”

Det kom en fil en tirsdag. Tolv megabyte, komprimert. En CSV.  
I e-posten stod det: “Kan dere bare gjøre disse dataene tilgjengelige for analyse?”

Den første uken var møterommet fullt.  
Teamleder, arkitekt, sikkerhet, plattformutvikler.  
Dataingeniøren satt litt lenger ned langs bordet. Han hadde åpnet fila – og lukket den igjen da møtet startet.

Arkitekturtegningen vokste fort.  
Bokser, piler, standarder. Noen foreslo streaming, noen batch. Arkitekten foreslo begge deler.  
Plattformutvikleren snakket om drift. Sikkerhet om tilgang.

“Vi må gjøre dette riktig”, sa arkitekten.  
“Vi må bruke plattformen.”

Plattformen var et trygt ord. Det betydde at alle hadde bidratt, og at ingen måtte forklare for mye.

Uke to var filen borte.  
Den var blitt til et datasett, så en strøm, så et mellomlager.  
Ingen åpnet den lenger.  
Koden lå i et repo nesten ingen hadde klonet.  
Jobben kjørte i et miljø de færreste hadde tilgang til.

Når noe feilet, samlet de seg igjen.

“Det er nok noe med infrastrukturen.”  
“Det er sikkert rettigheter.”  
“Det må være skjemaet.”

Ingen sa: “Det er koden min.”

Så kom spørsmålet fra forretning, dagen før styringsmøtet:  
“Når kan vi få tallene?”

Og da gikk det opp for dem at ingen egentlig hadde sett på selve dataene siden den første tirsdagen.

Etter hvert ble det vanskelig å svare på enkle spørsmål:  
Hvor lang tid tar det å endre én kolonne?  
Hvem eier jobben?  
Kan vi teste dette lokalt?

En kveld, etter at de andre hadde gått, åpnet han fila igjen.  
Den var fortsatt tolv megabyte. Kolonnene var de samme.  
Innholdet var ikke blitt mer komplisert – bare veien dit.

Han skrev litt kode. Bare nok til å lese fila, gjøre det ene de faktisk trengte, og skrive resultatet ut igjen.  
Han kjørte det lokalt. Input. Kode. Output. Alt synlig.

Neste dag viste han det frem.

“Hvor kjører den?” spurte teamlederen.  
“Der det passer,” svarte han.

“På hvilken plattform?” spurte arkitekten.  
“På nesten hvilken som helst.”

Plattformutvikleren så opp.  
“Men vi har jo en plattform?”

Han nikket. Plattformen var fin. Robust. Viktig.  
Men dette var ikke bundet til den.

Det var bare en prosess.  
Kode som kunne kjøres lokalt, i CI, i skyen – eller et annet sted senere.  
Den kunne flyttes uten å skrives om.

De kjørte koden sammen.  
For første gang på lenge visste alle hva som faktisk skjedde:  
hvor dataene kom fra, hva som ble endret, og hvor de endte.

Plattformen forsvant ikke.  
Den sluttet bare å være startpunktet.

Filen er borte nå. Løst, levert, arkivert.  
Men noe ble igjen.

Når nye oppgaver kommer inn, spør de ikke først hvor dette skal kjøre.  
De spør: hva er det som faktisk må skje?  
Og noen ganger, før de åpner møtekalenderen, åpner de dataene.

---

[← Forrige: Del 2 – Kort om meg](del-2-kort-om-meg.md) | [Neste: Del 4 – Broen](del-4-broen.md)

[Til hovedoversikt](komposisjon.md)
