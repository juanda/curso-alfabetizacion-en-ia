"""Iconos esquemáticos reutilizables. (x,y) = centro, k = escala."""
from sketch import *


def i_doc(s, x, y, k=1.0, fill="white", rayas=3):
    s.rect(x - 34 * k, y - 44 * k, 68 * k, 88 * k, fill, r=6, sw=3)
    for i in range(rayas):
        s.line(x - 20 * k, y - 22 * k + i * 16 * k, x + 20 * k, y - 22 * k + i * 16 * k, sw=2.6, dbl=False)


def i_imagen(s, x, y, k=1.0):
    s.rect(x - 44 * k, y - 34 * k, 88 * k, 68 * k, "white", r=6, sw=3)
    s.poly([(x - 36 * k, y + 26 * k), (x - 12 * k, y - 8 * k), (x + 4 * k, y + 12 * k), (x + 18 * k, y - 2 * k), (x + 36 * k, y + 26 * k)], "green", sw=2.6, dbl=False)
    s.ellipse(x + 24 * k, y - 18 * k, 8 * k, 8 * k, "yellow", sw=2.6, dbl=False)


def i_codigo(s, x, y, k=1.0):
    s.rect(x - 44 * k, y - 34 * k, 88 * k, 68 * k, "#3b3b3b", r=8, sw=3)
    s.text(x, y + 12 * k, "</>", 34 * k, font="title", color="green")


def i_mic(s, x, y, k=1.0):
    s.rect(x - 18 * k, y - 46 * k, 36 * k, 62 * k, "blue", r=18, sw=3)
    for j in range(3):
        s.line(x - 10 * k, y - 28 * k + j * 14 * k, x + 10 * k, y - 28 * k + j * 14 * k, sw=2.2, dbl=False)
    s.path([(x - 30 * k, y - 6 * k), (x - 28 * k, y + 22 * k), (x, y + 34 * k), (x + 28 * k, y + 22 * k), (x + 30 * k, y - 6 * k)], sw=3.4)
    s.line(x, y + 34 * k, x, y + 50 * k, sw=3.4)
    s.line(x - 16 * k, y + 52 * k, x + 16 * k, y + 52 * k, sw=3.4)


def i_video(s, x, y, k=1.0):
    s.rect(x - 44 * k, y - 34 * k, 88 * k, 68 * k, "white", r=8, sw=3)
    s.poly([(x - 12 * k, y - 18 * k), (x + 20 * k, y), (x - 12 * k, y + 18 * k)], "red", sw=2.6, dbl=False)


def i_libro(s, x, y, k=1.0, fill="blue"):
    s.rect(x - 40 * k, y - 30 * k, 80 * k, 60 * k, fill, r=4, sw=3)
    s.line(x, y - 30 * k, x, y + 30 * k, sw=2.6, dbl=False)
    for i in range(2):
        s.line(x - 30 * k, y - 12 * k + i * 16 * k, x - 10 * k, y - 12 * k + i * 16 * k, sw=2.2, dbl=False)
        s.line(x + 10 * k, y - 12 * k + i * 16 * k, x + 30 * k, y - 12 * k + i * 16 * k, sw=2.2, dbl=False)


def i_corazon(s, x, y, k=1.0, fill="red"):
    pts = [(x, y + 34 * k), (x - 34 * k, y - 2 * k), (x - 30 * k, y - 26 * k), (x - 12 * k, y - 32 * k), (x, y - 16 * k),
           (x + 12 * k, y - 32 * k), (x + 30 * k, y - 26 * k), (x + 34 * k, y - 2 * k)]
    s.path(pts, True, fill, INK, 3, 1)


def i_servidor(s, x, y, k=1.0):
    for i in range(3):
        s.rect(x - 40 * k, y - 50 * k + i * 36 * k, 80 * k, 30 * k, "gray", r=5, sw=3)
        s.dot(x + 26 * k, y - 35 * k + i * 36 * k, 3.5, "green")
        s.line(x - 28 * k, y - 35 * k + i * 36 * k, x + 8 * k, y - 35 * k + i * 36 * k, sw=2.4, dbl=False)


def i_caja(s, x, y, k=1.0):
    s.rect(x - 40 * k, y - 34 * k, 80 * k, 68 * k, "#2a2a2a", r=6, sw=3)
    s.text(x, y + 16 * k, "?", 52 * k, font="title", color="yellow")


def i_escudo(s, x, y, k=1.0, fill="blue"):
    s.path([(x - 34 * k, y - 32 * k), (x, y - 42 * k), (x + 34 * k, y - 32 * k), (x + 30 * k, y + 10 * k), (x, y + 42 * k), (x - 30 * k, y + 10 * k)], True, fill, INK, 3, 1)


def i_ojo(s, x, y, k=1.0):
    s.path([(x - 44 * k, y), (x - 16 * k, y - 22 * k), (x + 16 * k, y - 22 * k), (x + 44 * k, y), (x + 16 * k, y + 22 * k), (x - 16 * k, y + 22 * k)], True, "white", INK, 3, 1)
    s.ellipse(x, y, 13 * k, 13 * k, "teal", sw=2.6)
    s.dot(x, y, 4.5)


def i_lapiz(s, x, y, k=1.0):
    s.poly([(x - 40 * k, y + 30 * k), (x - 30 * k, y + 14 * k), (x + 30 * k, y - 34 * k), (x + 42 * k, y - 22 * k), (x - 16 * k, y + 28 * k)], "yellow", sw=3)
    s.poly([(x - 40 * k, y + 30 * k), (x - 30 * k, y + 14 * k), (x - 16 * k, y + 28 * k)], "pink", sw=2.6, dbl=False)


