"""Mini-librería para generar ilustraciones SVG con aspecto de boceto hecho a mano.

Todo el trazo lleva un pequeño temblor aleatorio (con semilla fija, así los
dibujos son reproducibles), doble trazo tenue y rellenos de "rotulador"
ligeramente desplazados del contorno.
"""
import math
import random

INK = "#2a2a2a"
PAL = dict(
    green="#a6e05a", yellow="#ffd95a", orange="#ff9d5c", blue="#8ccbf2",
    pink="#ff9bb0", purple="#c3a6f0", red="#f0645a", gray="#dedad0",
    white="#fffdf6", teal="#6fd6c2", brown="#c99a6b", none=None,
)
FONTS = {
    "body": "'Patrick Hand', 'Comic Sans MS', cursive",
    "title": "'Kalam', 'Patrick Hand', cursive",
    "note": "'Caveat', 'Patrick Hand', cursive",
}


def col(c):
    return PAL.get(c, c)


class Sketch:
    def __init__(self, w=800, h=500, seed=1):
        self.w, self.h = w, h
        self.r = random.Random(seed)
        self.o = []
        self.top = 0    # píxeles que se recortan por arriba (para quitar rótulos)
        self.ka = 1.0   # factor de amplitud del temblor
        self.ks = 1.0   # factor de grosor de trazo

    # ---------- utilidades geométricas ----------
    def j(self, a):
        return self.r.uniform(-a, a)

    def _wob(self, pts, amp):
        return [(x + self.j(amp), y + self.j(amp)) for x, y in pts]

    @staticmethod
    def _smooth(pts, closed):
        n = len(pts)
        if n < 3:
            return "M{:.1f},{:.1f} L{:.1f},{:.1f}".format(*pts[0], *pts[-1])
        P = pts + pts[:3] if closed else [pts[0]] + pts + [pts[-1]]
        d = ""
        rng = range(n) if closed else range(n - 1)
        for i in rng:
            if closed:
                p0, p1, p2, p3 = P[(i - 1) % n], P[i], P[(i + 1) % n], P[(i + 2) % n]
            else:
                p0, p1, p2, p3 = P[i], P[i + 1], P[min(i + 2, len(P) - 1)], P[min(i + 3, len(P) - 1)]
            if i == 0:
                d += "M{:.1f},{:.1f} ".format(*p1)
            c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
            c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
            d += "C{:.1f},{:.1f} {:.1f},{:.1f} {:.1f},{:.1f} ".format(*c1, *c2, *p2)
        return d + ("Z" if closed else "")

    # ---------- primitivas ----------
    def path(self, pts, closed=False, fill=None, stroke=INK, sw=3.4, amp=1.3, dbl=True, op=1.0):
        fill = col(fill)
        amp, sw = amp * self.ka, sw * self.ks
        if fill:
            fp = self._wob(pts, amp * 1.6)
            fp = [(x + 2.5 * self.ka, y + 2 * self.ka) for x, y in fp]
            self.o.append('<path d="{}" fill="{}" stroke="none" opacity="{}"/>'.format(
                self._smooth(fp, closed or True), fill, op))
        if stroke:
            p = self._wob(pts, amp)
            self.o.append('<path d="{}" fill="none" stroke="{}" stroke-width="{}" stroke-linecap="round" stroke-linejoin="round"/>'.format(
                self._smooth(p, closed), stroke, sw))
            if dbl:
                p2 = self._wob(pts, amp * 1.4)
                self.o.append('<path d="{}" fill="none" stroke="{}" stroke-width="{}" stroke-linecap="round" opacity="0.45"/>'.format(
                    self._smooth(p2, closed), stroke, round(sw * 0.55, 1)))

    def line(self, x1, y1, x2, y2, sw=3.4, stroke=INK, amp=1.1, dbl=True):
        L = math.hypot(x2 - x1, y2 - y1)
        n = max(3, int(L / 45) + 2)
        pts = [(x1 + (x2 - x1) * i / (n - 1), y1 + (y2 - y1) * i / (n - 1)) for i in range(n)]
        self.path(pts, False, None, stroke, sw, amp, dbl)

    def polyline(self, pts, **kw):
        self.path(pts, False, None, **kw)

    def poly(self, pts, fill=None, **kw):
        # polígono con esquinas rectas (sin suavizar) y contorno tembloroso
        fill_c = col(fill)
        if fill_c:
            fp = [(x + 2.5 * self.ka + self.j(2 * self.ka), y + 2 * self.ka + self.j(2 * self.ka)) for x, y in pts]
            self.o.append('<path d="M{} Z" fill="{}" stroke="none"/>'.format(
                " L".join("{:.1f},{:.1f}".format(*p) for p in fp), fill_c))
        sw = kw.get("sw", 3.4)
        n = len(pts)
        for i in range(n):
            a, b = pts[i], pts[(i + 1) % n]
            self.line(a[0], a[1], b[0], b[1], sw=sw, dbl=kw.get("dbl", True))

    def rect(self, x, y, w, h, fill=None, r=10, sw=3.4, dbl=True, amp=1.2):
        r = min(r, w / 2, h / 2)
        pts = [(x + r, y), (x + w / 2, y), (x + w - r, y), (x + w, y + r), (x + w, y + h / 2),
               (x + w, y + h - r), (x + w - r, y + h), (x + w / 2, y + h), (x + r, y + h),
               (x, y + h - r), (x, y + h / 2), (x, y + r)]
        self.path(pts, True, fill, INK, sw, amp, dbl)

    def ellipse(self, cx, cy, rx, ry, fill=None, sw=3.4, dbl=True, amp=1.2, rot=0, stroke=INK):
        n = 16
        pts = []
        for i in range(n):
            a = 2 * math.pi * i / n + self.j(0.04)
            x, y = rx * math.cos(a), ry * math.sin(a)
            c, s = math.cos(rot), math.sin(rot)
            pts.append((cx + x * c - y * s, cy + x * s + y * c))
        self.path(pts, True, fill, stroke, sw, amp, dbl)

    def dot(self, x, y, r=4, fill=INK):
        self.o.append('<circle cx="{:.1f}" cy="{:.1f}" r="{:.1f}" fill="{}"/>'.format(x + self.j(.6 * self.ka), y + self.j(.6 * self.ka), r * max(self.ks, .6), col(fill)))

    def text(self, x, y, s, size=28, anchor="middle", font="body", color=INK, rot=0, weight="normal"):
        s = s.replace("&", "&amp;").replace("<", "&lt;")
        t = ' transform="rotate({} {} {})"'.format(rot, x, y) if rot else ""
        self.o.append('<text x="{}" y="{}" font-family="{}" font-size="{}" text-anchor="{}" fill="{}" font-weight="{}"{}>{}</text>'.format(
            x, y, FONTS[font], size, anchor, col(color), weight, t, s))

    def lines(self, x, y, arr, size=26, lh=None, **kw):
        lh = lh or size * 1.2
        for i, s in enumerate(arr):
            self.text(x, y + i * lh, s, size, **kw)

    def arrow(self, x1, y1, x2, y2, bend=0, sw=3.4, head=16, stroke=INK):
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L, dx / L
        cx, cy = mx + nx * bend, my + ny * bend
        pts = [(x1, y1)]
        for t in (0.25, 0.5, 0.75):
            bx = (1 - t) ** 2 * x1 + 2 * (1 - t) * t * cx + t * t * x2
            by = (1 - t) ** 2 * y1 + 2 * (1 - t) * t * cy + t * t * y2
            pts.append((bx, by))
        pts.append((x2, y2))
        self.path(pts, False, None, stroke, sw, 1.0, True)
        # cabeza
        ang = math.atan2(y2 - pts[-2][1], x2 - pts[-2][0])
        for s in (+0.5, -0.5):
            self.line(x2, y2, x2 - head * math.cos(ang + s), y2 - head * math.sin(ang + s), sw=sw, stroke=stroke, dbl=False)

    def underline(self, x1, x2, y, color="yellow", sw=9):
        pts = [(x1, y), ((x1 + x2) / 2, y + self.j(4) + 2), (x2, y - 2)]
        self.o.append('<path d="{}" fill="none" stroke="{}" stroke-width="{}" stroke-linecap="round" opacity="0.85"/>'.format(
            self._smooth(pts, False), col(color), sw))

    def bubble(self, x, y, w, h, arr=None, tail=None, fill="white", size=26, font="body", tcol=INK):
        """Globo de diálogo. tail=(tx,ty) es la punta de la cola (puede quedar arriba, abajo, izq. o dcha.)."""
        self.rect(x, y, w, h, fill, r=24, sw=3.2, dbl=True)
        if tail:
            tx, ty = tail
            cx, cy = x + w / 2, y + h / 2
            if ty > y + h:      # abajo
                bx = min(max(tx, x + 40), x + w - 40)
                base = [(bx - 16, y + h), (bx + 16, y + h)]
                cover = [(bx - 14, y + h - 4), (bx + 14, y + h - 4), (bx + 14, y + h + 4), (bx - 14, y + h + 4)]
            elif ty < y:        # arriba
                bx = min(max(tx, x + 40), x + w - 40)
                base = [(bx - 16, y), (bx + 16, y)]
                cover = [(bx - 14, y - 4), (bx + 14, y - 4), (bx + 14, y + 4), (bx - 14, y + 4)]
            elif tx < x:        # izquierda
                by = min(max(ty, y + 30), y + h - 30)
                base = [(x, by - 16), (x, by + 16)]
                cover = [(x - 4, by - 14), (x + 4, by - 14), (x + 4, by + 14), (x - 4, by + 14)]
            else:               # derecha
                by = min(max(ty, y + 30), y + h - 30)
                base = [(x + w, by - 16), (x + w, by + 16)]
                cover = [(x + w - 4, by - 14), (x + w + 4, by - 14), (x + w + 4, by + 14), (x + w - 4, by + 14)]
            self.o.append('<path d="M{} Z" fill="{}" stroke="none"/>'.format(
                " L".join("{:.1f},{:.1f}".format(*p) for p in base + [(tx, ty)]), col(fill)))
            self.o.append('<path d="M{} Z" fill="{}" stroke="none"/>'.format(
                " L".join("{:.1f},{:.1f}".format(*p) for p in cover), col(fill)))
            self.line(base[0][0], base[0][1], tx, ty, sw=3.2, dbl=False)
            self.line(base[1][0], base[1][1], tx, ty, sw=3.2, dbl=False)
        if arr:
            n = len(arr)
            lh = size * 1.18
            y0 = y + h / 2 - (n - 1) * lh / 2 + size * 0.32
            for i, s in enumerate(arr):
                self.text(x + w / 2, y0 + i * lh, s, size, font=font, color=tcol)

    def sparks(self, cx, cy, r=34, n=5, color=INK):
        for i in range(n):
            a = -math.pi / 2 - 0.9 + i * 1.8 / (n - 1)
            self.line(cx + math.cos(a) * r, cy + math.sin(a) * r, cx + math.cos(a) * (r + 14), cy + math.sin(a) * (r + 14), sw=3, stroke=color, dbl=False)

    def star(self, cx, cy, r, fill="yellow"):
        pts = []
        for i in range(10):
            a = -math.pi / 2 + i * math.pi / 5
            rr = r if i % 2 == 0 else r * 0.45
            pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
        self.poly(pts, fill, sw=3)

    # ---------- salida ----------
    def svg(self):
        head = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {t} {w} {h}" width="{w}" height="{h}">'
                '<!-- Ilustración original de Juan David Rodríguez García (generada con herramientas/sketch.py) · CC BY-NC 4.0 -->').format(w=self.w, h=self.h - self.top, t=self.top)
        return head + "".join(self.o) + "</svg>"


