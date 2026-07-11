# -*- coding: utf-8 -*-
# Alle Hilfethemen der FaireWelt-Hilfeseite.
# E = Eintrag: (name, [(nummer_anzeige, nummer_tel), ...], beschreibung, web, insta, extra)

def E(name, phones=None, desc="", web=None, insta=None, extra=None):
    return {"name": name, "phones": phones or [], "desc": desc,
            "web": web, "insta": insta, "extra": extra}

GROUPS = [
 {"id":"notfall","icon":"🚨","title":"Notfall & Sicherheit","topics":[

  {"id":"notruf","icon":"📟","title":"Allgemeine Notrufnummern","entries":{
   "DE":[E("Feuerwehr & Rettungsdienst",[("112","112")],"Bei Feuer und medizinischen Notfällen – kostenlos, rund um die Uhr"),
        E("Polizei",[("110","110")],"Bei Straftaten und Gefahrensituationen"),
        E("Ärztlicher Bereitschaftsdienst",[("116 117","116117")],"Wenn es dringend ist, aber kein Notfall – auch online","www.116117.de"),
        E("nora Notruf-App",[],"Offizielle Notruf-App der Bundesländer – Notruf ohne Sprechen, z. B. für gehörlose Menschen oder in Bedrohungslagen","www.nora-notruf.de")],
   "AT":[E("Euronotruf",[("112","112")],"EU-weiter Notruf – funktioniert auch mit Handy ohne SIM-Empfang des eigenen Netzes"),
        E("Feuerwehr",[("122","122")],""),
        E("Polizei",[("133","133")],""),
        E("Rettung",[("144","144")],""),
        E("Ärztenotdienst",[("141","141")],"Ärztlicher Bereitschaftsdienst außerhalb der Ordinationszeiten"),
        E("Gesundheitsberatung",[("1450","1450")],"Telefonische Gesundheitsberatung: „Wie krank bin ich?“","www.1450.at"),
        E("Alpinnotruf / Bergrettung",[("140","140")],"")],
   "CH":[E("Euronotruf",[("112","112")],"EU-weiter Notruf – wird an die zuständige Zentrale weitergeleitet"),
        E("Polizei",[("117","117")],""),
        E("Feuerwehr",[("118","118")],""),
        E("Sanität / Rettung",[("144","144")],""),
        E("Rega – Rettungshelikopter",[("1414","1414")],"Schweizerische Rettungsflugwacht","www.rega.ch")]}},

  {"id":"signal","icon":"✋","title":"WICHTIGE INFO! Signal for Help","special":"signal","entries":{}},

  {"id":"heimweg","icon":"🧭","title":"Heimwegtelefon & Begleitung","entries":{
   "DE":[E("Heimwegtelefon Deutschland",[("030 12074182","03012074182")],"Telefonische Begleitung auf dem Heimweg – damit Du Dich sicherer fühlst","www.heimwegtelefon.net","@heimwegtelefon")],
   "AT":[E("Heimwegtelefon Graz",[("0316 872 2200","03168722200")],"Telefonische Begleitung für Graz und Umgebung","www.graz.at/heimwegtelefon","@heimwegtelefon_graz","App: „Heimweg-App Graz“")],
   "CH":[E("Heimweghilfe per App",[],"Digitale Begleitung und Notfallfunktionen, z. B. mit „WayGuard“ oder „SafeNow“ – die Polizei empfiehlt Wachsamkeit & Sicherheits-Apps","www.wayguard.de / www.safenow.app")]}},

  {"id":"aufdringlich","icon":"📵","title":"Hilfe gegen aufdringliche Personen","entries":{
   "DE":[E("NoAnrufe.de – Nummer ohne Anruf",[("0157 5302 4990","015753024990")],"Gib diese Nummer weiter, wenn Du Dich unwohl fühlst – die andere Person erhält eine Info-Nachricht statt Dich zu erreichen","www.noanruf.de","@noanruf.de")],
   "AT":[E("Kein offizielles Angebot",[],"Alternative: Heimwegtelefon Graz oder Apps wie „WayGuard“")],
   "CH":[E("Kein offizielles Angebot",[],"Alternative: Sicherheits-Apps wie „WayGuard“ oder „SafeNow“")]}},
 ]},

 {"id":"seele","icon":"💜","title":"Seelische Gesundheit & Krisen","topics":[

  {"id":"seelsorge","icon":"📞","title":"Allgemeine Telefonseelsorge","entries":{
   "DE":[E("TelefonSeelsorge",[("0800 111 0 111","08001110111"),("0800 111 0 222","08001110222"),("116 123","116123")],"Rund um die Uhr erreichbar, anonym und kostenlos – bei persönlichen Krisen, Ängsten und Sorgen. Auch Chat- und Mailberatung möglich","www.telefonseelsorge.de","@telefonseelsorge")],
   "AT":[E("TelefonSeelsorge",[("142","142")],"Rund um die Uhr erreichbar, anonym und kostenlos – Unterstützung bei persönlichen Krisen","www.telefonseelsorge.at","@telefonseelsorge.at")],
   "CH":[E("Die Dargebotene Hand",[("143","143")],"Rund um die Uhr erreichbar, anonym und kostenlos – Unterstützung bei persönlichen Krisen","www.143.ch","@dargebotenehand")]}},

  {"id":"suizid","icon":"🕯️","title":"Suizidprävention & Krisenhilfe","entries":{
   "DE":[E("TelefonSeelsorge",[("0800 111 0 111","08001110111")],"Rund um die Uhr erreichbar bei Krisen & Suizidgedanken","www.telefonseelsorge.de","@telefonseelsorge"),
        E("krisenchat",[],"Kostenlose 24/7-Krisenberatung per WhatsApp & SMS für alle unter 25","www.krisenchat.de","@krisenchat"),
        E("[U25] Deutschland",[],"Onlineberatung von jungen Menschen für junge Menschen in Krisen","www.u25-deutschland.de"),
        E("NaSPro – Nationales Suizidpräventionsprogramm",[],"Fachnetzwerk & Aufklärung zur Suizidvermeidung","www.suizidpraevention.de")],
   "AT":[E("Kriseninterventionszentrum Wien",[("01 406 95 95","014069595")],"Akuthilfe bei psychischen Krisen","www.kriseninterventionszentrum.at"),
        E("SUPRA – Suizidprävention Austria",[],"Koordinationsstelle & Aktionsplan zur Suizidvermeidung","www.sozialministerium.gv.at")],
   "CH":[E("Die Dargebotene Hand",[("143","143")],"Anonyme Hilfe bei Suizidgedanken","www.143.ch","@dargebotenehand"),
        E("Reden kann retten",[],"Kampagne zur Suizidprävention & Enttabuisierung","www.reden-kann-retten.ch")]}},

  {"id":"psyche","icon":"🧠","title":"Psychische Gesundheit","entries":{
   "DE":[E("Info-Telefon Deutsche Depressionshilfe",[("0800 33 44 533","08003344533")],"Beratung bei Depressionen und psychischen Belastungen","www.deutsche-depressionshilfe.de","@depressionshilfe")],
   "AT":[E("TelefonSeelsorge Österreich",[("142","142")],"Rund-um-die-Uhr-Hilfe bei seelischen Krisen","www.telefonseelsorge.at","@telefonseelsorge.at")],
   "CH":[E("Die Dargebotene Hand",[("143","143")],"Anonyme Hilfe bei psychischen Belastungen","www.143.ch","@dargebotenehand")]}},

  {"id":"trauer","icon":"🌫️","title":"Trauer & Verlust","entries":{
   "DE":[E("Caritas Trauerberatung",[("0800 111 0 111","08001110111")],"Online- und Telefonberatung bei Trauerfällen","www.caritas.de/trauerberatung","@caritasdeutschland")],
   "AT":[E("Trauerhilfe Oberösterreich",[("142","142")],"Begleitung durch Trauergruppen und Seelsorge (über die TelefonSeelsorge)","www.dioezese-linz.at/trauerhilfe","@telefonseelsorge.at")],
   "CH":[E("Trauerbegleitung Dargebotene Hand",[("143","143")],"Anonyme Hilfe bei Trauer und Verlust","www.143.ch","@dargebotenehand")]}},

  {"id":"selbsthilfe","icon":"🤲","title":"Selbsthilfegruppen & Angehörige","entries":{
   "DE":[E("NAKOS",[("030 31 01 89 60","0303101896 0".replace(" ",""))],"Nationale Kontakt- und Informationsstelle zur Anregung und Unterstützung von Selbsthilfegruppen","www.nakos.de","@nakos_de")],
   "AT":[E("Selbsthilfe Österreich",[("01 892 38 84","018923884")],"Vernetzung & Unterstützung von Selbsthilfegruppen","www.selbsthilfe.at","@selbsthilfe_oesterreich")],
   "CH":[E("Selbsthilfe Schweiz",[("031 370 70 20","0313707020")],"Plattform für Selbsthilfegruppen & Angehörigenberatung","www.selbsthilfeschweiz.ch","@selbsthilfe_ch")]}},
 ]},

 {"id":"familie","icon":"👨‍👩‍👧","title":"Kinder, Jugend & Familie","topics":[

  {"id":"kinder","icon":"🧒","title":"Hilfe für Kinder und Jugendliche","entries":{
   "DE":[E("Nummer gegen Kummer",[("116 111","116111")],"Beratung für Kinder und Jugendliche bei Problemen in Schule, Familie oder persönlichen Krisen – kostenlos und anonym","www.nummergegenkummer.de","@nummergegenkummer"),
        E("krisenchat",[],"24/7-Hilfe per WhatsApp & SMS für junge Menschen unter 25 – schreiben statt anrufen","www.krisenchat.de","@krisenchat"),
        E("Hotline für vermisste Kinder",[("116 000","116000")],"EU-weite Hotline bei Vermisstenfällen","www.initiative-vermisste-kinder.de")],
   "AT":[E("Rat auf Draht",[("147","147")],"Beratung für Kinder und Jugendliche – kostenlos, anonym, rund um die Uhr","www.rataufdraht.at","@rat.auf.draht")],
   "CH":[E("Pro Juventute Beratung",[("147","147")],"Beratung für Kinder und Jugendliche – kostenlos, anonym, rund um die Uhr","www.147.ch")]}},

  {"id":"eltern","icon":"🍼","title":"Hilfe für Eltern","entries":{
   "DE":[E("Elterntelefon",[("0800 111 0 550","08001110550")],"Beratung für Eltern in Erziehungsfragen – kostenlos und anonym","www.nummergegenkummer.de")],
   "AT":[E("Elternberatung",[("0800 511 511","0800511511")],"Beratung für Eltern in Erziehungsfragen – kostenlos und anonym","www.elternberatung.at")],
   "CH":[E("Elternnotruf",[("0848 35 45 55","0848354555")],"Beratung für Eltern in Erziehungsfragen – rund um die Uhr","www.elternnotruf.ch")]}},

  {"id":"schwanger","icon":"🤰","title":"Hilfe für Schwangere","entries":{
   "DE":[E("Hilfetelefon „Schwangere in Not“",[("0800 40 40 020","08004040020")],"Beratung für Schwangere in schwierigen Situationen – kostenlos, anonym, rund um die Uhr","www.schwanger-und-viele-fragen.de")],
   "AT":[E("Beratung für Schwangere",[("0800 310 013","0800310013")],"Unterstützung für werdende Mütter – kostenlos und anonym","www.schwanger.at")],
   "CH":[E("Beratung für Schwangere",[("0848 85 86 87","0848858687")],"Unterstützung für werdende Mütter – kostenlos und anonym","www.schwanger.ch")]}},

  {"id":"paare","icon":"💞","title":"Familien- & Paarberatung","entries":{
   "DE":[E("Pro Familia",[("069 900 29 60","0699002960")],"Beratung zu Partnerschaft, Familie und Sexualität","www.profamilia.de")],
   "AT":[E("Familienberatung Österreich",[("0800 240 262","0800240262")],"Beratung für Paare und Familien in Krisen","www.familienberatung.gv.at")],
   "CH":[E("Paarberatung & Mediation Schweiz",[("044 261 61 61","0442616161")],"Beratung für Paare und Familien","www.paarberatung.ch")]}},

  {"id":"schule","icon":"🎒","title":"Schulberatung & Mobbinghilfe","entries":{
   "DE":[E("Nummer gegen Kummer",[("116 111","116111"),("0800 111 0 550","08001110550")],"Beratung bei Schulstress, Mobbing & Prüfungsangst – 116 111 für Kinder, 0800 111 0 550 für Eltern","www.nummergegenkummer.de","@nummergegenkummer")],
   "AT":[E("Rat auf Draht",[("147","147")],"Hilfe bei Schulproblemen & Mobbing","www.rataufdraht.at","@rat.auf.draht")],
   "CH":[E("Pro Juventute",[("147","147")],"Beratung für Kinder & Jugendliche bei Schulstress","www.projuventute.ch","@projuventute")]}},
 ]},

 {"id":"gewalt","icon":"🛡️","title":"Gewalt, Missbrauch & Schutz","topics":[

  {"id":"missbrauch","icon":"🚫","title":"Hilfe bei sexuellem Missbrauch","entries":{
   "DE":[E("Hilfetelefon Sexueller Missbrauch",[("0800 22 55 530","08002255530")],"Kostenlose und anonyme Beratung für Betroffene und Angehörige","www.hilfe-telefon-missbrauch.de"),
        E("Nummer gegen Kummer",[("116 111","116111")],"Beratung für Kinder und Jugendliche","www.nummergegenkummer.de"),
        E("Weitere Frauennotrufe",[],"Übersicht regionaler Notrufe für Frauen","www.feminy.de/frauennotrufe")],
   "AT":[E("Frauenhelpline gegen Gewalt",[("0800 222 555","0800222555")],"Rund um die Uhr erreichbar","www.frauenhelpline.at"),
        E("Notruf für vergewaltigte Frauen und Mädchen",[("01 523 22 22","015232222")],"Beratung rund um die Uhr")],
   "CH":[E("Opferhilfe Schweiz",[("0848 86 86 86","0848868686")],"Unterstützung für Opfer von Gewalt","www.opferhilfe-schweiz.ch")]}},

  {"id":"frauen","icon":"♀️","title":"Gewalt gegen Frauen","entries":{
   "DE":[E("Hilfetelefon „Gewalt gegen Frauen“",[("116 016","116016"),("08000 116 016","08000116016")],"Beratung für Frauen, die von Gewalt betroffen sind – kostenlos, anonym, rund um die Uhr, in 18 Sprachen. Auch Chat- und Mailberatung","www.hilfetelefon.de")],
   "AT":[E("Frauenhelpline",[("0800 222 555","0800222555")],"Beratung für Frauen, die von Gewalt betroffen sind – kostenlos und anonym","www.frauenhelpline.at")],
   "CH":[E("Opferhilfe",[("0848 86 86 86","0848868686")],"Unterstützung für Opfer von Gewalt – kostenlos und anonym","www.opferhilfe-schweiz.ch")]}},

  {"id":"maenner","icon":"♂️","title":"Gewalt gegen Männer","entries":{
   "DE":[E("Hilfetelefon Gewalt an Männern",[("0800 123 99 00","08001239900")],"Beratung für Männer, die von Gewalt betroffen sind – kostenlos und anonym","www.maennerhilfetelefon.de")],
   "AT":[E("Männerberatung / Männerinfo",[("0800 400 777","0800400777")],"Beratung für Männer, die von Gewalt betroffen sind – kostenlos und anonym","www.maennerinfo.at")],
   "CH":[E("Männernotruf Zürich",[("044 364 00 00","0443640000")],"Beratung für Männer, die von Gewalt betroffen sind","www.maennernotruf.ch")]}},

  {"id":"opfer","icon":"⚖️","title":"Opferhilfe nach Straftaten","entries":{
   "DE":[E("WEISSER RING – Opfer-Telefon",[("116 006","116006")],"Hilfe für Opfer von Straftaten – kostenlos und anonym, täglich","www.weisser-ring.de")],
   "AT":[E("Opfer-Notruf (Weisser Ring Österreich)",[("0800 112 112","0800112112")],"Kostenlose Hilfe für Opfer von Straftaten – rund um die Uhr","www.opfer-notruf.at")],
   "CH":[E("Opferhilfe Schweiz",[("0848 86 86 86","0848868686")],"Beratungsstellen in allen Kantonen","www.opferhilfe-schweiz.ch")]}},

  {"id":"hass","icon":"🤝","title":"Hass, Mobbing, Rassismus & Diskriminierung","entries":{
   "DE":[E("Nummer gegen Kummer",[("116 111","116111")],"Beratung für Betroffene von Mobbing und Hass – kostenlos und anonym","www.nummergegenkummer.de"),
        E("Antidiskriminierungsstelle des Bundes",[("030 18555 1855","030185551855")],"Unterstützung bei Diskriminierung und Rassismus","www.antidiskriminierungsstelle.de")],
   "AT":[E("ZARA – Zivilcourage und Anti-Rassismus-Arbeit",[("01 929 98 99","019299899")],"Unterstützung bei Diskriminierung und Rassismus","www.zara.or.at")],
   "CH":[E("humanrights.ch",[],"Beratung gegen Diskriminierung und Rassismus","www.humanrights.ch")]}},
 ]},

 {"id":"vielfalt","icon":"🌈","title":"Vielfalt & Inklusion","topics":[

  {"id":"lgbtq","icon":"🏳️‍🌈","title":"Unterstützung für LGBTQIA+","entries":{
   "DE":[E("Lesben- und Schwulenverband Deutschland (LSVD⁺)",[("030 22 50 22 10","0302250221 0".replace(" ",""))],"Beratung und Unterstützung für LGBTQ+ Personen","www.lsvd.de")],
   "AT":[E("Queerbase",[("01 4000 83060","01400083060")],"Beratung für LGBTQ+ Geflüchtete und Menschen in Not","www.queerbase.at")],
   "CH":[E("Pink Cross",[("031 372 33 00","0313723300")],"Schweizer Dachverband der Schwulen mit Beratungsangeboten","www.pinkcross.ch")]}},

  {"id":"autismus","icon":"🧩","title":"Hilfe bei Autismus","entries":{
   "DE":[E("autismus Deutschland e. V.",[("030 831 90 96","0308319096")],"Beratung und Unterstützung für Menschen mit Autismus und deren Angehörige","www.autismus.de")],
   "AT":[E("Österreichische Autistenhilfe",[("01 789 26 42","017892642")],"Beratung und Unterstützung für Menschen mit Autismus","www.autistenhilfe.at")],
   "CH":[E("autismus schweiz",[("031 385 33 33","0313853333")],"Beratung und Unterstützung für Menschen mit Autismus","www.autismus.ch")]}},

  {"id":"adhs","icon":"⚡","title":"Hilfe bei ADHS & Neurodiversität","entries":{
   "DE":[E("ADHS Deutschland e. V.",[("030 85 65 67 00","0308565670 0".replace(" ",""))],"Selbsthilfegruppen & Beratung für ADHS-Betroffene","www.adhs-deutschland.de","@adhs_deutschland")],
   "AT":[E("ADAPT",[("0660 580 80 51","06605808051")],"Selbsthilfegruppen & Therapiestellen für ADHS","www.adapt.at","@adhs_family")],
   "CH":[E("elpos Schweiz",[("044 940 99 10","0449409910")],"Beratung & Unterstützung bei ADHS","www.elpos.ch","@elpos_schweiz")]}},

  {"id":"behinderung","icon":"♿","title":"Beratung für Menschen mit Behinderungen","entries":{
   "DE":[E("Lebenshilfe",[("030 82 99 32 0","0308299320")],"Beratung und Unterstützung für Menschen mit Behinderungen und deren Angehörige","www.lebenshilfe.de")],
   "AT":[E("Österreichischer Behindertenrat",[("01 513 15 35","015131535")],"Beratung und Unterstützung für Menschen mit Behinderungen","www.behindertenrat.at")],
   "CH":[E("Pro Infirmis",[("058 775 20 00","0587752000")],"Beratung und Unterstützung für Menschen mit Behinderungen","www.proinfirmis.ch")]}},
 ]},
]
