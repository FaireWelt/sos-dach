# -*- coding: utf-8 -*-
"""FaireWelt Hilfeinfos – professionelle Version.
Helles, ruhiges Design mit dem Hände-Banner, Themen-Schnellauswahl
und fester Direktwahl-Leiste auf dem Handy."""
import html as H
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
from data import GROUPS
from data2 import GROUPS2

AUSGABE = HIER.parent if HIER.name == "werkzeug" else HIER

ALL_GROUPS = GROUPS + GROUPS2
LOGO   = (HIER / 'logo_b64.txt').read_text().strip()
HAND   = (HIER / 'hand_b64.txt').read_text().strip()
BANNER = (HIER / 'banner_b64.txt').read_text().strip()
FAV    = (HIER / 'favicon_b64.txt').read_text().strip()
QRDATEN = (HIER / 'qr_map.json').read_text().strip()

LAND_NAME = {"DE": "Deutschland", "AT": "Österreich", "CH": "Schweiz"}
LAND_FLAG = {"DE": "🇩🇪", "AT": "🇦🇹", "CH": "🇨🇭"}

# Dezente Strich-Icons (Feather-Stil) je Themengruppe
SVG = {
 "alert":  '<path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
 "heart":  '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>',
 "users":  '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
 "sun":    '<circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>',
 "plus":   '<rect x="3" y="3" width="18" height="18" rx="2"/><line x1="12" y1="8" x2="12" y2="16"/><line x1="8" y1="12" x2="16" y2="12"/>',
 "case":   '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
 "phone":  '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
 "globe":  '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
 "insta":  '<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/>',
 "info":   '<circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/>',
 "walk":   '<circle cx="13" cy="4" r="2"/><path d="M13 8l-2 5 3 3v5"/><path d="M11 13l-3 2-2 5"/><path d="M13 8l3 2 3 1"/>',
}
GROUP_ICON = {"notfall":"alert","seele":"heart","familie":"users","gewalt":"shield",
              "vielfalt":"sun","gesundheit":"plus","soziales":"case","weitere":"phone"}

