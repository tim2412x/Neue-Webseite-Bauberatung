#!/usr/bin/env python3
"""Faerbt die weisse Wortmarke aus logo-dark.png auf den Textton um.

logo-dark.png ist weiss auf transparent und war fuer den alten Navy-Kopf
gedacht. Auf dem Grundton #F7F5F0 waere sie unsichtbar. Das Skript setzt alle
Farbkanaele auf --text (#17171A) und laesst die Deckung unveraendert — die
Kanten bleiben also weich, es entsteht kein Blaustich und kein Rand.

Aufruf:  python3 _design/tools/logo_umfaerben.py
Ergebnis: assets/logo-text.png
"""
import os
import struct
import sys
import zlib

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
QUELLE = os.path.join(ROOT, "assets", "logo-dark.png")
ZIEL = os.path.join(ROOT, "assets", "logo-text.png")
TON = (0x17, 0x17, 0x1A)


def bloecke(daten):
    i = 8
    while i < len(daten):
        laenge, typ = struct.unpack(">I4s", daten[i:i + 8])
        yield typ, daten[i + 8:i + 8 + laenge]
        i += 12 + laenge


def entfiltern(roh, breite, hoehe):
    """PNG-Zeilenfilter 0–4 rueckgaengig machen. 8 Bit RGBA, nicht verschraenkt."""
    schritt = breite * 4
    aus = bytearray(schritt * hoehe)
    vor = bytearray(schritt)
    pos = 0
    for y in range(hoehe):
        filt = roh[pos]
        pos += 1
        zeile = bytearray(roh[pos:pos + schritt])
        pos += schritt
        if filt == 1:
            for x in range(4, schritt):
                zeile[x] = (zeile[x] + zeile[x - 4]) & 0xFF
        elif filt == 2:
            for x in range(schritt):
                zeile[x] = (zeile[x] + vor[x]) & 0xFF
        elif filt == 3:
            for x in range(schritt):
                links = zeile[x - 4] if x >= 4 else 0
                zeile[x] = (zeile[x] + ((links + vor[x]) >> 1)) & 0xFF
        elif filt == 4:
            for x in range(schritt):
                a = zeile[x - 4] if x >= 4 else 0
                b = vor[x]
                c = vor[x - 4] if x >= 4 else 0
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                nah = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                zeile[x] = (zeile[x] + nah) & 0xFF
        elif filt != 0:
            raise ValueError("unbekannter Zeilenfilter %d" % filt)
        aus[y * schritt:(y + 1) * schritt] = zeile
        vor = zeile
    return aus


def block(typ, inhalt):
    return (struct.pack(">I", len(inhalt)) + typ + inhalt
            + struct.pack(">I", zlib.crc32(typ + inhalt) & 0xFFFFFFFF))


def main():
    daten = open(QUELLE, "rb").read()
    if daten[:8] != b"\x89PNG\r\n\x1a\n":
        sys.exit("keine PNG-Datei: %s" % QUELLE)

    idat = b""
    kopf = None
    for typ, inhalt in bloecke(daten):
        if typ == b"IHDR":
            kopf = inhalt
        elif typ == b"IDAT":
            idat += inhalt
    breite, hoehe, tiefe, art, _, _, verschraenkt = struct.unpack(">IIBBBBB", kopf)
    if (tiefe, art, verschraenkt) != (8, 6, 0):
        sys.exit("erwartet werden 8 Bit RGBA ohne Verschraenkung")

    pixel = entfiltern(zlib.decompress(idat), breite, hoehe)
    for i in range(0, len(pixel), 4):
        if pixel[i + 3]:                       # nur sichtbare Punkte faerben
            pixel[i], pixel[i + 1], pixel[i + 2] = TON

    schritt = breite * 4
    roh = bytearray()
    for y in range(hoehe):
        roh.append(0)                          # Filter 0: keiner
        roh += pixel[y * schritt:(y + 1) * schritt]

    with open(ZIEL, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(block(b"IHDR", kopf))
        f.write(block(b"IDAT", zlib.compress(bytes(roh), 9)))
        f.write(block(b"IEND", b""))
    print("%s — %dx%d, %d KB" % (os.path.relpath(ZIEL, ROOT), breite, hoehe,
                                 os.path.getsize(ZIEL) // 1024))


if __name__ == "__main__":
    main()
