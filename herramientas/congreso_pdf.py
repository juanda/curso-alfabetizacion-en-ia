"""Renderiza la fuente Marp del congreso con Pandoc y Chromium si no hay Marp CLI."""

import base64
import html
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "presentacion" / "congreso-pide-2026.md"
OUTPUT = ROOT / "pdf" / "congreso-pide-2026.pdf"
THEME = ROOT / "presentacion" / "tema" / "base.css"
FONTS = ROOT / "presentacion" / "fuentes"

raw = SOURCE.read_text(encoding="utf-8")
parts = re.split(r"(?m)^---\s*$", raw)
slides = [p.strip() for p in parts[2:] if p.strip()]

font_css = ""
for family, filename in (
    ("Patrick Hand", "PatrickHand-Regular.ttf"),
    ("Kalam", "Kalam-Bold.ttf"),
    ("Caveat", "Caveat-SemiBold.ttf"),
):
    encoded = base64.b64encode((FONTS / filename).read_bytes()).decode("ascii")
    font_css += f"@font-face{{font-family:'{family}';src:url(data:font/ttf;base64,{encoded}) format('truetype')}}\n"

sections = []
for number, slide in enumerate(slides, 1):
    class_match = re.search(r"<!-- _class: ([\w -]+) -->", slide)
    bg_match = re.search(r"<!-- _backgroundColor: (#[\da-fA-F]+) -->", slide)
    klass = class_match.group(1) if class_match else ""
    slide = re.sub(r"<!-- _(?:class|backgroundColor|paginate|footer): .*? -->\n?", "", slide)
    bg_image = ""

    def image_sub(match):
        nonlocal_bg = match.group(1)
        src = (SOURCE.parent / match.group(2)).resolve().as_uri()
        if nonlocal_bg.startswith("bg right:"):
            width = nonlocal_bg.split(":", 1)[1].split("%", 1)[0]
            bg_image_list.append(f'<img class="bg-right" style="width:{width}%" src="{src}">')
            return ""
        width = re.search(r"w:(\d+)", nonlocal_bg)
        size = f' style="width:{width.group(1)}px"' if width else ""
        return f'<img class="figure"{size} src="{src}">'

    bg_image_list = []
    slide = re.sub(r"!\[([^]]*)\]\((img/[^)]+)\)", image_sub, slide)
    bg_image = "".join(bg_image_list)
    body = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "html5"],
        input=slide, text=True, capture_output=True, check=True,
    ).stdout
    color = f' style="background:{bg_match.group(1)}"' if bg_match else ""
    footer = "" if number == 1 else f'<footer>V Congreso PIDE · Juan David Rodríguez García · CC BY-NC 4.0</footer><span class="page">{number}</span>'
    sections.append(f'<section class="{html.escape(klass)}"{color}>{bg_image}<div class="content">{body}</div>{footer}</section>')

css = font_css + THEME.read_text(encoding="utf-8") + """
@page { size: 13.333333in 7.5in; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
section { position: relative; display: flex; flex-direction: column; width:1280px; height:720px;
  break-after: page; page-break-after: always; overflow:hidden; }
section:last-child { break-after:auto; page-break-after:auto; }
section .content { position: relative; z-index:1; width:100%; }
section:has(.bg-right) .content { width:54%; }
section:has(.bg-right[style*='52%']) .content { width:48%; }
section:has(.bg-right[style*='44%']) .content { width:56%; }
.bg-right { position:absolute; right:0; top:0; height:100%; object-fit:contain; z-index:0; }
.figure { display:block; max-width:100%; max-height:490px; object-fit:contain; margin:0 auto; }
.page { position:absolute; right:34px; bottom:22px; font-size:22px; color:#8a867c; }
section.portada { padding-top:90px; }
section.seccion .content { width:100%; }
section.centro .content { width:100%; }
section.centro .figure { margin: 0 auto; max-height:390px; }
section.grande li { margin:.25em 0; }
section.grande h2 { font-size:48px; }
section.pequena { font-size:25px; }
section.pequena h2 { font-size:44px; }
section.pequena li { margin:.16em 0; }
section:has(.bg-right) h2 { font-size:46px; }
section:has(.bg-right) ul { font-size:29px; }
@media print { html,body { print-color-adjust:exact; -webkit-print-color-adjust:exact; } }
"""
with tempfile.TemporaryDirectory(prefix="pide-deck-") as temp:
    page = Path(temp) / "slides.html"
    page.write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(sections)}</body></html>', encoding="utf-8")
    OUTPUT.parent.mkdir(exist_ok=True)
    subprocess.run([
        "chromium", "--headless=new", "--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage",
        f"--user-data-dir={Path(temp) / 'chrome'}",
        "--no-pdf-header-footer", f"--print-to-pdf={OUTPUT}", "--virtual-time-budget=10000", page.as_uri(),
    ], check=True, capture_output=True)
print(f"{len(slides)} diapositivas: {OUTPUT}")
