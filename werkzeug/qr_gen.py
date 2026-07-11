# -*- coding: utf-8 -*-
"""Erzeugt für jede Telefonnummer der Seite einen QR-Code (tel:-URI),
verifiziert ihn per Rückwärts-Dekodierung und speichert alles kompakt
als Bitmatrix (Base64) in qr_map.json."""
import base64, json, sys
import cv2
import numpy as np
from data import GROUPS
from data2 import GROUPS2

def alle_nummern():
    nums = set()
    for g in GROUPS + GROUPS2:
        for t in g["topics"]:
            for land in t.get("entries", {}).values():
                for e in land:
                    for _, tel in e["phones"]:
                        nums.add(tel)
    # Notruf- und Schnellwahlnummern der festen Seitenelemente
    nums.update(["112", "110", "144", "133", "122", "117", "118",
                 "03012074182", "03168722200"])
    # Impressum
    nums.add("+4917682547714")
    return sorted(nums)

def matrix_zu_b64(matrix):
    """Packt die QR-Matrix (0=schwarz) zeilenweise in Bits, MSB zuerst."""
    n = matrix.shape[0]
    bits = (matrix == 0).astype(np.uint8).flatten()  # 1 = schwarzes Modul
    gepackt = np.packbits(bits)
    return n, base64.b64encode(gepackt.tobytes()).decode()

def b64_zu_matrix(n, b64):
    """Gegenprobe: entpackt exakt so, wie es das JavaScript später tut."""
    bits = np.unpackbits(np.frombuffer(base64.b64decode(b64), dtype=np.uint8))
    return bits[:n * n].reshape(n, n)

enc = cv2.QRCodeEncoder.create()
det = cv2.QRCodeDetector()
qr_map, fehler = {}, []

for nummer in alle_nummern():
    uri = "tel:" + nummer
    m = enc.encode(uri)
    n, b64 = matrix_zu_b64(m)

    # Verifikation 1: Bitpacking verlustfrei?
    zurueck = b64_zu_matrix(n, b64)
    assert np.array_equal(zurueck, (m == 0).astype(np.uint8)), f"Bitfehler bei {nummer}"

    # Verifikation 2: Aus den entpackten Bits ein Bild bauen und dekodieren
    # (mit Ruhezone, wie es die Handykamera sieht)
    bild = np.where(zurueck == 1, 0, 255).astype(np.uint8)
    bild = cv2.copyMakeBorder(bild, 4, 4, 4, 4, cv2.BORDER_CONSTANT, value=255)
    bild = cv2.resize(bild, (bild.shape[1] * 10, bild.shape[0] * 10),
                      interpolation=cv2.INTER_NEAREST)
    text, _, _ = det.detectAndDecode(bild)
    if text != uri:
        fehler.append((nummer, text))
        continue
    qr_map[nummer] = {"n": n, "d": b64}

if fehler:
    print("FEHLGESCHLAGEN:", fehler)
    sys.exit(1)

json.dump(qr_map, open("qr_map.json", "w"), separators=(",", ":"))
groesse = sum(len(v["d"]) for v in qr_map.values())
print(f"{len(qr_map)} QR-Codes erzeugt und verifiziert, Nutzdaten ≈ {groesse//1024} KB")
