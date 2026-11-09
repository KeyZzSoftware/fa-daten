# Finanzblatt – Anleitung für die automatische Ausgabe

Die Website „Financial Awareness“ lädt `finanzblatt.json` aus diesem Repo. Das Heft hat genau 4 Seiten:
- Seite 1–2: aktuelle, wichtige Wirtschafts- und Börsennachrichten (höchstens 9 Meldungen, Seite 1 zeigt die ersten 4)
- Seite 3–4: ein Aufklärungsthema (kluge, legale Steuertipps, Geld, Vorsorge, Immobilien …), nur bei der 0-Uhr-Ausgabe neu

## Ablauf je Lauf (Zeiten Europe/Berlin)
- **0 Uhr:** Falls `finanzblatt.json` existiert und ein älteres `datum` hat: nach `archiv/<datum>.json` verschieben und in `archiv` eintragen. Neue Ausgabe anlegen: `nr` + 1, neues `datum`, neue Nachrichten, neues Thema.
- **3, 6, 9, 12, 15, 18, 21 Uhr:** Nur `news`, `stand`, `naechstes` aktualisieren. Neue wichtige Meldungen ergänzen, veraltete oder unwichtige streichen. Thema bleibt.

## Nachrichten finden
1. Schlagzeilen bei CNBC (Markets, Economy, Earnings) und Wall Street Journal (Markets, Economy) lesen.
2. Hinter jede wichtige Schlagzeile tiefer schauen: Artikel lesen, wo frei zugänglich; bei Bezahlschranke (WSJ) nie umgehen, sondern denselben Vorgang in frei zugänglichen Quellen (CNBC, Reuters, AP, Unternehmensmeldungen) prüfen.
3. `kurse.json` lesen: Jede Aktie mit Tagesbewegung von mindestens ±4 % (Indizes ±1,5 %) bekommt eine eigene Meldung mit `aktie` und `warum` (der belegte Grund für die Bewegung).
4. Nur belegte Fakten. Keine Kursprognosen, keine Kauf- oder Verkaufsempfehlungen.

## Schreiben
- Deutsch, einfach, kurz. Eigene Worte, nie Sätze aus Quellen übernehmen.
- `titel` höchstens 70 Zeichen. `text` höchstens 230 Zeichen (Hauptmeldung bis 300). `warum` höchstens 160 Zeichen.
- `wichtig`: 3 = Top-Thema (marktbewegend), 2 = wichtig, 1 = Randnotiz. Sortierung auf der Seite: wichtig, dann neueste – so steht oben links immer das Neueste und Wichtigste.
- `zeit`: Zeitpunkt des Ereignisses (ISO 8601 mit Zeitzone).
- Thema (Seite 3–4): je Seite 3–4 Absätze `[Kurztitel, Text]` mit höchstens 220 Zeichen, plus `merke`. Optional `fach` mit denselben Feldern für Fachleser (Paragrafen, Formeln). Rechtsstand prüfen, Quellen angeben. Themen nicht wiederholen (siehe `archiv`).

## Format `finanzblatt.json`
```json
{
  "nr": 2,
  "datum": "2026-11-10",
  "stand": "2026-11-10T06:04:00+01:00",
  "naechstes": "2026-11-10T09:00:00+01:00",
  "news": [
    { "zeit": "2026-11-10T05:30:00+01:00", "wichtig": 3, "titel": "…", "text": "…",
      "aktie": { "n": "NVIDIA", "d": -4.2 }, "warum": "…", "ort": "USA",
      "quellen": [["CNBC", "https://www.cnbc.com/…"], ["WSJ", "https://www.wsj.com/…"]] }
  ],
  "thema": {
    "titel": "…", "unter": "…", "rubrik": "Steuern", "bereich": "steuern",
    "seiten": [ { "h": "", "absaetze": [["…", "…"]], "merke": "…" }, { "h": "…", "absaetze": [["…", "…"]], "merke": "…" } ],
    "fach":   [ { "h": "", "absaetze": [["…", "…"]], "merke": "…" }, { "h": "…", "absaetze": [["…", "…"]] } ],
    "quellen": [["Titel", "https://…"]]
  },
  "archiv": [ { "datum": "2026-11-09", "nr": 1, "titel": "…", "bereich": "steuern", "datei": "2026-11-09.json" } ]
}
```
`bereich` ist einer von: geld, anlegen, rente, versich, steuern, immo, alltag, wirtschaft.
`aktie`, `warum`, `ort`, `fach` sind optional.

## Prüfen vor dem Speichern
- JSON gültig (`python3 -m json.tool finanzblatt.json`).
- Alle Links beginnen mit https://.
- Commit-Nachricht: „Finanzblatt <datum> <uhrzeit>“, dann pushen.
