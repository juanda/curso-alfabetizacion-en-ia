#!/bin/sh
AQUI="$(cd "$(dirname "$0")" && pwd)"
export CHROME_PATH="$AQUI/chromium-sin-sandbox.sh"
exec "$AQUI/node_modules/.bin/marp" "$AQUI/../presentacion/presentacion.md" --theme "$AQUI/../presentacion/tema/alfabetizacion.css" --no-stdin --allow-local-files --pdf --pdf-outlines -o "$AQUI/../pdf/presentacion-alfabetizacion-ia.pdf"
