# FaireWelt Hilfeinfos

Hilfetelefone, Seelsorgen und Beratungsstellen für **Deutschland, Österreich und die Schweiz** – übersichtlich auf einer Seite, zusammengestellt von [FaireWelt auf Twitch](https://www.twitch.tv/fairewelt).

## Aufbau

```
├── index.html        Die Hilfeseite (komplett eigenständig, keine Abhängigkeiten)
├── impressum.html    Impressum & Nutzungsfreigaben
├── .nojekyll         Verhindert Jekyll-Verarbeitung auf GitHub Pages
└── werkzeug/         Generator zum Pflegen der Seite (optional)
    ├── data.py           Themen & Nummern, Teil 1 (Notfall bis Vielfalt)
    ├── data2.py          Themen & Nummern, Teil 2 (Gesundheit bis weitere Rufnummern)
    ├── build.py          Baut index.html
    ├── build_impressum.py Baut impressum.html
    ├── qr_gen.py         Erzeugt & verifiziert die QR-Codes aller Nummern
    ├── qr_map.json       Vorberechnete QR-Codes
    └── *_b64.txt         Eingebettete Bilder (Logo, Banner, Handzeichen, Favicon)
```

Die beiden HTML-Dateien sind **vollständig eigenständig**: Alle Bilder und QR-Codes
sind eingebettet, es gibt kein CSS-/JS-Gerüst und keine Bibliotheken. Nur die
Schriften (Manrope, Atkinson Hyperlegible) werden von Google Fonts geladen –
fällt das aus, greifen Systemschriften.

## Veröffentlichen mit GitHub Pages

1. Dieses Repository zu GitHub hochladen (Branch `main`).
2. **Settings → Pages → Source:** „Deploy from a branch“, Branch `main`, Ordner `/ (root)`.
3. Nach etwa einer Minute ist die Seite unter `https://BENUTZERNAME.github.io/REPONAME/` erreichbar.

Jeder andere statische Host (Netlify, Cloudflare Pages, eigener Webspace) funktioniert genauso –
einfach `index.html`, `impressum.html` und `.nojekyll` hochladen.

## Funktionen

- **Handy:** Jede Nummer ist ein Anruf-Knopf (`tel:`-Link) – ein Tipper wählt direkt.
  Unten klebt eine Schnellwahl-Leiste mit Notruf 112, Polizei und Wegbegleitung,
  die sich dem gewählten Land anpasst.
- **PC:** Ein Klick auf eine Nummer öffnet einen QR-Code. Mit der Handykamera
  gescannt, öffnet sich der Anruf direkt im Wählprogramm. Alternativ: Nummer
  kopieren oder – falls ein Anrufprogramm eingerichtet ist – direkt am PC anrufen.
- **Länderfilter** (Alle / DE / AT / CH), **Live-Suche**, **Themen-Sprungliste**,
  Themenübersicht, Druckansicht (klappt automatisch alles auf), Barrierefreiheit
  (gut lesbare Schrift, große Tippflächen, Tastaturbedienung).

## Geschützte Namensanzeige (Impressum)

Der bürgerliche Name liegt **AES-256-verschlüsselt** in `impressum.html` und ist ohne
Passwort auch im Quelltext nicht lesbar. Geprüfte Stellen erhalten das Passwort auf
Anfrage und können den Namen dann direkt auf der Seite freischalten.

Name oder Passwort ändern:

```bash
cd werkzeug
python3 name_verschluesseln.py "Vor- und Nachname" "NeuesSicheresPasswort"
python3 build_impressum.py
```

Wichtig: Ein starkes Passwort verwenden (Wortkette + Zahlen) – die Sicherheit der
Verschlüsselung steht und fällt damit. Die Berechtigung anfragender Stellen wird
**persönlich** geprüft (z. B. Rückruf über die offizielle Amtsnummer), bevor das
Passwort vergeben wird – eine automatische „Behörden-Erkennung“ gibt es im Web nicht.

## Eigene Domain einrichten (z. B. sos-dach.info)

Damit in der Adresszeile `sos-dach.info` statt `fairewelt.github.io/sos-dach`
steht, sind drei Schritte nötig – die Datei dafür liegt schon bereit:

1. **Domain registrieren** (falls noch nicht geschehen), z. B. bei IONOS,
   Namecheap, INWX oder Cloudflare Registrar. Das kann nur der jeweilige
   Anbieter erledigen, nicht GitHub.

2. **DNS-Einträge beim Domain-Anbieter setzen** (im dortigen DNS-Verwaltungsbereich):

   | Typ | Name | Ziel |
   |---|---|---|
   | A | @ (oder leer) | `185.199.108.153` |
   | A | @ (oder leer) | `185.199.109.153` |
   | A | @ (oder leer) | `185.199.110.153` |
   | A | @ (oder leer) | `185.199.111.153` |
   | CNAME | www | `fairewelt.github.io` |

   (Die vier A-Einträge sind die offiziellen GitHub-Pages-Server; steht
   `www.sos-dach.info` nicht zur Verfügung, kann der CNAME-Eintrag entfallen.)

3. **Domain in GitHub hinterlegen:** Die Datei `CNAME` (ohne Dateiendung, im
   Root des Repos, liegt bereits bei) enthält `sos-dach.info`. Danach im
   Repository unter **Settings → Pages → Custom domain** ebenfalls
   `sos-dach.info` eintragen und speichern. GitHub prüft die DNS-Einträge
   automatisch (kann bis zu 24 Stunden dauern) und bietet danach den Schalter
   **„Enforce HTTPS"** an – den unbedingt aktivieren, damit die Verbindung
   verschlüsselt ist (wichtig bei einer Hilfeseite!).

Bis die DNS-Änderung überall verbreitet ist, bleibt `fairewelt.github.io/sos-dach`
parallel erreichbar – nichts geht kaputt, es kommt nur eine zweite Adresse hinzu.

## Nummern ändern oder ergänzen

1. In `werkzeug/data.py` bzw. `werkzeug/data2.py` den Eintrag anpassen
   (Format ist selbsterklärend, `E(Name, [(Anzeige, Wählnummer)], Beschreibung, Web, Instagram)`).
2. Neu bauen:

   ```bash
   cd werkzeug
   python3 qr_gen.py          # nur nötig, wenn Nummern geändert wurden
   python3 build.py
   python3 build_impressum.py
   ```

   `qr_gen.py` benötigt einmalig `opencv-python` und `numpy`
   (`pip install opencv-python numpy`) – die fertigen Seiten selbst brauchen nichts.
   Jeder erzeugte QR-Code wird dabei automatisch rückwärts dekodiert und geprüft.

3. `index.html` / `impressum.html` einchecken – fertig.

## Hinweis

Alle Angaben ohne Gewähr. Nummern und Angebote können sich ändern –
im Zweifel bitte auf der jeweils verlinkten Website nachsehen.
