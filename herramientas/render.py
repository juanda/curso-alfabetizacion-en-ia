"""Genera las ilustraciones: escenas.py -> img/svg/*.svg -> img/*.png (vía Chromium sin cabeza)."""
import importlib, os, subprocess, sys, tempfile, re, pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent / "presentacion"
SVG_DIR, PNG_DIR, FONTS = BASE / "img" / "svg", BASE / "img", BASE / "fuentes"
SVG_DIR.mkdir(parents=True, exist_ok=True)

FONT_CSS = "".join(
    "@font-face{{font-family:'{}';src:url('file://{}');font-weight:{}}}".format(n, FONTS / f, w)
    for n, f, w in (("Patrick Hand", "PatrickHand-Regular.ttf", "normal"), ("Kalam", "Kalam-Bold.ttf", "normal"), ("Caveat", "Caveat-SemiBold.ttf", "normal")))


def render_png(name, svg, w, h):
    html = "<html><head><meta charset='utf-8'><style>{}html,body{{margin:0;background:transparent}}svg{{display:block}}</style></head><body>{}</body></html>".format(FONT_CSS, svg)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html)
        tmp = f.name
    out = PNG_DIR / f"{name}.png"
    subprocess.run(["chromium", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--default-background-color=00000000", "--force-device-scale-factor=2",
                    f"--window-size={w},{h}", f"--screenshot={out}", "--virtual-time-budget=3000", f"file://{tmp}"],
                   capture_output=True, timeout=120)
    os.unlink(tmp)


if __name__ == "__main__":
    sys.path.insert(0, str(pathlib.Path(__file__).parent))
    only = set(sys.argv[1:])
    mods = [m for m in ("escenas_1", "escenas_2", "escenas_3", "escenas_4", "escenas_prueba") if (pathlib.Path(__file__).parent / f"{m}.py").exists()]
    for m in mods:
        mod = importlib.import_module(m)
        for name, fn in mod.ESCENAS.items():
            if only and name not in only:
                continue
            s = fn()
            svg = s.svg()
            (SVG_DIR / f"{name}.svg").write_text(svg)
            render_png(name, svg, s.w, s.h - s.top)
            print("ok", name)
