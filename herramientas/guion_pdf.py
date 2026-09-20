"""Convierte guion/guion.md en un PDF (pandoc -> HTML autocontenido -> Chromium)."""
import base64, pathlib, subprocess, tempfile

AQUI = pathlib.Path(__file__).resolve().parent
RAIZ = AQUI.parent
FUENTES = RAIZ / "presentacion" / "fuentes"

ff = ""
for fam, f in (("Patrick Hand", "PatrickHand-Regular.ttf"), ("Kalam", "Kalam-Bold.ttf"), ("Caveat", "Caveat-SemiBold.ttf")):
    b = base64.b64encode((FUENTES / f).read_bytes()).decode()
    ff += "@font-face{font-family:'%s';src:url(data:font/ttf;base64,%s) format('truetype');}\n" % (fam, b)

css = ff + (AQUI / "guion.css").read_text()
tmp = pathlib.Path(tempfile.mkdtemp())
(tmp / "estilo.css").write_text(css)
html = tmp / "guion.html"
subprocess.run(["pandoc", str(RAIZ / "guion" / "guion.md"), "-f", "markdown+smart-implicit_figures", "-t", "html5", "--standalone",
                "--embed-resources", "--resource-path", str(RAIZ / "guion"), "--css", str(tmp / "estilo.css"),
                "--metadata", "pagetitle=Alfabetización en IA · Guion de apoyo", "-o", str(html)], check=True)
out = RAIZ / "pdf" / "guion-alfabetizacion-ia.pdf"
out.parent.mkdir(exist_ok=True)
subprocess.run(["chromium", "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                f"--print-to-pdf={out}", "--virtual-time-budget=10000", f"file://{html}"], check=True, capture_output=True)
print("ok", out)