# =====================================================================
#                         PERSONAJES Y OBJETOS
# =====================================================================

def escalado(fn):
    """Reduce temblor y grosor de trazo cuando el personaje se dibuja pequeño."""
    def w(s, cx, cy, sc=1.0, *a, **kw):
        old = (s.ka, s.ks)
        s.ka = min(1.0, sc * 1.3)
        s.ks = max(0.55, min(1.0, sc * 1.2))
        try:
            return fn(s, cx, cy, sc, *a, **kw)
        finally:
            s.ka, s.ks = old
    w.__name__ = fn.__name__
    w.__doc__ = fn.__doc__
    return w


@escalado
def robot(s, cx, cy, sc=1.0, color="blue", mood="happy", arms="down", label=None):
    """Robot simpático. (cx,cy) = centro de la cabeza."""
    k = sc
    # antena
    s.line(cx, cy - 55 * k, cx, cy - 82 * k, sw=3)
    s.ellipse(cx, cy - 88 * k, 8 * k, 8 * k, "red", sw=3)
    # cuerpo
    s.rect(cx - 42 * k, cy + 52 * k, 84 * k, 92 * k, color, r=14)
    s.rect(cx - 20 * k, cy + 78 * k, 40 * k, 26 * k, "white", r=6, sw=2.6)
    s.dot(cx - 8 * k, cy + 91 * k, 3.2)
    s.dot(cx + 8 * k, cy + 91 * k, 3.2, "red")
    # brazos
    if arms == "up":
        s.line(cx - 42 * k, cy + 70 * k, cx - 78 * k, cy + 20 * k)
        s.line(cx + 42 * k, cy + 70 * k, cx + 78 * k, cy + 20 * k)
        s.ellipse(cx - 80 * k, cy + 16 * k, 9 * k, 9 * k, "gray", sw=3)
        s.ellipse(cx + 80 * k, cy + 16 * k, 9 * k, 9 * k, "gray", sw=3)
    elif arms == "wide":
        s.line(cx - 42 * k, cy + 82 * k, cx - 95 * k, cy + 70 * k)
        s.line(cx + 42 * k, cy + 82 * k, cx + 95 * k, cy + 70 * k)
        s.ellipse(cx - 98 * k, cy + 69 * k, 9 * k, 9 * k, "gray", sw=3)
        s.ellipse(cx + 98 * k, cy + 69 * k, 9 * k, 9 * k, "gray", sw=3)
    else:
        s.line(cx - 42 * k, cy + 76 * k, cx - 64 * k, cy + 128 * k)
        s.line(cx + 42 * k, cy + 76 * k, cx + 64 * k, cy + 128 * k)
        s.ellipse(cx - 65 * k, cy + 132 * k, 9 * k, 9 * k, "gray", sw=3)
        s.ellipse(cx + 65 * k, cy + 132 * k, 9 * k, 9 * k, "gray", sw=3)
    # patas
    s.line(cx - 20 * k, cy + 144 * k, cx - 20 * k, cy + 168 * k)
    s.line(cx + 20 * k, cy + 144 * k, cx + 20 * k, cy + 168 * k)
    s.rect(cx - 34 * k, cy + 166 * k, 26 * k, 12 * k, "gray", r=5, sw=2.8)
    s.rect(cx + 8 * k, cy + 166 * k, 26 * k, 12 * k, "gray", r=5, sw=2.8)
    # cabeza
    s.rect(cx - 52 * k, cy - 52 * k, 104 * k, 100 * k, color, r=24)
    ey = cy - 12 * k
    if mood == "surprised":
        s.ellipse(cx - 20 * k, ey, 12 * k, 14 * k, "white", sw=3)
        s.ellipse(cx + 20 * k, ey, 12 * k, 14 * k, "white", sw=3)
        s.dot(cx - 20 * k, ey, 4)
        s.dot(cx + 20 * k, ey, 4)
        s.ellipse(cx, cy + 24 * k, 8 * k, 10 * k, "white", sw=3)
    elif mood == "evil":
        s.ellipse(cx - 20 * k, ey, 11 * k, 9 * k, "yellow", sw=3)
        s.ellipse(cx + 20 * k, ey, 11 * k, 9 * k, "yellow", sw=3)
        s.dot(cx - 20 * k, ey, 3.5)
        s.dot(cx + 20 * k, ey, 3.5)
        s.line(cx - 34 * k, ey - 16 * k, cx - 8 * k, ey - 6 * k, sw=3.4)
        s.line(cx + 34 * k, ey - 16 * k, cx + 8 * k, ey - 6 * k, sw=3.4)
        s.polyline([(cx - 22 * k, cy + 26 * k), (cx - 10 * k, cy + 20 * k), (cx, cy + 27 * k), (cx + 10 * k, cy + 20 * k), (cx + 22 * k, cy + 26 * k)], sw=3)
    elif mood == "sad":
        s.ellipse(cx - 20 * k, ey, 10 * k, 12 * k, "white", sw=3)
        s.ellipse(cx + 20 * k, ey, 10 * k, 12 * k, "white", sw=3)
        s.dot(cx - 20 * k, ey + 3, 3.5)
        s.dot(cx + 20 * k, ey + 3, 3.5)
        s.path([(cx - 20 * k, cy + 30 * k), (cx, cy + 20 * k), (cx + 20 * k, cy + 30 * k)], sw=3.2)
    else:
        s.ellipse(cx - 20 * k, ey, 11 * k, 12 * k, "white", sw=3)
        s.ellipse(cx + 20 * k, ey, 11 * k, 12 * k, "white", sw=3)
        s.dot(cx - 18 * k, ey, 4)
        s.dot(cx + 22 * k, ey, 4)
        s.path([(cx - 22 * k, cy + 20 * k), (cx, cy + 34 * k), (cx + 22 * k, cy + 20 * k)], sw=3.2)
    if label:
        s.text(cx, cy + 206 * k, label, 24 * k, "middle", "note")


