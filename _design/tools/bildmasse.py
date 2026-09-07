#!/usr/bin/env python3
"""Liest die echten Pixelmasse aller Bilder in /assets ohne Fremdbibliothek.

Aufruf: python3 _design/tools/bildmasse.py
Zweck:  jedes <img> im Redesign braucht width/height (Core Web Vitals, CLS).
"""
import glob, os, struct, sys

def dims(path):
    with open(path, "rb") as f:
        head = f.read(32)
        if head[:8] == b"\x89PNG\r\n\x1a\n":
            w, h = struct.unpack(">II", head[16:24])
            return w, h
        if head[:2] == b"\xff\xd8":                      # JPEG: SOFn suchen
            f.seek(2)
            while True:
                b = f.read(1)
                if not b:
                    return None
                if b != b"\xff":
                    continue
                marker = f.read(1)
                while marker == b"\xff":
                    marker = f.read(1)
                m = marker[0]
                if m in (0xd8, 0xd9) or 0xd0 <= m <= 0xd7:
                    continue
                ln = struct.unpack(">H", f.read(2))[0]
                if 0xc0 <= m <= 0xcf and m not in (0xc4, 0xc8, 0xcc):
                    f.read(1)
                    h, w = struct.unpack(">HH", f.read(4))
                    return w, h
                f.seek(ln - 2, 1)
        if head[:6] in (b"GIF87a", b"GIF89a"):
            return struct.unpack("<HH", head[6:10])
        if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
            return None                                   # nicht benoetigt
    return None

def main():
    for p in sorted(glob.glob(os.path.join("assets", "*"))):
        if not os.path.isfile(p):
            continue
        d = dims(p)
        kb = os.path.getsize(p) / 1024
        print("%-52s %-12s %8.0f KB" % (p, "%dx%d" % d if d else "-", kb))

if __name__ == "__main__":
    sys.exit(main())
