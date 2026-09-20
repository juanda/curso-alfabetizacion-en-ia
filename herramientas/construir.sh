#!/bin/sh
# Construye el tema (con las fuentes incrustadas), las ilustraciones y los PDF.
# Uso: ./construir.sh            (todo)
#      ./construir.sh imagenes   (solo ilustraciones)
#      ./construir.sh pdf        (solo PDF de presentación y guion)
set -e
AQUI="$(cd "$(dirname "$0")" && pwd)"
RAIZ="$AQUI/.."
PRES="$RAIZ/presentacion"
export CHROME_PATH="${CHROME_PATH:-/usr/bin/chromium}"

imagenes() { (cd "$AQUI" && python3 render.py); }

tema() {
  python3 - "$PRES" <<'PY'
import base64, pathlib, sys
p = pathlib.Path(sys.argv[1])
css = (p / "tema" / "base.css").read_text()
fonts = [("Patrick Hand", "PatrickHand-Regular.ttf"), ("Kalam", "Kalam-Bold.ttf"), ("Caveat", "Caveat-SemiBold.ttf")]
ff = ""
for fam, f in fonts:
    b = base64.b64encode((p / "fuentes" / f).read_bytes()).decode()
    ff += "@font-face{font-family:'%s';src:url(data:font/ttf;base64,%s) format('truetype');font-weight:normal;font-style:normal}\n" % (fam, b)
head, rest = css.split("*/", 1)
(p / "tema" / "alfabetizacion.css").write_text(head + "*/\n" + ff + rest)
PY
}

pdf() {
  tema
  mkdir -p "$RAIZ/pdf"
  "$AQUI/marp-pdf.sh"
  python3 "$AQUI/guion_pdf.py"
}

case "$1" in
  imagenes) imagenes ;;
  pdf) pdf ;;
  *) imagenes; pdf ;;
esac