@escalado
def person(s, cx, cy, sc=1.0, shirt="orange", hair="brown", glasses=False, mood="happy", arms="down", skin="#f6d2b0", long_hair=False, label=None, beard=False):
    """Persona esquemática. (cx,cy) = centro de la cabeza."""
    k = sc
    s.line(cx - 16 * k, cy + 100 * k, cx - 18 * k, cy + 150 * k)
    s.line(cx + 16 * k, cy + 100 * k, cx + 18 * k, cy + 150 * k)
    s.rect(cx - 36 * k, cy + 40 * k, 72 * k, 72 * k, shirt, r=18)
    if arms == "up":
        s.line(cx - 36 * k, cy + 56 * k, cx - 70 * k, cy + 6 * k)
        s.line(cx + 36 * k, cy + 56 * k, cx + 70 * k, cy + 6 * k)
    elif arms == "point":
        s.line(cx - 36 * k, cy + 60 * k, cx - 60 * k, cy + 100 * k)
        s.line(cx + 36 * k, cy + 56 * k, cx + 86 * k, cy + 38 * k)
    elif arms == "wide":
        s.line(cx - 36 * k, cy + 60 * k, cx - 84 * k, cy + 48 * k)
        s.line(cx + 36 * k, cy + 60 * k, cx + 84 * k, cy + 48 * k)
    else:
        s.line(cx - 36 * k, cy + 58 * k, cx - 56 * k, cy + 100 * k)
        s.line(cx + 36 * k, cy + 58 * k, cx + 56 * k, cy + 100 * k)
    # pelo detrás
    if long_hair:
        s.rect(cx - 46 * k, cy - 38 * k, 92 * k, 62 * k, hair, r=30)
    s.ellipse(cx, cy, 36 * k, 38 * k, skin)
    if not long_hair:
        s.path([(cx - 36 * k, cy - 4 * k), (cx - 30 * k, cy - 30 * k), (cx - 6 * k, cy - 42 * k), (cx + 22 * k, cy - 36 * k), (cx + 36 * k, cy - 8 * k), (cx + 20 * k, cy - 20 * k), (cx - 8 * k, cy - 22 * k)], True, hair, INK, 3, 1)
    else:
        s.path([(cx - 36 * k, cy + 4 * k), (cx - 30 * k, cy - 30 * k), (cx, cy - 42 * k), (cx + 30 * k, cy - 30 * k), (cx + 36 * k, cy + 4 * k), (cx + 20 * k, cy - 18 * k), (cx - 20 * k, cy - 18 * k)], True, hair, INK, 3, 1)
    if beard:
        s.path([(cx - 35 * k, cy + 2 * k), (cx - 31 * k, cy + 28 * k), (cx - 15 * k, cy + 46 * k), (cx, cy + 51 * k), (cx + 15 * k, cy + 46 * k),
                (cx + 31 * k, cy + 28 * k), (cx + 35 * k, cy + 2 * k), (cx + 24 * k, cy + 15 * k), (cx + 8 * k, cy + 12 * k), (cx, cy + 14 * k),
                (cx - 8 * k, cy + 12 * k), (cx - 24 * k, cy + 15 * k)], True, hair, INK, 3, 1)
    mc = "#fff3d6" if beard else INK
    ey = cy + 2 * k
    if mood == "surprised":
        s.ellipse(cx - 13 * k, ey, 6 * k, 8 * k, "white", sw=2.6)
        s.ellipse(cx + 13 * k, ey, 6 * k, 8 * k, "white", sw=2.6)
        s.dot(cx - 13 * k, ey, 2.5)
        s.dot(cx + 13 * k, ey, 2.5)
        s.ellipse(cx, cy + 22 * k, 6 * k, 8 * k, "white", sw=2.6)
    elif mood == "worried":
        s.dot(cx - 13 * k, ey, 3.5)
        s.dot(cx + 13 * k, ey, 3.5)
        s.line(cx - 20 * k, ey - 10 * k, cx - 8 * k, ey - 14 * k, sw=2.6, dbl=False)
        s.line(cx + 20 * k, ey - 10 * k, cx + 8 * k, ey - 14 * k, sw=2.6, dbl=False)
        s.path([(cx - 10 * k, cy + 26 * k), (cx, cy + 20 * k), (cx + 10 * k, cy + 26 * k)], sw=2.8)
    elif mood == "think":
        s.dot(cx - 13 * k, ey, 3.5)
        s.dot(cx + 13 * k, ey, 3.5)
        s.line(cx - 8 * k, cy + 24 * k, cx + 10 * k, cy + 22 * k, sw=2.8, dbl=False)
    else:
        s.dot(cx - 13 * k, ey, 3.5)
        s.dot(cx + 13 * k, ey, 3.5)
        s.path([(cx - 12 * k, cy + 20 * k), (cx, cy + 30 * k), (cx + 12 * k, cy + 20 * k)], sw=2.8, stroke=mc)
    if glasses:
        s.ellipse(cx - 13 * k, ey, 11 * k, 10 * k, None, sw=2.6, dbl=False)
        s.ellipse(cx + 13 * k, ey, 11 * k, 10 * k, None, sw=2.6, dbl=False)
        s.line(cx - 2 * k, ey, cx + 2 * k, ey, sw=2.6, dbl=False)
    if label:
        s.text(cx, cy + 176 * k, label, 22 * k, "middle", "note")


