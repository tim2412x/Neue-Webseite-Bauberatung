#!/usr/bin/env bash
# Laedt Spectral und Barlow (Subsets latin + latin-ext) als WOFF2 nach assets/fonts/.
# Einmalig noetig. Danach laeuft die Seite ohne Aufruf externer Domains (REDESIGN §2, §13).
# Aufruf aus dem Projektwurzelverzeichnis:  bash _design/tools/schriften_holen.sh
set -euo pipefail
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'
URL='https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,300;0,400;1,300&family=Barlow:wght@400;500&display=swap'
mkdir -p assets/fonts
curl -sSf -m 30 -A "$UA" "$URL" -o /tmp/gf.css
# Zielnamen + Quell-URLs herausschreiben, danach mit curl laden (python hat hier kein CA-Bundle)
python3 - > /tmp/gf.list <<'PY'
import re
css = open('/tmp/gf.css', encoding='utf-8').read()
blocks = re.split(r'/\*\s*([a-z-]+)\s*\*/', css)
for i in range(1, len(blocks), 2):
    subset, body = blocks[i], blocks[i + 1]
    if subset not in ('latin', 'latin-ext'):
        continue
    fam = re.search(r"font-family: '([^']+)'", body).group(1).lower()
    wgt = re.search(r'font-weight: (\d+)', body).group(1)
    ital = 'italic' in re.search(r'font-style: (\w+)', body).group(1)
    url = re.search(r'url\((https://[^)]+)\)', body).group(1)
    print('assets/fonts/%s-%s%s-%s.woff2 %s' % (fam, wgt, '-italic' if ital else '', subset, url))
PY
while read -r dest url; do
  if [ -s "$dest" ]; then echo "vorhanden: $dest"; else
    curl -sSf -m 30 -A "$UA" "$url" -o "$dest"
    printf 'geladen:   %-52s %5s\n' "$dest" "$(du -h "$dest" | cut -f1)"
  fi
done < /tmp/gf.list
