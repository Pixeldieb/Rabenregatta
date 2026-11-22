# Issue-Tracker: GitHub

Tickets und Pull Requests dieses Repos liegen auf GitHub unter `github.com/Pixeldieb/Rabenregatta`. Werkzeug ist `gh` (Konto `Pixeldieb`).
`gh` nimmt das Repo aus `git remote -v`; außerhalb des Checkouts `-R Pixeldieb/Rabenregatta` angeben.

## Befehle

- **Ticket anlegen:** Text in eine Datei im Scratchpad, dann `gh issue create --title "Titel" --label needs-triage --body-file datei`.
- **Ticket lesen:** `gh issue view N`, mit Kommentaren `gh issue view N --comments` (nur wenn nötig).
- **Tickets auflisten:** `gh issue list --state open --label ready-for-agent`.
- **Kommentieren:** `gh issue comment N --body-file datei`.
- **Labels:** `gh issue edit N --add-label ready-for-agent --remove-label needs-triage`.
- **Zuweisen:** `gh issue edit N --add-assignee @me`.
- **Schließen:** erst Begründung mit `gh issue comment`, dann `gh issue close N`. Oder `Closes #N` im PR.
- **Pull Requests:** `gh pr create --title "Titel" --body-file datei`, `gh pr view N`, `gh pr diff N`. Mergen macht RB.
- **Sprache:** Tickets und PR-Texte auf Deutsch.

Nur in RBs eigenes Repo schreiben, nie in `mattpocock/skills` oder ein Upstream-Repo.

## Pull Requests als Eingang für Triage

**PRs als Eingang: nein.** _(Auf `ja` setzen, wenn fremde PRs wie Wünsche durch die Triage laufen sollen; `/triage` liest das.)_

## Wenn ein Skill „im Issue-Tracker veröffentlichen“ sagt

GitHub-Ticket mit `gh issue create` anlegen.

## Wenn ein Skill „das passende Ticket holen“ sagt

`gh issue view N`. RB nennt meist Nummer oder Link.

## Blockieren

GitHub-Abhängigkeiten: `gh issue edit N --add-blocked-by B` (`gh` ab 2.94). Ältere `gh`:
`gh api --method POST repos/Pixeldieb/Rabenregatta/issues/N/dependencies/blocked_by -F issue_id=<id von B>`
(`gh api repos/Pixeldieb/Rabenregatta/issues/B --jq .id`). Offene Blocker zählen:
`gh api repos/Pixeldieb/Rabenregatta/issues/N --jq .issue_dependencies_summary.blocked_by` (0 heißt: frei).

## Wayfinding (für `/wayfinder`)

- **Karte:** ein Ticket mit Label `wayfinder:map`.
- **Kind-Ticket:** Unter-Ticket der Karte (`gh issue create --parent <Karte>`), Label `wayfinder:<typ>`
  (`research`/`prototype`/`grilling`/`task`). Fehlen die Labels, beim ersten Einsatz anlegen.
- **Nächstes Ticket:** offene Unter-Tickets der Karte ohne offenen Blocker und ohne Zuweisung; erstes in der Reihenfolge der Karte gewinnt.
- **Übernehmen:** `gh issue edit N --add-assignee @me`, als erste Schreibaktion der Sitzung.
- **Abschließen:** Antwort kommentieren, `gh issue close N`, dann in der Karte unter „Entscheidungen bisher“ einen Verweis ergänzen.