@escalado
def genie(s, cx, cy, sc=1.0, mood="happy", arms="up"):
    """Genio verde de la metáfora del ML (diseño propio, esquemático). (cx,cy)=centro de la cabeza."""
    k = sc
    # cola de humo
    s.path([(cx - 44 * k, cy + 92 * k), (cx + 44 * k, cy + 92 * k), (cx + 40 * k, cy + 140 * k), (cx + 20 * k, cy + 176 * k),
            (cx + 30 * k, cy + 206 * k), (cx + 8 * k, cy + 224 * k), (cx - 6 * k, cy + 200 * k), (cx - 30 * k, cy + 170 * k), (cx - 46 * k, cy + 130 * k)],
           True, "green", INK, 3.4, 1.4)
    # torso
    s.ellipse(cx, cy + 66 * k, 44 * k, 42 * k, "green")
    s.path([(cx - 34 * k, cy + 44 * k), (cx - 6 * k, cy + 96 * k), (cx + 34 * k, cy + 44 * k), (cx + 10 * k, cy + 36 * k), (cx - 10 * k, cy + 36 * k)], True, "purple", INK, 3, 1)
    s.rect(cx - 44 * k, cy + 92 * k, 88 * k, 16 * k, "orange", r=6, sw=3)
    # brazos
    if arms == "up":
        s.line(cx - 42 * k, cy + 56 * k, cx - 92 * k, cy + 14 * k, sw=3.6)
        s.line(cx + 42 * k, cy + 56 * k, cx + 92 * k, cy + 14 * k, sw=3.6)
        for sx in (-1, 1):
            s.ellipse(cx + sx * 96 * k, cy + 8 * k, 12 * k, 12 * k, "green", sw=3)
            s.line(cx + sx * 96 * k, cy - 4 * k, cx + sx * 104 * k, cy - 14 * k, sw=2.8, dbl=False)
    elif arms == "cross":
        s.line(cx - 42 * k, cy + 60 * k, cx + 20 * k, cy + 76 * k, sw=3.6)
        s.line(cx + 42 * k, cy + 60 * k, cx - 20 * k, cy + 76 * k, sw=3.6)
    elif arms == "ajusta":
        # brazo derecho extendido hacia la máquina con una llave inglesa; el izquierdo en jarras
        s.line(cx - 42 * k, cy + 60 * k, cx - 70 * k, cy + 84 * k, sw=3.6)
        s.line(cx - 70 * k, cy + 84 * k, cx - 44 * k, cy + 100 * k, sw=3.6)
        s.line(cx + 42 * k, cy + 56 * k, cx + 118 * k, cy + 40 * k, sw=3.6)
        s.ellipse(cx + 122 * k, cy + 39 * k, 11 * k, 11 * k, "green", sw=3)
        s.line(cx + 128 * k, cy + 34 * k, cx + 150 * k, cy + 8 * k, sw=6 * max(k, .6), stroke="#8a8a8a", dbl=False)
        s.ellipse(cx + 154 * k, cy + 4 * k, 10 * k, 10 * k, "gray", sw=2.6, dbl=False)
    else:
        s.line(cx - 42 * k, cy + 60 * k, cx - 78 * k, cy + 70 * k, sw=3.6)
        s.line(cx + 42 * k, cy + 60 * k, cx + 78 * k, cy + 70 * k, sw=3.6)
        s.ellipse(cx - 82 * k, cy + 70 * k, 11 * k, 11 * k, "green", sw=3)
        s.ellipse(cx + 82 * k, cy + 70 * k, 11 * k, 11 * k, "green", sw=3)
    # cabeza
    s.ellipse(cx, cy, 44 * k, 46 * k, "green")
    # copete azul
    s.path([(cx - 6 * k, cy - 44 * k), (cx + 6 * k, cy - 74 * k), (cx + 34 * k, cy - 86 * k), (cx + 28 * k, cy - 62 * k), (cx + 14 * k, cy - 44 * k)], True, "blue", INK, 3, 1)
    # pendiente
    s.ellipse(cx + 44 * k, cy + 10 * k, 6 * k, 6 * k, "yellow", sw=2.6)
    # ojos
    s.ellipse(cx - 16 * k, cy - 6 * k, 12 * k, 14 * k, "white", sw=3)
    s.ellipse(cx + 16 * k, cy - 6 * k, 12 * k, 14 * k, "white", sw=3)
    if mood == "think":
        s.dot(cx - 12 * k, cy - 12 * k, 4)
        s.dot(cx + 20 * k, cy - 12 * k, 4)
        s.line(cx - 12 * k, cy + 24 * k, cx + 12 * k, cy + 22 * k, sw=3, dbl=False)
    elif mood == "surprised":
        s.dot(cx - 16 * k, cy - 6 * k, 4)
        s.dot(cx + 16 * k, cy - 6 * k, 4)
        s.ellipse(cx, cy + 24 * k, 9 * k, 11 * k, "pink", sw=3)
    elif mood == "sad":
        s.dot(cx - 16 * k, cy - 2 * k, 4)
        s.dot(cx + 16 * k, cy - 2 * k, 4)
        s.path([(cx - 14 * k, cy + 28 * k), (cx, cy + 18 * k), (cx + 14 * k, cy + 28 * k)], sw=3.2)
    else:
        s.dot(cx - 14 * k, cy - 6 * k, 4)
        s.dot(cx + 18 * k, cy - 6 * k, 4)
        s.path([(cx - 18 * k, cy + 16 * k), (cx, cy + 34 * k), (cx + 18 * k, cy + 16 * k)], True, "pink", INK, 3, 1)