def i_bombilla(s, x, y, k=1.0, fill="yellow"):
    s.ellipse(x, y - 8 * k, 24 * k, 26 * k, fill, sw=3)
    s.rect(x - 12 * k, y + 16 * k, 24 * k, 16 * k, "gray", r=4, sw=2.8)
    for a in (-1.0, -0.5, 0, 0.5, 1.0):
        s.line(x + math.sin(a) * 34 * k, y - 8 * k - math.cos(a) * 34 * k, x + math.sin(a) * 46 * k, y - 8 * k - math.cos(a) * 46 * k, sw=2.6, dbl=False)


def i_lampara(s, x, y, k=1.0, on=True):
    s.poly([(x - 34 * k, y - 8 * k), (x + 34 * k, y - 8 * k), (x + 20 * k, y - 44 * k), (x - 20 * k, y - 44 * k)], "yellow" if on else "gray", sw=3)
    s.line(x, y - 8 * k, x, y + 34 * k, sw=3.4)
    s.line(x - 22 * k, y + 36 * k, x + 22 * k, y + 36 * k, sw=4)
    if on:
        for a in (-0.9, 0, 0.9):
            s.line(x + math.sin(a) * 30 * k, y + 4 * k, x + math.sin(a) * 44 * k, y + 22 * k, sw=2.6, dbl=False, stroke="#d9a400")


def i_ventilador(s, x, y, k=1.0):
    s.line(x, y + 10 * k, x, y + 44 * k, sw=4)
    s.line(x - 24 * k, y + 46 * k, x + 24 * k, y + 46 * k, sw=4)
    for a in (0, 2.1, 4.2):
        s.ellipse(x + math.cos(a) * 20 * k, y - 8 * k + math.sin(a) * 20 * k, 14 * k, 8 * k, "blue", sw=2.8, rot=a)
    s.ellipse(x, y - 8 * k, 6 * k, 6 * k, "gray", sw=2.6, dbl=False)


def i_pincel(s, x, y, k=1.0):
    s.line(x - 30 * k, y + 34 * k, x + 24 * k, y - 26 * k, sw=5, stroke="#8b5e3c")
    s.ellipse(x + 30 * k, y - 34 * k, 14 * k, 10 * k, "red", sw=3, rot=-0.9)


def i_paleta(s, x, y, k=1.0):
    s.path([(x - 42 * k, y), (x - 24 * k, y - 30 * k), (x + 14 * k, y - 34 * k), (x + 44 * k, y - 8 * k), (x + 34 * k, y + 22 * k), (x + 6 * k, y + 8 * k), (x - 14 * k, y + 32 * k), (x - 38 * k, y + 22 * k)], True, "#f5e2c0", INK, 3, 1)
    for (dx, dy, c) in ((-22, -10, "red"), (-2, -18, "yellow"), (20, -12, "blue"), (24, 8, "green")):
        s.ellipse(x + dx * k, y + dy * k, 7 * k, 7 * k, c, sw=2, dbl=False)


def i_camara(s, x, y, k=1.0):
    s.rect(x - 40 * k, y - 22 * k, 80 * k, 52 * k, "gray", r=8, sw=3)
    s.rect(x - 16 * k, y - 34 * k, 32 * k, 14 * k, "gray", r=4, sw=3)
    s.ellipse(x, y + 4 * k, 18 * k, 18 * k, "blue", sw=3)
    s.ellipse(x, y + 4 * k, 8 * k, 8 * k, "white", sw=2.4, dbl=False)


def wrap(t, n):
    words, lines, cur = t.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    lines.append(cur)
    return lines


def timeline(s, events, y0, x0, dx, size=26, wrapn=17, dsize=36):
    """events = [(fecha, texto, color, arriba(1)/abajo(-1))]"""
    s.arrow(x0 - 70, y0, x0 + dx * (len(events) - 1) + 90, y0, sw=5, head=22)
    for i, (d, t, c, up) in enumerate(events):
        x = x0 + i * dx
        s.ellipse(x, y0, 15, 15, c, sw=3.4)
        lines = wrap(t, wrapn)
        if up == 1:
            s.line(x, y0 - 16, x, y0 - 50, sw=2.6, dbl=False)
            ty = y0 - 70
            for j, ln in enumerate(reversed(lines)):
                s.text(x, ty - j * (size + 4), ln, size)
            s.text(x, ty - len(lines) * (size + 4) - 6, d, dsize, font="title")
        else:
            s.line(x, y0 + 16, x, y0 + 50, sw=2.6, dbl=False)
            s.text(x, y0 + 50 + dsize, d, dsize, font="title")
            for j, ln in enumerate(lines):
                s.text(x, y0 + 50 + dsize + 34 + j * (size + 4), ln, size)


def pesa(s, x, y, k=1.0):
    s.line(x - 44 * k, y, x + 44 * k, y, sw=6)
    s.rect(x - 60 * k, y - 26 * k, 22 * k, 52 * k, "gray", r=5)
    s.rect(x + 38 * k, y - 26 * k, 22 * k, 52 * k, "gray", r=5)


def sudor(s, x, y):
    s.path([(x, y - 14), (x + 8, y + 2), (x, y + 10), (x - 8, y + 2)], True, "blue", INK, 2.4, .6, False)


def i_calc(s, x, y, k=1.0):
    s.rect(x - 32 * k, y - 44 * k, 64 * k, 88 * k, "orange", r=8, sw=3)
    s.rect(x - 24 * k, y - 36 * k, 48 * k, 20 * k, "white", r=4, sw=2.4, dbl=False)
    for r in range(3):
        for c in range(3):
            s.ellipse(x - 16 * k + c * 16 * k, y - 2 * k + r * 16 * k, 4.5 * k, 4.5 * k, "white", sw=2, dbl=False)
