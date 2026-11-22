# Triage-Labels

Die Skills sprechen von fünf Status-Rollen. Dieses Repo nutzt Matts Standardnamen.

| Rolle in mattpocock-skills | Label bei uns     | Bedeutung                                                     |
| -------------------------- | ----------------- | ------------------------------------------------------------- |
| `needs-triage`             | `needs-triage`    | RB muss es einordnen                                          |
| `needs-info`               | `needs-info`      | Wartet auf Angaben der meldenden Person                       |
| `ready-for-agent`          | `ready-for-agent` | Vollständig beschrieben, eine Claude-Sitzung kann es umsetzen |
| `ready-for-human`          | `ready-for-human` | Ein Mensch muss handeln (siehe unten)                         |
| `wontfix`                  | `wontfix`         | Wird nicht umgesetzt                                          |

## `ready-for-human`

Setzen, wenn RB oder andere Menschen selbst entscheiden, liefern (Fotos, Dateien), vor Ort handeln (Gerät, Messung),
in externen Systemen handeln oder Dritte einbinden müssen. Muss RB nur eine Claude-Sitzung anstoßen, gilt `ready-for-agent`.

Das Ticket sagt, **warum** es nicht an einen Agenten gehen kann, und bekommt einen Kommentar „Prompt für die nächste
Sitzung“ mit einem Start-Prompt im Codeblock. Wiederkehrende Schritte, die nur ein Mensch ausführen kann, als Skript
mit dem Skill `wizard` beilegen.