@escalado
def parrot(s, cx, cy, sc=1.0, glass=False, flip=False):
    """Loro. (cx,cy) = centro del cuerpo. glass=True lo dibuja transparente con engranajes a la vista."""
    k = sc
    f = -1 if flip else 1
    edge = "#3f88c5" if glass else INK
    glassfill = "#eaf6ff"
    # posadero
    s.line(cx - 70 * k, cy + 98 * k, cx + 80 * k, cy + 98 * k, sw=6, stroke="#8b5e3c", dbl=False)
    # cola
    s.path([(cx - f * 22 * k, cy + 44 * k), (cx - f * 58 * k, cy + 134 * k), (cx - f * 34 * k, cy + 140 * k), (cx - f * 4 * k, cy + 56 * k)], True,
           glassfill if glass else "blue", edge, 3, 1)
    # cuerpo
    s.ellipse(cx, cy, 50 * k, 64 * k, glassfill if glass else "green", stroke=edge)
    # patas
    s.line(cx - 12 * k, cy + 62 * k, cx - 12 * k, cy + 98 * k, sw=3, stroke=edge, dbl=False)
    s.line(cx + 14 * k, cy + 62 * k, cx + 14 * k, cy + 98 * k, sw=3, stroke=edge, dbl=False)
    if glass:
        gear(s, cx - 6 * k, cy + 4 * k, 22 * k, "yellow")
        gear(s, cx + f * 26 * k, cy + 34 * k, 14 * k, "orange")
        gear(s, cx - f * 24 * k, cy + 38 * k, 11 * k, "teal")
    else:
        s.path([(cx - f * 36 * k, cy - 12 * k), (cx - f * 4 * k, cy - 30 * k), (cx + f * 24 * k, cy + 8 * k), (cx - f * 4 * k, cy + 50 * k), (cx - f * 34 * k, cy + 30 * k)], True, "blue", INK, 3, 1)
    # cabeza
    hx, hy = cx + f * 28 * k, cy - 76 * k
    s.ellipse(hx, hy, 33 * k, 31 * k, glassfill if glass else "red", stroke=edge)
    # pico
    s.path([(hx + f * 22 * k, hy - 10 * k), (hx + f * 56 * k, hy + 4 * k), (hx + f * 46 * k, hy + 28 * k), (hx + f * 24 * k, hy + 14 * k)], True, "yellow", INK, 3, 1)
    s.ellipse(hx + f * 6 * k, hy - 8 * k, 9 * k, 9 * k, "white", sw=2.8)
    s.dot(hx + f * 8 * k, hy - 8 * k, 3.5)
    if glass:
        s.line(cx - 34 * k, cy - 36 * k, cx - 40 * k, cy - 6 * k, sw=4, stroke="white", dbl=False)


