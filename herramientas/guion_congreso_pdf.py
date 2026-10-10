"""Convierte el guion de la ponencia PIDE en un PDF A4."""

import base64
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "guion" / "congreso-pide-2026.md"
OUTPUT = ROOT / "pdf" / "guion-congreso-pide-2026.pdf"
FONT_DIR = ROOT / "presentacion" / "fuentes"

fonts = ""
for family, filename in (
    ("Patrick Hand", "PatrickHand-Regular.ttf"),
    ("Kalam", "Kalam-Bold.ttf"),
    ("Caveat", "Caveat-SemiBold.ttf"),
):
    encoded = base64.b64encode((FONT_DIR / filename).read_bytes()).decode()
    fonts += f"@font-face{{font-family:'{family}';src:url(data:font/ttf;base64,{encoded}) format('truetype')}}\n"

css = fonts + (ROOT / "herramientas" / "guion.css").read_text() + """
h1 { font-size: 22pt; margin-top: 1.25em; break-before: auto; }
body > h1:first-of-type { margin-top: 0; }
h2 { display: block; break-after: avoid-page; page-break-after: avoid; }
table { font-size: 9.2pt; }
a { word-break: normal; overflow-wrap: break-word; }
"""
with tempfile.TemporaryDirectory(prefix="guion-congreso-") as temp:
    temporary = Path(temp)
    style = temporary / "estilo.css"
    html = temporary / "guion.html"
    style.write_text(css)
    subprocess.run([
        "pandoc", str(SOURCE), "-f", "markdown+smart-implicit_figures", "-t", "html5",
        "--standalone", "--embed-resources", "--resource-path", str(SOURCE.parent),
        "--css", str(style), "--metadata", "pagetitle=Guion · Congreso PIDE 2026",
        "-o", str(html),
    ], check=True)
    OUTPUT.parent.mkdir(exist_ok=True)
    subprocess.run([
        "chromium", "--headless=new", "--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage",
        f"--user-data-dir={temporary / 'chrome'}", "--no-pdf-header-footer",
        f"--print-to-pdf={OUTPUT}", "--virtual-time-budget=10000", html.as_uri(),
    ], check=True, capture_output=True)
print(OUTPUT)
