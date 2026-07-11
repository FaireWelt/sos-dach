# -*- coding: utf-8 -*-
"""Verschlüsselt den bürgerlichen Namen für die geschützte Anzeige im Impressum.

Aufruf:  python3 name_verschluesseln.py "Vor- und Nachname" "Passwort"

Erzeugt name_geschuetzt.json (AES-256-GCM, Schlüssel per PBKDF2-SHA256 aus dem
Passwort abgeleitet). Ohne das Passwort ist der Name auch im Quelltext der
fertigen Seite nicht lesbar. Nach jeder Änderung build_impressum.py neu ausführen.
"""
import base64
import hashlib
import json
import os
import sys
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

ITERATIONEN = 600_000

def verschluesseln(name: str, passwort: str) -> dict:
    salt = os.urandom(16)
    iv = os.urandom(12)
    schluessel = hashlib.pbkdf2_hmac("sha256", passwort.encode("utf-8"),
                                     salt, ITERATIONEN, dklen=32)
    ct = AESGCM(schluessel).encrypt(iv, name.encode("utf-8"), None)
    b64 = lambda b: base64.b64encode(b).decode()
    return {"s": b64(salt), "iv": b64(iv), "c": b64(ct), "it": ITERATIONEN}

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    name, passwort = sys.argv[1], sys.argv[2]
    if len(passwort) < 12:
        sys.exit("Bitte ein Passwort mit mindestens 12 Zeichen verwenden.")
    daten = verschluesseln(name, passwort)
    ziel = Path(__file__).resolve().parent / "name_geschuetzt.json"
    ziel.write_text(json.dumps(daten, separators=(",", ":")))
    print(f"Verschlüsselt gespeichert: {ziel}")
    print("Jetzt build_impressum.py ausführen, um die Seite neu zu bauen.")