def gear(s, cx, cy, r, fill="yellow"):
    pts = []
    n = 8
    for i in range(n * 2):
        a = math.pi * i / n
        rr = r if i % 2 == 0 else r * 0.75
        for da in (-0.12, 0.12):
            pts.append((cx + rr * math.cos(a + da), cy + rr * math.sin(a + da)))
    s.poly(pts, fill, sw=2.6, dbl=False)
    s.ellipse(cx, cy, r * 0.3, r * 0.3, "white", sw=2.4, dbl=False)


def brain(s, cx, cy, sc=1.0, fill="pink"):
    k = sc
    pts = [(-70, 0), (-64, -32), (-40, -52), (-8, -48), (20, -58), (52, -44), (70, -14), (66, 20), (44, 44), (10, 46), (-20, 52), (-52, 38)]
    pts = [(cx + x * k, cy + y * k) for x, y in pts]
    s.path(pts, True, fill, INK, 3.4, 1.2)
    s.path([(cx - 40 * k, cy - 30 * k), (cx - 20 * k, cy - 10 * k), (cx - 40 * k, cy + 10 * k)], sw=2.6)
    s.path([(cx + 0 * k, cy - 36 * k), (cx + 14 * k, cy - 6 * k), (cx - 4 * k, cy + 26 * k)], sw=2.6)
    s.path([(cx + 44 * k, cy - 24 * k), (cx + 34 * k, cy + 4 * k), (cx + 48 * k, cy + 26 * k)], sw=2.6)


