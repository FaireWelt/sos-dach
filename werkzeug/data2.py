# -*- coding: utf-8 -*-
from data import E

GROUPS2 = [
 {"id":"gesundheit","icon":"🏥","title":"Gesundheit & Erkrankungen","topics":[

  {"id":"hiv","icon":"🎗️","title":"Hilfe bei HIV und AIDS","entries":{
   "DE":[E("Deutsche Aidshilfe",[("030 69 00 87 0","0306900870")],"Beratung und Unterstützung für Menschen mit HIV und AIDS","www.aidshilfe.de")],
   "AT":[E("Aids Hilfe Wien",[("01 599 37 0","01599370")],"Beratung und Unterstützung für Menschen mit HIV und AIDS","www.aids.at")],
   "CH":[E("Aids-Hilfe Schweiz",[("031 390 60 00","0313906000")],"Beratung und Unterstützung für Menschen mit HIV und AIDS","www.aids.ch")]}},

  {"id":"hepatitis","icon":"🫁","title":"Hilfe bei Hepatitis","entries":{
   "DE":[E("Deutsche Leberhilfe e. V.",[("0221 282 99 99","02212829999")],"Beratung und Unterstützung für Menschen mit Hepatitis","www.leberhilfe.org")],
   "AT":[E("Österr. Gesellschaft für Gastroenterologie und Hepatologie",[("01 405 13 83","014051383")],"Fachinformationen zu Lebererkrankungen","www.oeggh.at")],
   "CH":[E("Hepatitis Schweiz",[("044 383 99 00","0443839900")],"Beratung und Unterstützung für Menschen mit Hepatitis","www.hepatitis-schweiz.ch")]}},

  {"id":"krebs","icon":"🩺","title":"Hilfe bei Krebs","entries":{
   "DE":[E("Deutsche Krebshilfe – INFONETZ KREBS",[("0800 80 70 88 77","08008070887 7".replace(" ",""))],"Beratung und Unterstützung für Krebspatienten und Angehörige","www.krebshilfe.de")],
   "AT":[E("Österreichische Krebshilfe",[("0800 699 900","0800699900")],"Beratung und Unterstützung für Krebspatienten und Angehörige","www.krebshilfe.net")],
   "CH":[E("Krebsliga Schweiz – Krebstelefon",[("0800 11 88 11","0800118811")],"Beratung und Unterstützung für Krebspatienten und Angehörige","www.krebsliga.ch")]}},

  {"id":"sucht","icon":"🚭","title":"Suchtberatung","entries":{
   "DE":[E("BZgA-Infotelefon zur Suchtvorbeugung",[("0221 89 20 31","02218920 31".replace(" ",""))],"Beratung zu Alkohol-, Drogen-, Spiel- und Internetsucht","www.bzga.de"),
        E("Sucht & Drogen Hotline",[("01806 313 031","01806313031")],"Telefonberatung rund um die Uhr (kostenpflichtig: 20 ct/Anruf Festnetz)","www.sucht-und-drogen-hotline.de")],
   "AT":[E("Drogenberatung – Sucht- und Drogenkoordination Wien",[("01 4000 53 660","01400053660")],"Beratung für Betroffene und Angehörige bei Suchtproblemen","www.sdw.wien")],
   "CH":[E("Sucht Schweiz",[("021 321 29 00","0213212900")],"Beratung und Unterstützung bei Suchtproblemen","www.suchtschweiz.ch")]}},

  {"id":"palliativ","icon":"🕊️","title":"Palliativversorgung & Hospizhilfe","entries":{
   "DE":[E("Deutscher Hospiz- und PalliativVerband",[("030 820 97 110","03082097110")],"Informationen zu Hospizen, ambulanter Palliativversorgung & Sterbebegleitung","www.dhpv.de","@dhpv_ev")],
   "AT":[E("Hospiz Österreich",[("01 513 88 40","015138840")],"Beratung & Begleitung für schwerkranke Menschen und Angehörige","www.hospiz.at","@hospiz_oesterreich")],
   "CH":[E("palliative ch",[("031 311 41 11","0313114111")],"Dachverband für Palliative Care in der Schweiz","www.palliative.ch","@palliative_ch")]}},

  {"id":"pflege","icon":"🧓","title":"Pflege & Demenzhilfe","entries":{
   "DE":[E("compass Pflegeberatung",[("0800 101 88 00","08001018800")],"Kostenfreie Beratung zu Pflegeleistungen & Angehörigenhilfe","www.pflegeberatung.de"),
        E("Pflegetelefon des Bundesfamilienministeriums",[("030 20 17 91 31","0302017913 1".replace(" ",""))],"Unterstützung für pflegende Angehörige","www.wege-zur-pflege.de"),
        E("Alzheimer-Telefon",[("030 259 37 95 14","030259379514")],"Beratung bei Demenz für Betroffene und Angehörige","www.deutsche-alzheimer.de")],
   "AT":[E("Volkshilfe Demenzhilfe",[("01 402 62 09","014026209")],"Beratung, Betreuung & finanzielle Hilfe bei Demenz","www.demenz-hilfe.at","@volkshilfe.at"),
        E("Pflegeberatung Sozialministeriumservice",[("05 99 88","059988")],"Informationen zu Pflegegeld & Unterstützungsleistungen","www.sozialministeriumservice.at")],
   "CH":[E("Pro Senectute",[("058 591 15 15","0585911515")],"Beratung für ältere Menschen & pflegende Angehörige","www.prosenectute.ch","@prosenectute"),
        E("Alzheimer Schweiz",[("058 058 80 00","0580588000")],"Information & Unterstützung bei Demenz","www.alz.ch","@alzheimerschweiz")]}},

  {"id":"pflegeausland","icon":"🌍","title":"Pflege im Ausland & grenzüberschreitende Hilfe","entries":{
   "DE":[E("Deutsche im Ausland e. V.",[],"Infos zur Pflegeversicherung bei Wohnsitz im Ausland","www.deutsche-im-ausland.org","@deutscheimausland")],
   "AT":[E("Sozialministeriumservice",[("05 99 88","059988")],"Beratung zu Pflegegeld & Pflege im Ausland","www.sozialministeriumservice.at")],
   "CH":[E("Pflegewegweiser Schweiz",[],"Informationen zu Pflegeleistungen, Betreuungsgutschriften & Spitex","www.pflegewegweiser.ch")]}},
 ]},

 {"id":"soziales","icon":"🫂","title":"Leben, Recht & Soziales","topics":[

  {"id":"arbeitslos","icon":"💶","title":"Arbeitslosigkeit & soziale Notlagen","entries":{
   "DE":[E("Caritas Sozialberatung",[("0800 025 025 0","08000250250")],"Beratung für Menschen in finanziellen Schwierigkeiten und Arbeitslosigkeit","www.caritas.de")],
   "AT":[E("Sozialberatung der Volkshilfe",[("01 360 64 0","0136064 0".replace(" ",""))],"Unterstützung für Menschen in sozialen Notlagen","www.volkshilfe.at")],
   "CH":[E("Caritas Schweiz",[("041 419 22 22","0414192222")],"Beratung für Menschen in finanziellen Schwierigkeiten und Arbeitslosigkeit","www.caritas.ch")]}},

  {"id":"recht","icon":"📜","title":"Rechtliche Beratung bei Diskriminierung","entries":{
   "DE":[E("Antidiskriminierungsstelle des Bundes",[("030 18555 1855","030185551855")],"Beratung bei Diskriminierung und rechtlichen Fragen","www.antidiskriminierungsstelle.de")],
   "AT":[E("ZARA – Zivilcourage und Anti-Rassismus-Arbeit",[("01 929 98 99","019299899")],"Beratung bei Diskriminierung und rechtlichen Fragen","www.zara.or.at")],
   "CH":[E("humanrights.ch",[("031 390 60 00","0313906000")],"Beratung bei Diskriminierung und rechtlichen Fragen","www.humanrights.ch")]}},

  {"id":"senioren","icon":"👵","title":"Für Senior:innen & bei Einsamkeit","entries":{
   "DE":[E("Silbernetz",[("0800 4 70 80 90","0800470809 0".replace(" ",""))],"Telefon gegen Einsamkeit im Alter – täglich 8 bis 22 Uhr","www.silbernetz.org","@silbernetz")],
   "AT":[E("Plaudernetz",[("05 1776 100","051776100")],"Telefonische Gespräche gegen Einsamkeit","www.plaudernetz.at","@plaudernetz")],
   "CH":[E("Pro Senectute",[("058 591 15 15","0585911515")],"Beratung und Unterstützung für ältere Menschen","www.prosenectute.ch","@prosenectute")]}},

  {"id":"migration","icon":"🕊️","title":"Migration, Flucht & Integration","entries":{
   "DE":[E("Pro Asyl",[("069 242 314 20","06924231420")],"Rechtsberatung und Unterstützung für Geflüchtete","www.proasyl.de","@pro_asyl")],
   "AT":[E("asylkoordination österreich",[("01 524 30 70","015243070")],"Informationen und Hilfe für Geflüchtete","www.asyl.at","@asylkoordination")],
   "CH":[E("Schweizerische Flüchtlingshilfe",[("031 370 75 75","0313707575")],"Beratung und Unterstützung für Asylsuchende","www.fluechtlingshilfe.ch","@fluechtlingshilfe")]}},
 ]},

 {"id":"weitere","icon":"☎️","title":"Weitere wichtige Rufnummern","topics":[

  {"id":"gift","icon":"☠️","title":"Giftnotruf","entries":{
   "DE":[E("Giftnotruf Berlin",[("030 19240","03019240")],"Rund um die Uhr bei Vergiftungen","www.giftnotruf.charite.de"),
        E("Giftnotruf München",[("089 19240","08919240")],"Rund um die Uhr bei Vergiftungen","www.toxikologie.mri.tum.de")],
   "AT":[E("Vergiftungsinformationszentrale",[("01 406 43 43","014064343")],"Rund um die Uhr bei Vergiftungen","www.goeg.at/VIZ")],
   "CH":[E("Tox Info Suisse",[("145","145")],"Rund um die Uhr bei Vergiftungen","www.toxinfo.ch")]}},

  {"id":"tauchen","icon":"🤿","title":"Taucher-Notruf & Druckkammern","entries":{
   "DE":[E("DAN Europe / aqua med Taucher-Notruf",[("0700 34 83 54 63","070034835463")],"Internationale Notrufnummer für Tauchunfälle")],
   "AT":[E("Druckkammer Wien – Arbeiter-Samariter-Bund",[("01 914 47 00","019144700")],""),
        E("AKH Wien – Tauchmedizinischer Notruf",[("01 40400 1001","01404001001")],"")],
   "CH":[E("Druckkammer Zürich",[("044 387 87 87","0443878787")],"")]}},

  {"id":"panne","icon":"🚗","title":"Autopannenhilfe","entries":{
   "DE":[E("ADAC-Pannenhilfe",[("089 20 20 40 00","0892020400 0".replace(" ",""))],"Pannen- und Unfallhilfe rund um die Uhr","www.adac.de")],
   "AT":[E("ÖAMTC-Nothilfe",[("120","120")],"Pannenhilfe rund um die Uhr","www.oeamtc.at")],
   "CH":[E("TCS-Pannenhilfe",[("0800 140 140","0800140140")],"Pannenhilfe rund um die Uhr","www.tcs.ch")]}},

  {"id":"barrierefrei","icon":"🦻","title":"Notruf ohne Sprechen (für gehörlose Menschen)","entries":{
   "DE":[E("nora Notruf-App",[],"Offizielle Notruf-App der Bundesländer – erreicht Polizei, Feuerwehr und Rettung per App","www.nora-notruf.de"),
        E("Notruf-Fax",[],"Notruf-Fax an 112 ist bundesweit möglich – Vorlagen bei der örtlichen Feuerwehr")],
   "AT":[E("Gehörlosennotruf per SMS/Fax",[("0800 133 133","0800133133")],"SMS oder Fax an 0800 133 133 erreicht die Polizei-Notrufzentrale"),
        E("DEC112-App",[],"Barrierefreier Notruf per Chat-App","www.dec112.at")],
   "CH":[E("procom SMS-Notruf",[],"Notruf-Vermittlung für gehörlose Menschen per SMS und App","www.procom-deaf.ch")]}},
 ]},
]