def icon(name, cls="ic"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{SVG[name]}</svg>')

def esc(t): return H.escape(t, quote=True)

# ----------------------------------------------------------------- Bausteine
def render_entry(e):
    out = ['<div class="eintrag">']
    out.append(f'<p class="e-name">{esc(e["name"])}</p>')
    if e["phones"]:
        out.append('<div class="e-nummern">')
        for anzeige, tel in e["phones"]:
            out.append(f'<a class="telknopf" href="tel:{esc(tel)}">{icon("phone","ic ic-tel")}<span>{esc(anzeige)}</span></a>')
        out.append('</div>')
    if e["desc"]:
        out.append(f'<p class="e-desc">{esc(e["desc"])}</p>')
    links = []
    if e["web"]:
        webs = [x.strip() for x in e["web"].split(" / ")] if " / " in e["web"] else [e["web"]]
        for w in webs:
            url = w if w.startswith("http") else "https://" + w
            links.append(f'<a class="e-link" href="{esc(url)}" target="_blank" rel="noopener">{icon("globe","ic ic-s")}{esc(w)}</a>')
    if e["insta"]:
        handle = e["insta"].lstrip("@")
        links.append(f'<a class="e-link" href="https://www.instagram.com/{esc(handle)}/" target="_blank" rel="noopener">{icon("insta","ic ic-s")}{esc(e["insta"])}</a>')
    if e["extra"]:
        links.append(f'<span class="e-extra">{icon("info","ic ic-s")}{esc(e["extra"])}</span>')
    if links:
        out.append('<div class="e-links">' + "".join(links) + '</div>')
    out.append('</div>')
    return "".join(out)

def render_signal():
    return f'''<details class="thema" id="thema-signal" data-suche="signal for help handzeichen hilfe zeichen gewalt notlage diskret häusliche">
<summary><span class="t-titel">Signal for Help – das Handzeichen für stille Hilfe</span><span class="t-badge">Wichtig</span>{icon("chevron") if False else '<svg class="ic t-pfeil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>'}</summary>
<div class="t-inhalt">
<div class="signal-karte">
  <img class="signal-bild" src="data:image/webp;base64,{HAND}" alt="Signal-for-Help-Handzeichen: offene Handfläche, Daumen eingeklappt, Finger schließen sich darüber" width="140" height="140" loading="lazy">
  <div class="signal-text">
    <p class="signal-lead">Dieses Handzeichen ist weltweit bekannt und kann Leben retten.</p>
    <p><strong>So funktioniert es:</strong></p>
    <ol>
      <li>Zeige Deine Handfläche – offen und nach außen gerichtet.</li>
      <li>Klappe den Daumen in die Handfläche.</li>
      <li>Schließe die Finger über den Daumen – so wird er „eingeschlossen“.</li>
    </ol>
    <p><strong>Wenn Du Hilfe brauchst,</strong> zeige dieses Handzeichen – zum Beispiel unauffällig in einem Videoanruf oder durch ein Fenster.</p>
    <p><strong>Wenn Dir jemand dieses Zeichen zeigt:</strong> Hilf – aber bring Dich dabei nicht selbst in Gefahr.</p>
    <p class="signal-hinweis"><strong>Wichtig zu wissen:</strong> Das Zeichen ist kein offizieller Notruf, sondern ein diskreter Hinweis, dass jemand Hilfe benötigt. Es bedeutet nicht automatisch „Ruf die Polizei“, sondern eher: <em>„Kontaktiere mich sicher und frag, wie Du helfen kannst.“</em></p>
  </div>
</div>
</div>
</details>'''

def render_topic(t):
    if t.get("special") == "signal":
        return render_signal()
    such = [t["title"]]
    body = []
    for land in ("DE", "AT", "CH"):
        eintraege = t["entries"].get(land, [])
        if not eintraege:
            continue
        for e in eintraege:
            such += [e["name"], e["desc"] or ""]
            such += [p[0] for p in e["phones"]]
        body.append(f'<div class="land land-{land.lower()}">')
        body.append(f'<h4 class="land-titel"><span class="flagge" aria-hidden="true">{LAND_FLAG[land]}</span>{LAND_NAME[land]}</h4>')
        body += [render_entry(e) for e in eintraege]
        body.append('</div>')
    suchtext = esc(" ".join(such).lower())
    pfeil = '<svg class="ic t-pfeil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>'
    return (f'<details class="thema" id="thema-{t["id"]}" data-suche="{suchtext}">'
            f'<summary><span class="t-titel">{esc(t["title"])}</span>{pfeil}</summary>'
            f'<div class="t-inhalt">{"".join(body)}</div></details>')

def render_groups():
    out = []
    for g in ALL_GROUPS:
        out.append(f'<section class="gruppe" id="gruppe-{g["id"]}">')
        out.append(f'<h3 class="g-titel">{icon(GROUP_ICON[g["id"]], "ic g-ic")}<span>{esc(g["title"])}</span></h3>')
        out += [render_topic(t) for t in g["topics"]]
        out.append('</section>')
    return "\n".join(out)

def render_index():
    """Übersichtliche Themenliste – das schnelle Inhaltsverzeichnis."""
    out = ['<section class="index" id="themenliste">',
           '<h2 class="index-titel">Alle Hilfethemen im Überblick</h2>',
           '<p class="index-sub">Wähle Dein Thema – Du springst direkt zu den passenden Nummern für Deutschland, Österreich und die Schweiz.</p>',
           '<div class="index-spalten">']
    for g in ALL_GROUPS:
        out.append('<div class="index-block">')
        out.append(f'<p class="index-gruppe">{icon(GROUP_ICON[g["id"]], "ic ic-s")}{esc(g["title"])}</p>')
        out.append('<ul class="index-liste">')
        for t in g["topics"]:
            out.append(f'<li><a href="#thema-{t["id"]}">{esc(t["title"])}</a></li>')
        out.append('</ul></div>')
    out.append('</div></section>')
    return "".join(out)

def render_select():
    """Natives Sprungmenü – besonders schnell auf dem Handy."""
    out = ['<select id="themaSprung" aria-label="Direkt zu einem Hilfethema springen">',
           '<option value="" selected>Thema auswählen …</option>']
    for g in ALL_GROUPS:
        out.append(f'<optgroup label="{esc(g["title"])}">')
        for t in g["topics"]:
            out.append(f'<option value="thema-{t["id"]}">{esc(t["title"])}</option>')
        out.append('</optgroup>')
    out.append('</select>')
    return "".join(out)

# ----------------------------------------------------------------- Seite
page = f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<script>
(function(){{
  try {{
    var t = localStorage.getItem("fw-theme");
    if (t === "hell" || t === "dunkel") document.documentElement.setAttribute("data-theme", t);
  }} catch (e) {{ /* z. B. Privatmodus – dann greift automatisch die Systemeinstellung */ }}
}})();
</script>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#3e2a78">
<title>FaireWelt Hilfeinfos – Hilfetelefone &amp; Beratungsstellen für D-A-CH</title>
<meta name="description" content="Hilfetelefone, Seelsorgen und Beratungsstellen für Deutschland, Österreich und die Schweiz – übersichtlich zusammengestellt von FaireWelt.">
<link rel="icon" type="image/png" href="data:image/png;base64,{FAV}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
:root{{
  --papier:#f6f5f2; --karte:#ffffff; --tinte:#221c33; --nebel:#5f5a70;
  --violett:#4b3591; --violett-tief:#3e2a78; --violett-hell:#efeaf9;
  --bernstein:#c67900; --rot:#c0392b; --rot-hell:#fdf1ef;
  --linie:#e4e1da; --linie-stark:#cfcbc2;
  --de:#b98514; --at:#b3453f; --ch:#2e8c82;
  --rund:14px; --rund-klein:10px;
  --schatten:0 1px 3px rgba(34,28,51,.08),0 4px 16px rgba(34,28,51,.06);
  --werkzeuge-bg:rgba(255,255,255,.96);
  --rot-rand:#e8c4bd; --violett-rand:#d8cdf0; --platzhalter:#eceae6; --platzhalter-schrift:#9a95a8;
  --display:"Manrope","Segoe UI",system-ui,sans-serif;
  --text:"Atkinson Hyperlegible","Segoe UI",system-ui,sans-serif;
  --bar-hoehe:0px;
  color-scheme:light;
}}
/* Nachtsicht: gedämpfte, dunkle Ansicht – unauffällig und blendfrei.
   Greift automatisch nach Systemeinstellung, per Hand umschaltbar. */
@media (prefers-color-scheme:dark){{
  :root:not([data-theme="hell"]){{
    --papier:#15121f; --karte:#1e1a2b; --tinte:#f1eef7; --nebel:#a79fc0;
    --violett:#7c3aed; --violett-tief:#9061f9; --violett-hell:#241c3d;
    --bernstein:#e2a13c; --rot:#cf3e33; --rot-hell:#2a1512;
    --linie:#2e293f; --linie-stark:#453d5c;
    --de:#d9a53d; --at:#e07a72; --ch:#4fbdb0;
    --schatten:0 1px 3px rgba(0,0,0,.4),0 4px 20px rgba(0,0,0,.35);
    --werkzeuge-bg:rgba(21,18,31,.94);
    --rot-rand:#5c2c26; --violett-rand:#3d3159; --platzhalter:#1e1a2b; --platzhalter-schrift:#6b6485;
    color-scheme:dark;
  }}
}}
:root[data-theme="dunkel"]{{
  --papier:#15121f; --karte:#1e1a2b; --tinte:#f1eef7; --nebel:#a79fc0;
  --violett:#7c3aed; --violett-tief:#9061f9; --violett-hell:#241c3d;
  --bernstein:#e2a13c; --rot:#cf3e33; --rot-hell:#2a1512;
  --linie:#2e293f; --linie-stark:#453d5c;
  --de:#d9a53d; --at:#e07a72; --ch:#4fbdb0;
  --schatten:0 1px 3px rgba(0,0,0,.4),0 4px 20px rgba(0,0,0,.35);
  --werkzeuge-bg:rgba(21,18,31,.94);
  --rot-rand:#5c2c26; --violett-rand:#3d3159; --platzhalter:#1e1a2b; --platzhalter-schrift:#6b6485;
  color-scheme:dark;
}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
@media (prefers-reduced-motion:reduce){{
  html{{scroll-behavior:auto}}
  *,*::before,*::after{{animation:none!important;transition:none!important}}
}}
body{{
  margin:0;background:var(--papier);color:var(--tinte);
  font-family:var(--text);font-size:17px;line-height:1.55;
  padding-bottom:var(--bar-hoehe);
  -webkit-tap-highlight-color:rgba(75,53,145,.15);
  transition:background-color .2s ease,color .2s ease;
}}
a{{color:var(--violett)}}
a:focus-visible,button:focus-visible,summary:focus-visible,input:focus-visible,select:focus-visible{{
  outline:3px solid var(--violett);outline-offset:2px;border-radius:6px;
}}
.ic{{width:1.15em;height:1.15em;flex:none;vertical-align:-.18em}}
.ic-s{{width:1em;height:1em}}

/* ---------- Kopf mit Banner ---------- */
.banner{{
  display:block;width:100%;height:clamp(120px,17vw,240px);
  object-fit:cover;object-position:38% center;
  border-bottom:4px solid var(--violett-tief);background:var(--platzhalter);
}}
.kopf{{background:var(--karte);border-bottom:1px solid var(--linie)}}
.kopf-innen{{max-width:1060px;margin:0 auto;padding:26px 20px 22px;display:flex;gap:18px;align-items:center;flex-wrap:wrap}}
.kopf img.logo{{width:72px;height:72px;border-radius:50%;flex:none;box-shadow:var(--schatten)}}
.kopf h1{{font-family:var(--display);font-weight:800;font-size:clamp(1.5rem,3.6vw,2.15rem);margin:0;letter-spacing:-.01em}}
.kopf h1 .fw{{color:var(--violett)}}
.leitsatz{{margin:.35em 0 0;color:var(--nebel);max-width:62ch}}
.leitsatz strong{{color:var(--tinte)}}
.leitsatz a{{font-weight:700;text-decoration:none}}
.leitsatz a:hover{{text-decoration:underline}}

/* ---------- Werkzeugleiste ---------- */
.werkzeuge{{
  position:sticky;top:0;z-index:50;background:var(--werkzeuge-bg);
  backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);
  border-bottom:1px solid var(--linie);box-shadow:0 2px 10px rgba(34,28,51,.05);
}}
.werkzeuge-innen{{max-width:1060px;margin:0 auto;padding:10px 20px;display:flex;gap:10px;flex-wrap:wrap;align-items:center}}
.suche{{flex:1 1 230px;position:relative;min-width:200px}}
.suche input{{
  width:100%;padding:10px 14px 10px 40px;border-radius:10px;border:1.5px solid var(--linie-stark);
  background:var(--karte);color:var(--tinte);font:inherit;font-size:1rem;
}}
.suche input::placeholder{{color:var(--platzhalter-schrift)}}
.suche .ic{{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--nebel);pointer-events:none}}
#themaSprung{{
  flex:1 1 220px;min-width:190px;max-width:340px;
  padding:10px 12px;border-radius:10px;border:1.5px solid var(--linie-stark);
  background:var(--karte);color:var(--tinte);font:inherit;font-size:1rem;cursor:pointer;
}}
.laender{{display:flex;gap:0;border:1.5px solid var(--linie-stark);border-radius:10px;overflow:hidden}}
.land-knopf{{
  font-family:var(--display);font-weight:700;font-size:.92rem;
  padding:10px 13px;border:none;cursor:pointer;background:var(--karte);color:var(--nebel);
  border-right:1.5px solid var(--linie);min-height:44px;
}}
.land-knopf:last-child{{border-right:none}}
.land-knopf[aria-pressed="true"]{{background:var(--violett);color:#fff}}
.land-knopf:not([aria-pressed="true"]):hover{{background:var(--violett-hell);color:var(--violett)}}
.theme-knopf{{
  display:flex;align-items:center;gap:7px;flex:none;
  font-family:var(--display);font-weight:700;font-size:.92rem;
  padding:9px 14px;border-radius:10px;border:1.5px solid var(--linie-stark);
  background:var(--karte);color:var(--nebel);cursor:pointer;min-height:44px;
}}
.theme-knopf:hover{{border-color:var(--violett);color:var(--violett)}}
.theme-knopf[aria-pressed="true"]{{background:var(--violett-hell);border-color:var(--violett);color:var(--violett)}}
.theme-mond{{display:block}}
.theme-sonne{{display:none}}
.theme-knopf[aria-pressed="true"] .theme-mond{{display:none}}
.theme-knopf[aria-pressed="true"] .theme-sonne{{display:block}}
@media (max-width:700px){{.theme-text{{display:none}}.theme-knopf{{padding:9px 12px}}}}

/* ---------- Notfallstreifen ---------- */
.sos{{max-width:1060px;margin:20px auto 0;padding:0 20px}}
.sos-karte{{
  background:var(--rot-hell);border:1.5px solid var(--rot-rand);border-left:5px solid var(--rot);
  border-radius:var(--rund);padding:14px 18px;
}}
.sos-karte h2{{font-family:var(--display);font-size:1.05rem;font-weight:800;margin:0 0 8px;color:var(--rot);display:flex;gap:8px;align-items:center}}
.sos-zeilen{{display:flex;flex-wrap:wrap;gap:6px 22px}}
.sos-zeile{{display:flex;align-items:center;gap:8px;flex-wrap:wrap}}
.sos-land{{font-size:1.05rem}}
.sos-tel{{
  display:inline-block;text-decoration:none;font-family:var(--display);font-weight:800;
  background:#fff;color:var(--rot);border:1.5px solid var(--rot);border-radius:8px;
  padding:5px 12px;font-size:.98rem;min-height:34px;
}}
.sos-tel:hover{{background:var(--rot);color:#fff}}
.sos-hinweis{{margin:8px 0 0;font-size:.9rem;color:var(--nebel)}}
.sos-hinweis a{{color:var(--rot);font-weight:700}}

/* ---------- Themenliste (Index) ---------- */
.index{{max-width:1060px;margin:26px auto 0;padding:0 20px}}
.index-titel{{font-family:var(--display);font-weight:800;font-size:1.35rem;margin:0}}
.index-sub{{margin:.35em 0 14px;color:var(--nebel)}}
.index-spalten{{columns:3;column-gap:22px}}
.index-block{{
  break-inside:avoid;background:var(--karte);border:1px solid var(--linie);
  border-radius:var(--rund);padding:14px 16px;margin:0 0 14px;box-shadow:var(--schatten);
}}
.index-gruppe{{
  font-family:var(--display);font-weight:800;font-size:.95rem;margin:0 0 6px;
  color:var(--violett);display:flex;align-items:center;gap:8px;
}}
.index-liste{{list-style:none;margin:0;padding:0}}
.index-liste li{{border-top:1px solid var(--linie)}}
.index-liste li:first-child{{border-top:none}}
.index-liste a{{
  display:block;padding:8px 4px;text-decoration:none;color:var(--tinte);font-size:.97rem;
  border-radius:6px;
}}
.index-liste a:hover{{color:var(--violett);background:var(--violett-hell)}}
@media (max-width:920px){{.index-spalten{{columns:2}}}}
@media (max-width:620px){{.index-spalten{{columns:1}}}}

/* ---------- Gruppen & Themen ---------- */
main{{max-width:1060px;margin:0 auto;padding:6px 20px 70px}}
.gruppe{{margin-top:34px;scroll-margin-top:86px}}
.g-titel{{
  font-family:var(--display);font-weight:800;font-size:1.3rem;margin:0 0 10px;
  display:flex;align-items:center;gap:10px;color:var(--violett-tief);
}}
.g-ic{{width:1.25em;height:1.25em;color:var(--violett)}}
.thema{{
  background:var(--karte);border:1px solid var(--linie);border-radius:var(--rund);
  margin:10px 0;box-shadow:var(--schatten);scroll-margin-top:86px;
}}
.thema[open]{{border-color:var(--violett)}}
.thema summary{{
  list-style:none;cursor:pointer;display:flex;align-items:center;gap:12px;
  padding:15px 18px;font-family:var(--display);font-weight:700;font-size:1.04rem;
  min-height:52px;user-select:none;border-radius:var(--rund);
}}
.thema summary::-webkit-details-marker{{display:none}}
.thema summary:hover{{background:var(--violett-hell)}}
.t-titel{{flex:1}}
.t-badge{{
  font-size:.75rem;font-weight:800;letter-spacing:.04em;text-transform:uppercase;
  background:var(--violett);color:#fff;border-radius:999px;padding:3px 10px;flex:none;
}}
.t-pfeil{{color:var(--nebel);transition:transform .18s ease}}
.thema[open] .t-pfeil{{transform:rotate(180deg);color:var(--violett)}}
.t-inhalt{{padding:2px 18px 16px;border-top:1px solid var(--linie)}}
.land{{margin-top:14px}}
.land-titel{{
  font-family:var(--display);font-size:.92rem;font-weight:800;margin:0 0 8px;
  color:var(--nebel);display:flex;align-items:center;gap:8px;
  text-transform:uppercase;letter-spacing:.05em;
}}
.flagge{{font-size:1.25em}}
.eintrag{{
  background:var(--papier);border:1px solid var(--linie);border-radius:var(--rund-klein);
  padding:12px 14px;margin:8px 0;border-left-width:4px;
}}
.land-de .eintrag{{border-left-color:var(--de)}}
.land-at .eintrag{{border-left-color:var(--at)}}
.land-ch .eintrag{{border-left-color:var(--ch)}}
.e-name{{font-weight:700;margin:0}}
.e-nummern{{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}}
.telknopf{{
  display:inline-flex;align-items:center;gap:8px;text-decoration:none;
  font-family:var(--display);font-weight:800;font-size:1.02rem;letter-spacing:.02em;
  background:var(--violett);color:#fff;border-radius:9px;padding:9px 15px;min-height:42px;
  transition:background .12s ease;
}}
.telknopf:hover{{background:var(--violett-tief)}}
.ic-tel{{width:1em;height:1em}}
.e-desc{{margin:8px 0 0;color:var(--tinte)}}
.e-links{{margin-top:9px;display:flex;flex-wrap:wrap;gap:6px 18px;font-size:.93rem}}
.e-link,.e-extra{{display:inline-flex;align-items:center;gap:6px}}
.e-link{{text-decoration:none;font-weight:700}}
.e-link:hover{{text-decoration:underline}}
.e-link .ic-s,.e-extra .ic-s{{color:var(--nebel)}}
.e-extra{{color:var(--nebel)}}

/* ---------- Signal for Help ---------- */
.signal-karte{{display:flex;gap:20px;align-items:flex-start;flex-wrap:wrap;margin-top:14px}}
.signal-bild{{
  flex:none;width:140px;height:140px;object-fit:contain;border-radius:var(--rund-klein);
  background:#fff;border:1px solid var(--linie);padding:8px;
}}
.signal-text{{flex:1;min-width:260px}}
.signal-lead{{font-family:var(--display);font-weight:800;font-size:1.08rem;color:var(--violett-tief);margin-top:0}}
.signal-text ol{{padding-left:1.3em;margin:.4em 0}}
.signal-text li{{margin:.3em 0}}
.signal-hinweis{{
  background:var(--violett-hell);border:1px solid var(--violett-rand);
  border-radius:var(--rund-klein);padding:10px 14px;
}}

/* ---------- Kein Treffer / Aktionen ---------- */
.listen-aktionen{{max-width:1060px;margin:18px auto 0;padding:0 20px;display:flex;gap:10px;justify-content:flex-end}}
.mini-knopf{{
  font:inherit;font-size:.88rem;font-weight:700;padding:8px 14px;border-radius:8px;cursor:pointer;
  background:var(--karte);color:var(--nebel);border:1.5px solid var(--linie-stark);min-height:40px;
}}
.mini-knopf:hover{{color:var(--violett);border-color:var(--violett)}}
.kein-treffer{{display:none;text-align:center;color:var(--nebel);padding:44px 20px}}
.kein-treffer strong{{color:var(--tinte);font-family:var(--display)}}

/* ---------- Fuß ---------- */
footer{{border-top:1px solid var(--linie);background:var(--karte)}}
.fuss-innen{{max-width:1060px;margin:0 auto;padding:28px 20px;display:flex;flex-wrap:wrap;gap:24px 40px;justify-content:space-between}}
.fuss-links{{display:flex;flex-direction:column;gap:8px}}
.fuss-links strong{{font-family:var(--display);margin-bottom:2px}}
.fuss-links a{{color:var(--tinte);text-decoration:none}}
.fuss-links a:hover{{color:var(--violett);text-decoration:underline}}
.fuss-hinweis{{max-width:48ch;color:var(--nebel);font-size:.92rem}}
.fuss-hinweis strong{{color:var(--tinte)}}

/* ---------- Nach oben ---------- */
#nachOben{{
  position:fixed;right:16px;bottom:calc(16px + var(--bar-hoehe));z-index:60;display:none;
  width:46px;height:46px;border-radius:50%;border:1.5px solid var(--linie-stark);cursor:pointer;
  background:var(--karte);color:var(--violett);font-size:1.3rem;font-weight:800;
  box-shadow:var(--schatten);
}}
#nachOben:hover{{background:var(--violett);color:#fff}}

/* ---------- Mobile Direktwahl-Leiste ---------- */
.schnellwahl{{
  display:none;position:fixed;left:0;right:0;bottom:0;z-index:70;
  background:var(--violett-tief);border-top:1px solid rgba(255,255,255,.18);
  padding:8px 10px calc(8px + env(safe-area-inset-bottom));
  box-shadow:0 -4px 18px rgba(34,28,51,.28);
}}
.schnellwahl-innen{{display:flex;gap:8px;max-width:560px;margin:0 auto}}
.sw-knopf{{
  flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;
  text-decoration:none;border-radius:10px;padding:8px 4px;min-height:56px;
  font-family:var(--display);line-height:1.2;text-align:center;
}}
.sw-knopf .sw-nr{{font-weight:800;font-size:1.05rem}}
.sw-knopf .sw-label{{font-size:.72rem;font-weight:700;opacity:.92}}
.sw-notruf{{background:var(--rot);color:#fff}}
.sw-polizei{{background:#fff;color:#3e2a78}}
.sw-weg{{background:#2e8c82;color:#fff}}
.sw-knopf:active{{filter:brightness(1.12)}}
@media (max-width:820px){{
  :root{{--bar-hoehe:calc(74px + env(safe-area-inset-bottom))}}
  .schnellwahl{{display:block}}
}}

/* ---------- Twitch-Banner ---------- */
.twitch-bereich{{max-width:1060px;margin:8px auto 34px;padding:0 20px}}
.twitch-banner{{
  display:flex;align-items:center;gap:22px;flex-wrap:wrap;text-decoration:none;
  background:linear-gradient(115deg,#772ce8 0%,#9146ff 55%,#a970ff 100%);
  border-radius:var(--rund);padding:24px 28px;color:#fff;
  box-shadow:0 6px 24px rgba(119,44,232,.35);
  transition:transform .15s ease,box-shadow .15s ease;
}}
.twitch-banner:hover{{transform:translateY(-3px);box-shadow:0 10px 32px rgba(119,44,232,.45)}}
.tb-logo{{
  width:110px;height:110px;border-radius:50%;flex:none;
  border:3px solid rgba(255,255,255,.85);box-shadow:0 4px 14px rgba(0,0,0,.25);
}}
.tb-text{{flex:1;min-width:230px;display:flex;flex-direction:column;gap:4px}}
.tb-live{{
  display:inline-flex;align-items:center;gap:7px;align-self:flex-start;
  font-family:var(--display);font-weight:800;font-size:.75rem;letter-spacing:.09em;
  text-transform:uppercase;background:rgba(0,0,0,.28);border-radius:999px;padding:4px 12px;
}}
.tb-punkt{{width:8px;height:8px;border-radius:50%;background:#ff4d4d;box-shadow:0 0 0 3px rgba(255,77,77,.35)}}
@keyframes tb-puls{{0%,100%{{opacity:1}}50%{{opacity:.35}}}}
.tb-punkt{{animation:tb-puls 1.6s ease-in-out infinite}}
.tb-titel{{font-family:var(--display);font-weight:800;font-size:clamp(1.35rem,3vw,1.8rem);line-height:1.15}}
.tb-sub{{opacity:.92;max-width:52ch}}
.tb-cta{{
  display:inline-flex;align-items:center;gap:9px;flex:none;
  font-family:var(--display);font-weight:800;font-size:1.05rem;
  background:#fff;color:#5c16c5;border-radius:10px;padding:13px 22px;min-height:48px;
  box-shadow:0 3px 12px rgba(0,0,0,.22);
}}
.twitch-banner:hover .tb-cta{{background:#f4edff}}
@media (max-width:640px){{
  .twitch-banner{{flex-direction:column;text-align:center;padding:22px 18px}}
  .tb-text{{align-items:center}}
  .tb-live{{align-self:center}}
  .tb-cta{{width:100%;justify-content:center}}
}}

/* ---------- QR-Dialog (PC → Handy) ---------- */
#qrDialog{{
  border:none;border-radius:var(--rund);padding:22px 24px;max-width:340px;width:calc(100vw - 40px);
  box-shadow:0 12px 48px rgba(34,28,51,.35);color:var(--tinte);font-family:var(--text);
  background:var(--karte);
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
.qr-nummer{{
  text-align:center;font-family:var(--display);font-weight:800;font-size:1.25rem;
  margin:.7em 0;letter-spacing:.02em;user-select:all;
}}
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

/* ---------- Startbildschirm (Handy) ---------- */
#startDialog{{
  border:none;border-radius:var(--rund);padding:20px 20px 22px;
  max-width:400px;width:calc(100vw - 28px);max-height:calc(100vh - 28px);
  box-shadow:0 12px 48px rgba(34,28,51,.4);color:var(--tinte);
  font-family:var(--text);overflow:auto;background:var(--karte);
}}
#startDialog::backdrop{{background:rgba(34,28,51,.6);backdrop-filter:blur(3px)}}
.start-kopf{{display:flex;align-items:center;gap:12px;margin-bottom:16px}}
.start-kopf img{{border-radius:50%;flex:none}}
.start-marke{{flex:1;display:flex;flex-direction:column;line-height:1.25}}
.start-marke strong{{font-family:var(--display);font-weight:800;font-size:1.02rem}}
.start-marke span{{color:var(--nebel);font-size:.86rem}}
.start-schritt h2{{font-family:var(--display);font-weight:800;font-size:1.22rem;margin:0 0 4px}}
.start-hinweis{{color:var(--nebel);font-size:.92rem;margin:0 0 14px}}
.start-laender{{display:flex;flex-direction:column;gap:10px}}
.start-land{{
  display:flex;align-items:center;gap:14px;width:100%;min-height:58px;
  font-family:var(--display);font-weight:800;font-size:1.08rem;text-align:left;
  background:var(--papier);color:var(--tinte);border:1.5px solid var(--linie-stark);
  border-radius:12px;padding:12px 16px;cursor:pointer;
}}
.start-land:hover{{border-color:var(--violett);background:var(--violett-hell)}}
.start-flagge{{font-size:1.7rem;line-height:1;flex:none}}
.start-alle{{
  justify-content:center;min-height:46px;font-size:.95rem;font-weight:700;
  background:var(--karte);color:var(--nebel);border-style:dashed;
}}
.start-weiter{{
  display:flex;align-items:center;justify-content:center;gap:8px;width:100%;
  margin-top:16px;min-height:46px;font:inherit;font-family:var(--display);
  font-weight:700;font-size:.95rem;background:none;color:var(--nebel);
  border:none;cursor:pointer;padding:8px;
}}
.start-weiter:hover{{color:var(--violett)}}
.start-weiter .ic{{width:1.05em;height:1.05em}}
.start-landchip{{
  display:inline-flex;align-items:center;gap:6px;margin:0 0 12px;
  font:inherit;font-size:.88rem;font-weight:700;color:var(--violett);
  background:var(--violett-hell);border:1px solid var(--violett-rand);border-radius:999px;
  padding:6px 14px;cursor:pointer;min-height:36px;
}}
.start-landchip:hover{{border-color:var(--violett)}}
.start-liste{{display:flex;flex-direction:column;gap:10px;margin-top:12px}}
.start-punkt{{
  display:flex;align-items:center;gap:14px;width:100%;min-height:58px;
  font-family:var(--display);font-weight:700;font-size:1rem;text-align:left;line-height:1.3;
  background:var(--violett);color:#fff;border:none;border-radius:12px;
  padding:12px 16px;cursor:pointer;
}}
.start-punkt:hover{{background:var(--violett-tief)}}
.start-punkt:first-child{{background:var(--rot)}}
.start-punkt:first-child:hover{{filter:brightness(1.08)}}
.start-ic{{width:26px;height:26px;flex:none}}
.start-hand{{
  flex:none;width:34px;height:34px;object-fit:contain;border-radius:8px;
  background:#fff;padding:2px;
}}
.start-uebersicht{{
  display:flex;align-items:center;justify-content:center;gap:8px;width:100%;margin-top:14px;min-height:48px;
  font-family:var(--display);font-weight:800;font-size:.95rem;text-align:center;
  background:var(--karte);color:var(--violett);border:1.5px solid var(--violett);
  border-radius:10px;padding:11px 14px;cursor:pointer;
}}
.start-uebersicht .ic{{width:1.05em;height:1.05em;flex:none}}
.start-uebersicht:hover{{background:var(--violett-hell)}}

/* ---------- Druck ---------- */
@media print{{
  body{{background:#fff;color:#000;font-size:11pt;padding-bottom:0}}
  .werkzeuge,.listen-aktionen,#nachOben,.schnellwahl,.banner,.twitch-bereich,#qrDialog,#startDialog{{display:none!important}}
  .thema,.eintrag,.sos-karte,.index-block{{box-shadow:none;break-inside:avoid}}
  .telknopf,.sos-tel{{background:none;color:#000;border:none;padding:0;font-weight:700}}
  .telknopf::before{{content:"Tel. "}}
  a{{color:#000}}
}}
@media (max-width:560px){{
  .kopf-innen{{padding:18px 16px 16px}}
  .kopf img.logo{{width:56px;height:56px}}
  .werkzeuge-innen{{padding:8px 12px}}
  .laender{{width:100%}}
  .land-knopf{{flex:1}}
  .thema summary{{padding:13px 14px;font-size:1rem}}
  .t-inhalt{{padding:2px 12px 14px}}
  main{{padding:6px 14px 60px}}
  .sos,.index,.listen-aktionen{{padding:0 14px}}
}}
</style>
</head>
<body>

<img class="banner" src="data:image/webp;base64,{BANNER}" alt="Eine offen ausgestreckte, helfende Hand mit einem Herzsymbol – daneben das FaireWelt-Logo" width="1600" height="270">

<header class="kopf">
  <div class="kopf-innen">
    <img class="logo" src="data:image/webp;base64,{LOGO}" alt="" width="72" height="72">
    <div>
      <h1><span class="fw">FaireWelt</span> Hilfeinfos</h1>
      <p class="leitsatz"><strong>Hier wird Dir geholfen.</strong> Geprüfte Hilfetelefone, Seelsorgen und Beratungsstellen für Deutschland, Österreich und die Schweiz – zusammengestellt von <a href="https://www.twitch.tv/fairewelt" target="_blank" rel="noopener">twitch.tv/fairewelt</a>.</p>
    </div>
  </div>
</header>

<div class="werkzeuge">
  <div class="werkzeuge-innen">
    <div class="suche">
      {icon("lupe") if False else '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>'}
      <input type="search" id="sucheingabe" placeholder="Suchen, z.&nbsp;B. „Mobbing“ oder „Trauer“" aria-label="Hilfethemen durchsuchen">
    </div>
    {render_select()}
    <div class="laender" role="group" aria-label="Nach Land filtern">
      <button class="land-knopf" data-land="alle" aria-pressed="true">Alle</button>
      <button class="land-knopf" data-land="de" aria-pressed="false">🇩🇪 DE</button>
      <button class="land-knopf" data-land="at" aria-pressed="false">🇦🇹 AT</button>
      <button class="land-knopf" data-land="ch" aria-pressed="false">🇨🇭 CH</button>
    </div>
    <button class="theme-knopf" id="themeKnopf" type="button" aria-pressed="false" title="Nachtsicht: dunkle, blendfreie Ansicht">
      <svg class="ic theme-mond" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
      <svg class="ic theme-sonne" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{SVG["sun"]}</svg>
      <span class="theme-text">Nachtsicht</span>
    </button>
  </div>
</div>

<div class="sos" id="sos">
  <div class="sos-karte">
    <h2>{icon("alert")}Im akuten Notfall sofort anrufen</h2>
    <div class="sos-zeilen">
      <div class="sos-zeile sos-de"><span class="sos-land" aria-hidden="true">🇩🇪</span>
        <a class="sos-tel" href="tel:112">112 Feuerwehr / Rettung</a>
        <a class="sos-tel" href="tel:110">110 Polizei</a></div>
      <div class="sos-zeile sos-at"><span class="sos-land" aria-hidden="true">🇦🇹</span>
        <a class="sos-tel" href="tel:144">144 Rettung</a>
        <a class="sos-tel" href="tel:133">133 Polizei</a>
        <a class="sos-tel" href="tel:122">122 Feuerwehr</a></div>
      <div class="sos-zeile sos-ch"><span class="sos-land" aria-hidden="true">🇨🇭</span>
        <a class="sos-tel" href="tel:144">144 Sanität</a>
        <a class="sos-tel" href="tel:117">117 Polizei</a>
        <a class="sos-tel" href="tel:118">118 Feuerwehr</a></div>
    </div>
    <p class="sos-hinweis">Der Euronotruf <a href="tel:112">112</a> funktioniert in allen drei Ländern – kostenlos, rund um die Uhr, auch vom Handy.</p>
  </div>
</div>

{render_index()}

<div class="listen-aktionen">
  <button class="mini-knopf" id="alleAuf">Alle Themen öffnen</button>
  <button class="mini-knopf" id="alleZu">Alle schließen</button>
</div>

<main>
{render_groups()}
<div class="kein-treffer" id="keinTreffer">
  <strong>Dazu haben wir leider noch nichts gefunden.</strong><br>
  Versuch es mit einem anderen Begriff – oder schreib uns im Stream, dann ergänzen wir das Thema.
</div>
</main>

<section class="twitch-bereich">
  <a class="twitch-banner" href="https://www.twitch.tv/fairewelt" target="_blank" rel="noopener" aria-label="FaireWelt auf Twitch besuchen – öffnet in neuem Tab">
    <img class="tb-logo" src="data:image/webp;base64,{LOGO}" alt="" width="110" height="110">
    <div class="tb-text">
      <span class="tb-live"><span class="tb-punkt" aria-hidden="true"></span>Live-Community</span>
      <span class="tb-titel">FaireWelt auf Twitch</span>
      <span class="tb-sub">Gaming, gute Gespräche und eine Community, die aufeinander achtet – bei uns bist Du willkommen, wie Du bist.</span>
    </div>
    <span class="tb-cta">Jetzt vorbeischauen<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></span>
  </a>
</section>

<dialog id="startDialog" aria-labelledby="startTitel">
  <div class="start-kopf">
    <img src="data:image/webp;base64,{LOGO}" alt="" width="46" height="46">
    <div class="start-marke">
      <strong>FaireWelt Hilfeinfos</strong>
      <span>Hier wird Dir geholfen.</span>
    </div>
    <button class="qr-schliessen" id="startZu" aria-label="Überspringen und zur Übersicht">✕</button>
  </div>

  <div class="start-schritt" id="startSchritt1">
    <h2 id="startTitel">In welchem Land befindest Du Dich?</h2>
    <p class="start-hinweis">Damit zeigen wir Dir sofort die richtigen Nummern.</p>
    <div class="start-laender">
      <button class="start-land" data-land="de"><span class="start-flagge" aria-hidden="true">🇩🇪</span>Deutschland</button>
      <button class="start-land" data-land="at"><span class="start-flagge" aria-hidden="true">🇦🇹</span>Österreich</button>
      <button class="start-land" data-land="ch"><span class="start-flagge" aria-hidden="true">🇨🇭</span>Schweiz</button>
      <button class="start-land start-alle" data-land="alle">Alle Länder anzeigen</button>
    </div>
    <button class="start-weiter" id="startWeiter1">Weiter zur Seite<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></button>
  </div>

  <div class="start-schritt" id="startSchritt2" hidden>
    <button class="start-landchip" id="startLandChip" aria-label="Land ändern"></button>
    <h2>Schnelle Hilfe bei akuter Gefahr</h2>
    <div class="start-liste">
      <button class="start-punkt" data-ziel="thema-notruf">
        <svg class="ic start-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{SVG["alert"]}</svg>
        <span>Allgemeine Notrufnummern</span></button>
      <button class="start-punkt" data-ziel="gruppe-gewalt">
        <svg class="ic start-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{SVG["shield"]}</svg>
        <span>Gewalt, Missbrauch &amp; Schutz</span></button>
      <button class="start-punkt" data-ziel="thema-heimweg">
        <svg class="ic start-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{SVG["walk"]}</svg>
        <span>Heimwegtelefon &amp; Begleitung</span></button>
      <button class="start-punkt" data-ziel="thema-aufdringlich">
        <svg class="ic start-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{SVG["phone"]}<line x1="23" y1="1" x2="1" y2="23"/></svg>
        <span>Hilfe gegen aufdringliche Personen</span></button>
      <button class="start-punkt" data-ziel="thema-signal">
        <img class="start-hand" src="data:image/webp;base64,{HAND}" alt="" width="34" height="34">
        <span>INFOS! Signal for Help – das stille Handzeichen</span></button>
    </div>
    <button class="start-uebersicht" id="startUebersicht">Weiter zur Seite – alle Hilfethemen ansehen<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></button>
  </div>
</dialog>

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
    <div class="fuss-links">
      <strong>FaireWelt im Netz</strong>
      <a href="https://www.twitch.tv/fairewelt" target="_blank" rel="noopener">FaireWelt auf Twitch</a>
      <a href="https://discord.gg/84crvbx9E4" target="_blank" rel="noopener">Discord-Server FaireWelt</a>
      <a href="https://www.youtube.com/@FaireWeltYT" target="_blank" rel="noopener">FaireWelt bei YouTube</a>
      <a href="https://linktr.ee/FaireWelt" target="_blank" rel="noopener">Linktree von Fynn</a>
      <a href="impressum.html">Impressum</a>
    </div>
    <p class="fuss-hinweis">Wir hoffen, wir konnten Dir mit der gesuchten Information helfen.<br><br>
    <strong>Alle Angaben ohne Gewähr</strong> auf Fehler und Funktion aufgrund von Änderungen. Nummern und Angebote können sich ändern – im Zweifel bitte auf der verlinkten Website nachsehen. Stand: Juli 2026.</p>
  </div>
</footer>

<button id="nachOben" title="Nach oben" aria-label="Nach oben scrollen">↑</button>

<nav class="schnellwahl" aria-label="Schnellwahl für direkte Hilfe">
  <div class="schnellwahl-innen">
    <a class="sw-knopf sw-notruf" href="tel:112">
      <span class="sw-nr">112</span><span class="sw-label">Notruf</span>
    </a>
    <a class="sw-knopf sw-polizei" id="swPolizei" href="tel:110">
      <span class="sw-nr" id="swPolizeiNr">110 🇩🇪</span><span class="sw-label">Polizei</span>
    </a>
    <a class="sw-knopf sw-weg" id="swWeg" href="tel:03012074182">
      <span class="sw-nr" id="swWegNr">Anrufen 🇩🇪</span><span class="sw-label">Wegbegleitung</span>
    </a>
  </div>
</nav>

<script>
(function(){{
  "use strict";

  // ----- Nachtsicht: Umschalter, Systemerkennung, theme-color-Meta -----
  var themeKnopf = document.getElementById("themeKnopf");
  var systemDunkel = window.matchMedia("(prefers-color-scheme: dark)");
  var themeMeta = document.querySelector('meta[name="theme-color"]');

  function gespeichertesTheme(){{
    try {{ return localStorage.getItem("fw-theme"); }} catch (e) {{ return null; }}
  }}
  function themeMerken(wert){{
    try {{
      if (wert) localStorage.setItem("fw-theme", wert);
      else localStorage.removeItem("fw-theme");
    }} catch (e) {{ /* z. B. Privatmodus */ }}
  }}
  function effektivDunkel(){{
    var gespeichert = gespeichertesTheme();
    if (gespeichert === "dunkel") return true;
    if (gespeichert === "hell") return false;
    return systemDunkel.matches;
  }}
  function themeAnzeigeAktualisieren(){{
    var dunkel = effektivDunkel();
    themeKnopf.setAttribute("aria-pressed", dunkel ? "true" : "false");
    themeKnopf.querySelector(".theme-text").textContent = dunkel ? "Tagsicht" : "Nachtsicht";
    if (themeMeta) themeMeta.setAttribute("content", dunkel ? "#15121f" : "#3e2a78");
  }}
  themeKnopf.addEventListener("click", function(){{
    var neuDunkel = !effektivDunkel();
    // Stimmt die Wahl zufällig wieder mit der Systemeinstellung überein,
    // wird nichts mehr gespeichert – dann folgt die Seite wieder automatisch dem System.
    if (neuDunkel === systemDunkel.matches) {{
      document.documentElement.removeAttribute("data-theme");
      themeMerken(null);
    }} else {{
      var wert = neuDunkel ? "dunkel" : "hell";
      document.documentElement.setAttribute("data-theme", wert);
      themeMerken(wert);
    }}
    themeAnzeigeAktualisieren();
  }});
  if (systemDunkel.addEventListener) {{
    systemDunkel.addEventListener("change", function(){{
      if (!gespeichertesTheme()) themeAnzeigeAktualisieren();
    }});
  }}
  themeAnzeigeAktualisieren();

  var aktivesLand = "alle";
  var suchEingabe = document.getElementById("sucheingabe");
  var themen = Array.prototype.slice.call(document.querySelectorAll(".thema"));
  var gruppen = Array.prototype.slice.call(document.querySelectorAll(".gruppe"));
  var keinTreffer = document.getElementById("keinTreffer");

  // ----- Schnellwahl-Daten (Handy-Leiste) -----
  var POLIZEI = {{de:"110", at:"133", ch:"117"}};
  var WEG = {{
    de:{{tel:"03012074182", nr:"Anrufen"}},
    at:{{tel:"03168722200", nr:"Anrufen"}},
    ch:null  // Schweiz: nur Apps – Knopf führt zum Thema
  }};
  var FLAGGE = {{de:"\\uD83C\\uDDE9\\uD83C\\uDDEA", at:"\\uD83C\\uDDE6\\uD83C\\uDDF9", ch:"\\uD83C\\uDDE8\\uD83C\\uDDED"}};

  function schnellwahlAktualisieren(){{
    var land = (aktivesLand === "alle") ? "de" : aktivesLand;
    var flagge = (aktivesLand === "alle") ? FLAGGE.de : FLAGGE[land];
    var pol = document.getElementById("swPolizei");
    pol.href = "tel:" + POLIZEI[land];
    document.getElementById("swPolizeiNr").textContent = POLIZEI[land] + " " + flagge;
    var weg = document.getElementById("swWeg");
    var wegNr = document.getElementById("swWegNr");
    if (WEG[land]) {{
      weg.href = "tel:" + WEG[land].tel;
      weg.removeAttribute("data-sprung");
      wegNr.textContent = WEG[land].nr + " " + flagge;
    }} else {{
      weg.href = "#thema-heimweg";
      weg.setAttribute("data-sprung", "thema-heimweg");
      wegNr.textContent = "Apps " + flagge;
    }}
  }}

  // ----- Länderfilter -----
  function landAnwenden(){{
    ["de","at","ch"].forEach(function(l){{
      var zeigen = (aktivesLand === "alle" || aktivesLand === l);
      document.querySelectorAll(".land-" + l).forEach(function(el){{
        el.style.display = zeigen ? "" : "none";
      }});
      document.querySelectorAll(".sos-" + l).forEach(function(el){{
        el.style.display = zeigen ? "" : "none";
      }});
    }});
    schnellwahlAktualisieren();
  }}
  function landSetzen(land){{
    aktivesLand = land;
    document.querySelectorAll(".land-knopf").forEach(function(k){{
      k.setAttribute("aria-pressed", k.dataset.land === land ? "true" : "false");
    }});
    landAnwenden();
  }}
  document.querySelectorAll(".land-knopf").forEach(function(knopf){{
    knopf.addEventListener("click", function(){{
      landSetzen(knopf.dataset.land);
      landMerken(knopf.dataset.land);
    }});
  }});

  // ----- Landeswahl merken (falls der Browser es erlaubt) -----
  function landMerken(land){{
    try {{ localStorage.setItem("fw-land", land); }} catch (e) {{ /* z. B. Privatmodus */ }}
  }}
  function gemerktesLand(){{
    try {{ return localStorage.getItem("fw-land"); }} catch (e) {{ return null; }}
  }}

  // ----- Thema öffnen & hinspringen -----
  function themaOeffnen(id){{
    var ziel = document.getElementById(id);
    if (!ziel) return;
    if (ziel.tagName === "DETAILS") {{
      ziel.open = true;
    }} else {{
      // Ganze Themengruppe: alle enthaltenen Themen aufklappen
      ziel.querySelectorAll("details.thema").forEach(function(d){{ d.open = true; }});
    }}
    ziel.scrollIntoView({{behavior:"smooth", block:"start"}});
  }}

  // Sprungmenü (Auswahlliste)
  var sprung = document.getElementById("themaSprung");
  sprung.addEventListener("change", function(){{
    if (sprung.value) {{
      themaOeffnen(sprung.value);
      sprung.selectedIndex = 0;
      sprung.blur();
    }}
  }});

  // Themenliste & interne Anker
  document.querySelectorAll('a[href^="#thema-"]').forEach(function(a){{
    a.addEventListener("click", function(ev){{
      ev.preventDefault();
      themaOeffnen(a.getAttribute("href").slice(1));
    }});
  }});

  // ----- Suche -----
  function suchen(){{
    var q = suchEingabe.value.trim().toLowerCase();
    var treffer = 0;
    themen.forEach(function(t){{
      var passt = !q || (t.dataset.suche || "").indexOf(q) !== -1;
      t.style.display = passt ? "" : "none";
      if (passt) treffer++;
      if (q && passt) t.open = true;
    }});
    gruppen.forEach(function(g){{
      var sichtbar = false;
      g.querySelectorAll(".thema").forEach(function(t){{
        if (t.style.display !== "none") sichtbar = true;
      }});
      g.style.display = sichtbar ? "" : "none";
    }});
    keinTreffer.style.display = (q && treffer === 0) ? "block" : "none";
  }}
  suchEingabe.addEventListener("input", suchen);

  // ----- Alle öffnen/schließen -----
  document.getElementById("alleAuf").addEventListener("click", function(){{
    themen.forEach(function(t){{ t.open = true; }});
  }});
  document.getElementById("alleZu").addEventListener("click", function(){{
    themen.forEach(function(t){{ t.open = false; }});
  }});

  // ----- Druck: alles aufklappen -----
  window.addEventListener("beforeprint", function(){{
    themen.forEach(function(t){{ t.open = true; }});
  }});

  // ----- Nach-oben-Knopf -----
  var nachOben = document.getElementById("nachOben");
  window.addEventListener("scroll", function(){{
    nachOben.style.display = window.scrollY > 700 ? "block" : "none";
  }}, {{passive:true}});
  nachOben.addEventListener("click", function(){{
    window.scrollTo({{top:0, behavior:"smooth"}});
  }});

  // ----- PC → Handy: Telefonnummern als QR-Code übertragen -----
  // Auf Geräten ohne Telefonfunktion öffnet ein Klick auf eine Nummer
  // einen QR-Code, den man mit der Handykamera scannt.
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

  function nummerFormatieren(tel){{
    return tel.length <= 5 ? tel : tel.replace(/(\\d{{3,4}})(?=(\\d{{4}})+$)/g, "$1 ");
  }}

  function qrZeigen(tel){{
    var eintrag = QR[tel];
    if (!eintrag) return false;
    document.getElementById("qrCode").innerHTML = qrAlsSvg(eintrag);
    document.getElementById("qrNummer").textContent = nummerFormatieren(tel);
    document.getElementById("qrAnrufen").setAttribute("href", "tel:" + tel);
    var kopieren = document.getElementById("qrKopieren");
    kopieren.textContent = "Nummer kopieren";
    kopieren.dataset.tel = tel;
    qrDialog.showModal();
    return true;
  }}

  if (qrDialog && typeof qrDialog.showModal === "function") {{
    document.addEventListener("click", function(ev){{
      if (!istDesktop) return;
      var a = ev.target.closest ? ev.target.closest('a[href^="tel:"]') : null;
      if (!a || a.classList.contains("no-qr")) return;
      var tel = a.getAttribute("href").slice(4);
      if (qrZeigen(tel)) ev.preventDefault();
    }});
    document.getElementById("qrZu").addEventListener("click", function(){{
      qrDialog.close();
    }});
    qrDialog.addEventListener("click", function(ev){{
      if (ev.target === qrDialog) qrDialog.close();  // Klick auf den Hintergrund
    }});
    document.getElementById("qrAnrufen").addEventListener("click", function(){{
      qrDialog.close();
    }});
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

  // ----- Startbildschirm (Handy): Land wählen, dann schnelle Hilfe -----
  var startDialog = document.getElementById("startDialog");
  var istMobil = window.matchMedia("(max-width: 820px)").matches;
  var LANDNAME = {{de:"Deutschland", at:"Österreich", ch:"Schweiz", alle:"Alle Länder"}};

  function startSchritt2(){{
    var chip = document.getElementById("startLandChip");
    var flagge = (aktivesLand === "alle") ? "" : FLAGGE[aktivesLand] + " ";
    chip.textContent = flagge + LANDNAME[aktivesLand] + "  ·  ändern";
    document.getElementById("startSchritt1").hidden = true;
    document.getElementById("startSchritt2").hidden = false;
  }}
  function startSchritt1(){{
    document.getElementById("startSchritt2").hidden = true;
    document.getElementById("startSchritt1").hidden = false;
  }}

  if (startDialog && typeof startDialog.showModal === "function" && istMobil) {{
    var gemerkt = gemerktesLand();
    if (gemerkt && LANDNAME[gemerkt]) {{
      landSetzen(gemerkt);
      startSchritt2();  // Land ist bekannt – direkt zur schnellen Hilfe
    }}
    startDialog.showModal();

    startDialog.querySelectorAll(".start-land").forEach(function(knopf){{
      knopf.addEventListener("click", function(){{
        landSetzen(knopf.dataset.land);
        landMerken(knopf.dataset.land);
        startSchritt2();
      }});
    }});
    document.getElementById("startLandChip").addEventListener("click", startSchritt1);
    document.getElementById("startWeiter1").addEventListener("click", function(){{
      startDialog.close();
    }});
    startDialog.querySelectorAll(".start-punkt").forEach(function(knopf){{
      knopf.addEventListener("click", function(){{
        startDialog.close();
        setTimeout(function(){{ themaOeffnen(knopf.dataset.ziel); }}, 60);
      }});
    }});
    document.getElementById("startUebersicht").addEventListener("click", function(){{
      startDialog.close();
    }});
    document.getElementById("startZu").addEventListener("click", function(){{
      startDialog.close();
    }});
    startDialog.addEventListener("click", function(ev){{
      if (ev.target === startDialog) startDialog.close();
    }});
  }}

  schnellwahlAktualisieren();
}})();
</script>
</body>
</html>
'''

page = page.replace("__QRDATEN__", QRDATEN)
ziel = AUSGABE / 'index.html'
ziel.write_text(page, encoding='utf-8')
print("Hilfeseite gebaut:", ziel, "|", len(page)//1024, "KB")