def laptop(s, x, y, w=160, h=100, screen="white"):
    s.rect(x, y, w, h, screen, r=8)
    s.poly([(x - 16, y + h + 16), (x + w + 16, y + h + 16), (x + w, y + h + 2), (x, y + h + 2)], "gray", sw=3)


def book(s, x, y, w=70, h=90, fill="blue", label=None):
    s.rect(x, y, w, h, fill, r=4)
    s.line(x + 10, y + 4, x + 10, y + h - 4, sw=2.6, dbl=False)
    if label:
        s.text(x + w / 2 + 4, y + h / 2 + 8, label, 22, font="note")


def cloud(s, cx, cy, w=160, h=80, fill="white"):
    pts = [(-.5, .3), (-.42, -.1), (-.22, -.3), (0, -.2), (.2, -.42), (.42, -.2), (.5, .12), (.38, .34), (0, .38), (-.3, .36)]
    s.path([(cx + x * w, cy + y * h * 2) for x, y in pts], True, fill, INK, 3.2, 1.2)


def thermometer(s, cx, cy, h=200, level=0.5, color="red"):
    s.rect(cx - 16, cy - h / 2, 32, h, "white", r=16)
    s.ellipse(cx, cy + h / 2 + 10, 28, 28, color)
    top = cy + h / 2 - level * h
    s.rect(cx - 8, top, 16, cy + h / 2 - top + 8, color, r=6, sw=2, dbl=False)
    for i in range(1, 5):
        yy = cy - h / 2 + i * h / 5
        s.line(cx + 16, yy, cx + 30, yy, sw=2.6, dbl=False)


def window(s, x, y, w, h, title="", fill="white", tcol="blue"):
    s.rect(x, y, w, h, fill, r=12)
    s.rect(x, y, w, 34, tcol, r=12)
    for i, c in enumerate(("red", "yellow", "green")):
        s.ellipse(x + 16 + i * 15, y + 17, 4.5, 4.5, c, sw=2, dbl=False)
    if title:
        s.text(x + 62, y + 25, title, 22, anchor="start", font="note")


def sign(s, cx, cy, txt, fill="yellow", w=150, h=60, size=26):
    s.line(cx, cy + h / 2, cx, cy + h / 2 + 70, sw=5, stroke="#8b5e3c")
    s.rect(cx - w / 2, cy - h / 2, w, h, fill, r=8)
    s.text(cx, cy + size * 0.32, txt, size, font="title")


def warning(s, cx, cy, sc=1.0):
    k = sc
    s.poly([(cx, cy - 36 * k), (cx + 40 * k, cy + 30 * k), (cx - 40 * k, cy + 30 * k)], "yellow", sw=3.4)
    s.text(cx, cy + 22 * k, "!", 40 * k, font="title")


def digit(s, cx, cy, d, size=60, wob=0.08, sw=5, color=INK, rot=None):
    """Dibuja un dígito a 'mano alzada' con variaciones aleatorias. Esqueletos simplificados."""
    sk = DIGITS[d]
    r = s.r
    ang = (rot if rot is not None else r.uniform(-0.28, 0.28))
    sx, sy = r.uniform(0.85, 1.1), r.uniform(0.9, 1.12)
    ca, sa = math.cos(ang), math.sin(ang)
    for stroke in sk:
        pts = []
        for (px, py) in stroke:
            x = (px - 0.5) * sx + r.uniform(-wob, wob)
            y = (py - 0.5) * sy + r.uniform(-wob, wob)
            pts.append((cx + size * (x * ca - y * sa), cy + size * (x * sa + y * ca)))
        s.o.append('<path d="{}" fill="none" stroke="{}" stroke-width="{}" stroke-linecap="round" stroke-linejoin="round"/>'.format(
            s._smooth(pts, False), color, sw))


