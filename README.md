Foredrag for Rubiks 2026

Dette repoet inneholder presentasjonen "Data Engineering as Code" utarbeidet for Sopra Steria Rubiks-konferansen den 7. februar 2026.

## Struktur

### [`/docs`](./docs/README.md)
Inneholder presentasjonsmaterialer inkludert:
- Presentasjonsslider og komposisjon
- Talenotater
- Detaljerte beskrivelser av presentasjonsinnhold

### [`/src`](./src/README.md)
Inneholder live demonstrasjonskode som blir kjørt under presentasjonen, og viser praktiske eksempler på "Data Engineering as Code"-konsepter i praksis.

## Kommandoer (Justfile)

Hvis du har `just` installert kan du kjøre vanlige oppgaver fra `src/`:

```bash
cd src
just process
just query
just process-query
just test
just demo
just container-build
just container-run
just container-run-custom
just container-query
```
