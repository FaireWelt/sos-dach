# -*- coding: utf-8 -*-
"""Impressum der FaireWelt Hilfeinfos – gleiches Design wie die Hauptseite."""
import json
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
AUSGABE = HIER.parent if HIER.name == "werkzeug" else HIER

LOGO = (HIER / 'logo_b64.txt').read_text().strip()
FAV  = (HIER / 'favicon_b64.txt').read_text().strip()
QR_ALLE = json.loads((HIER / 'qr_map.json').read_text())
QRDATEN = json.dumps({"+4917682547714": QR_ALLE["+4917682547714"]}, separators=(",", ":"))
NAMEDATEN = (HIER / 'name_geschuetzt.json').read_text().strip()

STREAMER = ["fairewelt","eligreedy","johnny_weasel","der_cptn","slayertheunkind",
            "bela_dbt","tobias_huch","streaven","tentapill","JaneWhooo","500IQerror"]

chips = "\n".join(
    f'      <a class="streamer-chip{" haupt" if s == "fairewelt" else ""}" '
    f'href="https://www.twitch.tv/{s}" target="_blank" rel="noopener">{s}</a>'
    for s in STREAMER)

page = f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#3e2a78">
<title>Impressum – FaireWelt Hilfeinfos</title>
<meta name="robots" content="noindex">
<link rel="icon" type="image/png" href="data:image/png;base64,{FAV}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
:root{{
  --papier:#f6f5f2; --karte:#ffffff; --tinte:#221c33; --nebel:#5f5a70;
  --violett:#4b3591; --violett-tief:#3e2a78; --violett-hell:#efeaf9;
  --linie:#e4e1da; --linie-stark:#cfcbc2;
  --rund:14px; --rund-klein:10px;
  --schatten:0 1px 3px rgba(34,28,51,.08),0 4px 16px rgba(34,28,51,.06);
  --display:"Manrope","Segoe UI",system-ui,sans-serif;
  --text:"Atkinson Hyperlegible","Segoe UI",system-ui,sans-serif;
}}
*{{box-sizing:border-box}}
body{{
  margin:0;background:var(--papier);color:var(--tinte);
  font-family:var(--text);font-size:17px;line-height:1.55;
  -webkit-tap-highlight-color:rgba(75,53,145,.15);
}}
a{{color:var(--violett)}}
a:focus-visible,button:focus-visible{{outline:3px solid var(--violett);outline-offset:2px;border-radius:6px}}
.ic{{width:1.1em;height:1.1em;flex:none;vertical-align:-.16em}}
.kopf{{background:var(--karte);border-bottom:1px solid var(--linie)}}
.kopf-innen{{max-width:900px;margin:0 auto;padding:26px 20px 22px;display:flex;gap:18px;align-items:center;flex-wrap:wrap}}
.kopf img{{width:64px;height:64px;border-radius:50%;flex:none;box-shadow:var(--schatten)}}
.kopf h1{{font-family:var(--display);font-weight:800;font-size:clamp(1.4rem,3.4vw,1.9rem);margin:0;letter-spacing:-.01em}}
.kopf h1 .fw{{color:var(--violett)}}
.zurueck{{display:inline-block;margin-top:4px;font-weight:700;text-decoration:none}}
.zurueck:hover{{text-decoration:underline}}
main{{max-width:900px;margin:0 auto;padding:14px 20px 60px}}
.karte{{
  background:var(--karte);border:1px solid var(--linie);border-radius:var(--rund);
  padding:20px 22px;margin:16px 0;box-shadow:var(--schatten);
}}
.karte h2{{font-family:var(--display);font-weight:800;font-size:1.2rem;margin:0 0 10px;color:var(--violett-tief)}}
.streamer-chips{{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}}
.streamer-chip{{
  text-decoration:none;color:var(--tinte);background:var(--papier);border:1.5px solid var(--linie-stark);
  border-radius:999px;padding:8px 16px;font-size:.95rem;font-weight:700;min-height:40px;
  display:inline-flex;align-items:center;
}}
.streamer-chip:hover{{border-color:var(--violett);color:var(--violett);background:var(--violett-hell)}}
.streamer-chip.haupt{{border-color:var(--violett);color:#fff;background:var(--violett)}}
.anfrage{{
  margin-top:14px;background:var(--violett-hell);border:1px solid #d8cdf0;
  border-radius:var(--rund-klein);padding:12px 16px;
}}
address{{font-style:normal;line-height:1.7}}
.kontakt-knoepfe{{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px}}
.kontakt-knopf{{
  display:inline-flex;align-items:center;gap:8px;text-decoration:none;
  font-family:var(--display);font-weight:800;font-size:.98rem;
  background:var(--violett);color:#fff;border-radius:9px;padding:10px 17px;min-height:44px;
}}
.kontakt-knopf:hover{{background:var(--violett-tief)}}
.kontakt-knopf.sekundaer{{background:var(--karte);color:var(--violett);border:1.5px solid var(--violett)}}
.kontakt-knopf.sekundaer:hover{{background:var(--violett-hell)}}
.hinweis{{color:var(--nebel);font-size:.92rem}}
.weg{{
  background:var(--papier);border:1px solid var(--linie);border-radius:var(--rund-klein);
  padding:14px 16px;margin:12px 0;
}}
.weg-titel{{font-family:var(--display);font-weight:800;margin:0 0 6px;color:var(--violett-tief)}}
.vorgangsnummer{{
  display:inline-block;font-family:var(--display);font-weight:800;letter-spacing:.02em;
  background:var(--violett-hell);border:1px solid #d8cdf0;border-radius:8px;
  padding:2px 10px;white-space:nowrap;
}}
.freischalten{{display:flex;flex-wrap:wrap;gap:10px;margin:10px 0 4px}}
.freischalten input{{
  flex:1 1 220px;min-width:180px;padding:10px 14px;border-radius:9px;
  border:1.5px solid var(--linie-stark);background:var(--karte);color:var(--tinte);
  font:inherit;font-size:1rem;
}}
.freischalten .kontakt-knopf{{border:none;cursor:pointer;font:inherit;font-family:var(--display);font-weight:800}}
.fs-ergebnis{{font-family:var(--display);font-weight:800;font-size:1.05rem;margin:.4em 0 0;min-height:1.3em}}
.fs-ergebnis.ok{{color:#1d7a3e}}
.fs-ergebnis.fehler{{color:#b3453f}}
footer{{border-top:1px solid var(--linie);background:var(--karte)}}
.fuss-innen{{max-width:900px;margin:0 auto;padding:24px 20px;display:flex;flex-wrap:wrap;gap:14px 30px}}
.fuss-innen a{{color:var(--tinte);text-decoration:none}}
.fuss-innen a:hover{{color:var(--violett);text-decoration:underline}}

/* QR-Dialog (PC → Handy) */
#qrDialog{{
  border:none;border-radius:var(--rund);padding:22px 24px;max-width:340px;width:calc(100vw - 40px);
  box-shadow:0 12px 48px rgba(34,28,51,.35);color:var(--tinte);font-family:var(--text);
}}
#qrDialog::backdrop{{background:rgba(34,28,51,.55);backdrop-filter:blur(3px)}}
.qr-kopf{{display:flex;align-items:flex-start;gap:12px}}
.qr-kopf h2{{font-family:var(--display);font-weight:800;font-size:1.12rem;margin:0;flex:1}}
.qr-schliessen{{
  flex:none;width:34px;height:34px;border-radius:8px;border:1.5px solid var(--linie-stark);
  background:var(--karte);color:var(--nebel);font-size:1rem;cursor:pointer;
}}
.qr-schliessen:hover{{color:var(--tinte);border-color:var(--tinte)}}
.qr-anleitung{{color:var(--nebel);font-size:.93rem;margin:.5em 0 .9em}}
.qr-code{{display:flex;justify-content:center}}
.qr-code svg{{width:210px;height:210px;border:1px solid var(--linie);border-radius:10px}}
.qr-nummer{{text-align:center;font-family:var(--display);font-weight:800;font-size:1.15rem;margin:.7em 0;user-select:all}}
.qr-aktionen{{display:flex;gap:10px}}
.qr-knopf{{
  flex:1;display:inline-flex;justify-content:center;align-items:center;text-align:center;
  font-family:var(--display);font-weight:800;font-size:.95rem;text-decoration:none;
  background:var(--violett);color:#fff;border:none;border-radius:9px;padding:11px 10px;
  min-height:44px;cursor:pointer;
}}
.qr-knopf:hover{{background:var(--violett-tief)}}
.qr-sekundaer{{background:var(--karte);color:var(--violett);border:1.5px solid var(--violett)}}
.qr-sekundaer:hover{{background:var(--violett-hell)}}
.qr-hinweis{{color:var(--nebel);font-size:.8rem;margin:.9em 0 0}}
@media print{{
  body{{background:#fff;color:#000}}
  .karte{{box-shadow:none}}
  #qrDialog{{display:none!important}}
  a,.streamer-chip,.kontakt-knopf{{color:#000!important;background:none!important}}
}}
</style>
</head>
<body>

<header class="kopf">
  <div class="kopf-innen">
    <img src="data:image/webp;base64,{LOGO}" alt="" width="64" height="64">
    <div>
      <h1><span class="fw">FaireWelt</span> Hilfeinfos – Impressum</h1>
      <a class="zurueck" href="index.html">← Zurück zu den Hilfeinformationen</a>
    </div>
  </div>
</header>

<main>

<section class="karte">
  <h2>Nutzung in Streams &amp; Videos</h2>
  <p>Die unten aufgeführten Streamer dürfen diese Seite in ihren Streams und Videos verwenden – natürlich <strong>FaireWelt</strong> selbst, aber auch:</p>
  <div class="streamer-chips">
{chips}
  </div>
  <div class="anfrage">
    <strong>Du möchtest die Seite auch nutzen?</strong> Weitere Anfragen werden gerne gesehen – per E-Mail an
    <a href="mailto:fairewelt@mein.online-impressum.de">fairewelt@mein.online-impressum.de</a>
    oder über Discord an <strong>„fairewelt_07820“</strong>.
  </div>
</section>

<section class="karte">
  <h2>Impressum</h2>
  <p><strong>Angaben gemäß § 5 TMG</strong></p>
  <address>
    FaireWelt – Fynn Logan<br>
    c/o Online-Impressum.de #32596<br>
    Europaring 90<br>
    53757 Sankt Augustin
  </address>
  <div class="kontakt-knoepfe">
    <a class="kontakt-knopf" href="mailto:fairewelt@mein.online-impressum.de">E-Mail schreiben</a>
    <a class="kontakt-knopf" href="tel:+4917682547714">+49 176 82547714</a>
    <a class="kontakt-knopf sekundaer" href="https://www.mein.online-impressum.de/fairewelt/" target="_blank" rel="noopener">Zweiter Kontaktweg</a>
  </div>
  <p style="margin-top:16px"><strong>Zuständige Regulierungs- und Aufsichtsbehörde:</strong><br>
  Landesanstalt für Medien Nordrhein-Westfalen<br>
  Sitz: Deutschland</p>
</section>

<section class="karte" id="behoerden">
  <h2>Identitätsauskunft für Behörden, Gerichte &amp; Rechteinhaber</h2>
  <p>Dieses Angebot wird unter dem Künstlernamen <strong>Fynn Logan</strong> betrieben.
  Staatliche, städtische und juristische Stellen erhalten den bürgerlichen Namen
  des Betreibers auf zwei Wegen:</p>

  <div class="weg">
    <p class="weg-titel">Weg 1 – über den Impressum-Dienst (empfohlen)</p>
    <p>Richten Sie Ihre Anfrage unter Angabe der Vorgangsnummer
    <span class="vorgangsnummer">Online-Impressum.de&nbsp;#32596</span>
    an den Dienst <a href="https://www.mein.online-impressum.de/fairewelt/" target="_blank" rel="noopener">mein.online-impressum.de/fairewelt</a>.
    Der Dienst prüft die Berechtigung und legt die Identität gegenüber befugten Stellen offen.</p>
  </div>

  <div class="weg">
    <p class="weg-titel">Weg 2 – direkte Freischaltung auf dieser Seite</p>
    <p>Kontaktieren Sie den Betreiber über die oben genannten Kontaktwege (E-Mail oder Telefon)
    unter Angabe Ihrer Dienststelle und eines Rückrufwegs. Nach Prüfung der Anfrage erhalten
    Sie ein Freischalt-Passwort, mit dem Sie den bürgerlichen Namen direkt hier anzeigen können:</p>
    <div class="freischalten">
      <input type="password" id="fsPasswort" placeholder="Freischalt-Passwort" autocomplete="off" aria-label="Freischalt-Passwort eingeben">
      <button class="kontakt-knopf" id="fsKnopf">Namen anzeigen</button>
    </div>
    <p class="fs-ergebnis" id="fsErgebnis" role="status" aria-live="polite"></p>
    <p class="hinweis">Der Name ist auf dieser Seite nur verschlüsselt hinterlegt (AES-256) und
    ohne das Passwort auch im Quelltext nicht lesbar. Die Prüfung der Berechtigung erfolgt
    persönlich vor der Passwort-Vergabe.</p>
  </div>
</section>

<p class="hinweis">Alle Angaben ohne Gewähr auf Fehler und Funktion aufgrund von Änderungen.</p>

</main>

<dialog id="qrDialog" aria-labelledby="qrTitel">
  <div class="qr-kopf">
    <h2 id="qrTitel">Nummer aufs Handy übertragen</h2>
    <button class="qr-schliessen" id="qrZu" aria-label="Fenster schließen">✕</button>
  </div>
  <p class="qr-anleitung">Scanne den Code mit der Handykamera – der Anruf öffnet sich direkt im Wählprogramm.</p>
  <div class="qr-code" id="qrCode" role="img" aria-label="QR-Code mit der Telefonnummer"></div>
  <p class="qr-nummer" id="qrNummer"></p>
  <div class="qr-aktionen">
    <button class="qr-knopf" id="qrKopieren">Nummer kopieren</button>
    <a class="qr-knopf qr-sekundaer no-qr" id="qrAnrufen" href="#">Am PC anrufen</a>
  </div>
  <p class="qr-hinweis">„Am PC anrufen“ funktioniert, wenn ein Anrufprogramm eingerichtet ist – etwa eine Telefon-App, ein Softphone oder die Kopplung mit dem Handy.</p>
</dialog>

<footer>
  <div class="fuss-innen">
    <a href="index.html">Hilfeinformationen</a>
    <a href="https://www.twitch.tv/fairewelt" target="_blank" rel="noopener">FaireWelt auf Twitch</a>
    <a href="https://discord.gg/84crvbx9E4" target="_blank" rel="noopener">Discord-Server</a>
    <a href="https://www.youtube.com/@FaireWeltYT" target="_blank" rel="noopener">YouTube</a>
    <a href="https://linktr.ee/FaireWelt" target="_blank" rel="noopener">Linktree von Fynn</a>
  </div>
</footer>

<script>
(function(){{
  "use strict";
  var QR = __QRDATEN__;
  var istDesktop = window.matchMedia("(hover: hover) and (pointer: fine)").matches &&
                   !/Android|iPhone|iPad|iPod|Mobile|Windows Phone/i.test(navigator.userAgent);
  var qrDialog = document.getElementById("qrDialog");

  function qrAlsSvg(eintrag){{
    var n = eintrag.n, roh = atob(eintrag.d), felder = "";
    for (var y = 0; y < n; y++) {{
      for (var x = 0; x < n; x++) {{
        var i = y * n + x;
        if (roh.charCodeAt(i >> 3) & (128 >> (i & 7))) {{
          felder += '<rect x="' + (x + 2) + '" y="' + (y + 2) + '" width="1" height="1"/>';
        }}
      }}
    }}
    var kante = n + 4;
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + kante + ' ' + kante +
           '" shape-rendering="crispEdges"><rect width="' + kante + '" height="' + kante +
           '" fill="#ffffff"/><g fill="#221c33">' + felder + '</g></svg>';
  }}

  if (qrDialog && typeof qrDialog.showModal === "function") {{
    document.addEventListener("click", function(ev){{
      if (!istDesktop) return;
      var a = ev.target.closest ? ev.target.closest('a[href^="tel:"]') : null;
      if (!a || a.classList.contains("no-qr")) return;
      var tel = a.getAttribute("href").slice(4);
      var eintrag = QR[tel];
      if (!eintrag) return;
      ev.preventDefault();
      document.getElementById("qrCode").innerHTML = qrAlsSvg(eintrag);
      document.getElementById("qrNummer").textContent = tel;
      document.getElementById("qrAnrufen").setAttribute("href", "tel:" + tel);
      var kopieren = document.getElementById("qrKopieren");
      kopieren.textContent = "Nummer kopieren";
      kopieren.dataset.tel = tel;
      qrDialog.showModal();
    }});
    document.getElementById("qrZu").addEventListener("click", function(){{ qrDialog.close(); }});
    qrDialog.addEventListener("click", function(ev){{ if (ev.target === qrDialog) qrDialog.close(); }});
    document.getElementById("qrAnrufen").addEventListener("click", function(){{ qrDialog.close(); }});
    document.getElementById("qrKopieren").addEventListener("click", function(){{
      var knopf = this, tel = knopf.dataset.tel || "";
      function fertig(ok){{
        knopf.textContent = ok ? "Kopiert ✓" : "Kopieren fehlgeschlagen";
        setTimeout(function(){{ knopf.textContent = "Nummer kopieren"; }}, 1800);
      }}
      if (navigator.clipboard && navigator.clipboard.writeText) {{
        navigator.clipboard.writeText(tel).then(function(){{ fertig(true); }},
                                                function(){{ fertig(false); }});
      }} else {{ fertig(false); }}
    }});
  }}
  // ----- Geschützte Namensanzeige für geprüfte Stellen -----
  var GESCHUETZT = __NAMEDATEN__;
  var fsKnopf = document.getElementById("fsKnopf");
  var fsPasswort = document.getElementById("fsPasswort");
  var fsErgebnis = document.getElementById("fsErgebnis");

  function b64Bytes(s){{
    var roh = atob(s), arr = new Uint8Array(roh.length);
    for (var i = 0; i < roh.length; i++) arr[i] = roh.charCodeAt(i);
    return arr;
  }}

  function fsMeldung(text, klasse){{
    fsErgebnis.textContent = text;
    fsErgebnis.className = "fs-ergebnis " + (klasse || "");
  }}

  function nameFreischalten(){{
    var pw = fsPasswort.value;
    if (!pw) {{ fsMeldung("Bitte das Freischalt-Passwort eingeben.", "fehler"); return; }}
    if (!(window.crypto && crypto.subtle)) {{
      fsMeldung("Dieser Browser unterstützt die Entschlüsselung nicht.", "fehler");
      return;
    }}
    fsMeldung("Prüfe …", "");
    fsKnopf.disabled = true;
    var enc = new TextEncoder();
    crypto.subtle.importKey("raw", enc.encode(pw), "PBKDF2", false, ["deriveKey"])
      .then(function(basis){{
        return crypto.subtle.deriveKey(
          {{name:"PBKDF2", salt:b64Bytes(GESCHUETZT.s), iterations:GESCHUETZT.it, hash:"SHA-256"}},
          basis, {{name:"AES-GCM", length:256}}, false, ["decrypt"]);
      }})
      .then(function(schluessel){{
        return crypto.subtle.decrypt({{name:"AES-GCM", iv:b64Bytes(GESCHUETZT.iv)}},
                                     schluessel, b64Bytes(GESCHUETZT.c));
      }})
      .then(function(klar){{
        var name = new TextDecoder().decode(klar);
        fsMeldung("Betreiber: " + name, "ok");
        fsKnopf.disabled = false;
      }})
      .catch(function(){{
        fsMeldung("Passwort nicht korrekt.", "fehler");
        fsKnopf.disabled = false;
      }});
  }}

  if (fsKnopf) {{
    fsKnopf.addEventListener("click", nameFreischalten);
    fsPasswort.addEventListener("keydown", function(ev){{
      if (ev.key === "Enter") nameFreischalten();
    }});
  }}
}})();
</script>
</body>
</html>
'''

page = page.replace("__QRDATEN__", QRDATEN).replace("__NAMEDATEN__", NAMEDATEN)
ziel = AUSGABE / 'impressum.html'
ziel.write_text(page, encoding='utf-8')
print("Impressum gebaut:", ziel, "|", len(page)//1024, "KB")
