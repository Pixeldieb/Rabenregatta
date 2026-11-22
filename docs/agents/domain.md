# Fachdoku (Domain Docs)

Wie die Skills die Fachdoku dieses Repos lesen und pflegen. Aufbau: **ein Kontext** (single-context).

## Vor dem Erkunden lesen

- **`GLOSSARY.md`** im Repo-Wurzelverzeichnis: Glossar der Fachbegriffe.
- **`docs/adr/`**: Entscheidungen (ADRs) zum Bereich lesen, an dem gearbeitet wird. Neue ADRs als
  `docs/adr/NNNN-kurztitel.md`. Nummer vorher auf `origin/main` nachsehen, parallele Sitzungen vergeben ebenfalls Nummern.

Fehlt eine dieser Dateien, **ohne Hinweis weitermachen**. Nicht vorab anlegen. Der Skill `domain-modeling` legt sie an,
sobald ein Begriff oder eine Entscheidung tatsächlich geklärt ist.

## Aufbau

```
/
├── GLOSSARY.md
└── docs/adr/
    ├── 0001-erste-entscheidung.md
    └── …
```

Sprache der Fachdoku: Deutsch.

## Begriffe aus dem Glossar verwenden

Wo eine Ausgabe einen Fachbegriff nennt (Ticket-Titel, Vorschlag, Hypothese, Testname), den Begriff aus `GLOSSARY.md`
nehmen, keine Synonyme, die das Glossar ausdrücklich meidet. Fehlt ein Begriff, ist das ein Signal: entweder eine Sprache
erfinden, die das Projekt nicht spricht (überdenken), oder eine echte Lücke (für `domain-modeling` notieren).

## Widersprüche zu Entscheidungen offenlegen

Widerspricht eine Ausgabe einer bestehenden Entscheidung, das ausdrücklich sagen statt still darüber hinwegzugehen:

> _Widerspricht ADR-0007 (…), sollte aber neu aufgerollt werden, weil …_