def _circ(cx, cy, rx, ry, a0=0, a1=2 * math.pi, n=12):
    return [(cx + rx * math.cos(a0 + (a1 - a0) * i / n), cy + ry * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]


DIGITS = {
    0: [_circ(.5, .5, .32, .48, -1.2, -1.2 + 2 * math.pi + .25)],
    1: [[(.35, .22), (.55, .04), (.55, .5), (.55, .96)]],
    2: [[(.2, .25), (.35, .06), (.65, .06), (.8, .25), (.62, .55), (.2, .95), (.85, .95)]],
    3: [[(.2, .1), (.7, .08), (.75, .3), (.45, .5), (.78, .68), (.7, .92), (.2, .92)]],
    4: [[(.7, .96), (.7, .04), (.15, .66), (.9, .66)]],
    5: [[(.78, .06), (.28, .06), (.24, .48), (.62, .42), (.8, .66), (.6, .94), (.2, .86)]],
    6: [[(.7, .08), (.35, .3), (.22, .65), (.35, .94), (.68, .9), (.75, .62), (.5, .5), (.25, .62)]],
    7: [[(.15, .08), (.85, .08), (.5, .5), (.4, .96)]],
    8: [_circ(.5, .28, .26, .22, 0, 2 * math.pi, 10), _circ(.5, .72, .3, .24, 0, 2 * math.pi, 10)],
    9: [_circ(.5, .3, .28, .26, 0, 2 * math.pi, 10) + [(.76, .5), (.66, .96)]],
}


def marker(s, x, y, w, h, color="yellow", op=0.75):
    """Franja de rotulador para resaltar."""
    pts = [(x, y + h * .2), (x + w, y), (x + w, y + h * .85), (x, y + h)]
    s.o.append('<path d="M{} Z" fill="{}" opacity="{}"/>'.format(" L".join("{:.1f},{:.1f}".format(*p) for p in pts), col(color), op))


@escalado
def maquina(s, cx, cy, sc=1.0, estado="ajustada", salida=None, color="#dedad0"):
    """La máquina = el MODELO de ML. (cx,cy) = centro del cuerpo.
    estado: 'sin_ajustar' (mandos al azar, luz roja), 'ajustando' (chispas, luz amarilla) o 'ajustada' (mandos con marca, luz verde).
    salida: texto de la pantalla (p. ej. '7')."""
    k = sc
    # tolva de entrada
    s.poly([(cx - 128 * k, cy - 150 * k), (cx - 28 * k, cy - 150 * k), (cx - 52 * k, cy - 92 * k), (cx - 104 * k, cy - 92 * k)], "orange", sw=3.2)
    # patas
    s.line(cx - 100 * k, cy + 92 * k, cx - 100 * k, cy + 116 * k, sw=4)
    s.line(cx + 100 * k, cy + 92 * k, cx + 100 * k, cy + 116 * k, sw=4)
    s.rect(cx - 122 * k, cy + 112 * k, 44 * k, 14 * k, "gray", r=5, sw=2.8)
    s.rect(cx + 78 * k, cy + 112 * k, 44 * k, 14 * k, "gray", r=5, sw=2.8)
    # cuerpo
    s.rect(cx - 150 * k, cy - 92 * k, 300 * k, 186 * k, color, r=22)
    # pantalla
    s.rect(cx + 24 * k, cy - 70 * k, 108 * k, 64 * k, "#e8f6ff", r=8, sw=3)
    if salida:
        s.text(cx + 78 * k, cy - 22 * k, salida, 44 * k, font="title")
    # luz
    luz = {"sin_ajustar": "red", "ajustando": "yellow", "ajustada": "green"}[estado]
    s.ellipse(cx + 110 * k, cy - 84 * k, 9 * k, 9 * k, luz, sw=2.6, dbl=False)
    # engranaje decorativo
    gear(s, cx - 96 * k, cy - 34 * k, 22 * k, "yellow")
    # mandos
    angs = {"sin_ajustar": (2.6, -2.3, 1.7), "ajustando": (-0.2, 0.9, -1.6), "ajustada": (-0.7, 0.4, 1.1)}[estado]
    for i, a in enumerate(angs):
        x, y = cx - 84 * k + i * 76 * k, cy + 44 * k
        s.ellipse(x, y, 25 * k, 25 * k, "white", sw=3)
        if estado == "ajustada":
            for t in (-1.2, 0, 1.2):
                s.line(x + math.sin(t) * 29 * k, y - math.cos(t) * 29 * k, x + math.sin(t) * 36 * k, y - math.cos(t) * 36 * k, sw=2.4, stroke="#2e9e2e", dbl=False)
        s.line(x, y, x + math.sin(a) * 19 * k, y - math.cos(a) * 19 * k, sw=3.4, dbl=False)
        s.dot(x, y, 3.4)
    if estado == "ajustando":
        for (dx, dy) in ((-150, -100), (150, -104), (-158, 30)):
            s.sparks(cx + dx * k, cy + dy * k, 16 * k, 3)
