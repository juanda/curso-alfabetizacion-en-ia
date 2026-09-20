from sketch import *
from iconos import *
from escenas_3 import caja, barras

W, H = 900, 560


def asistente():
    s = Sketch(1200, 560, 71)
    person(s, 110, 250, 0.9, "orange", "brown", True, "happy", "point")
    s.bubble(40, 40, 400, 90, ["«¿Podrías encender", "la lámpara, por favor?»"], tail=(120, 190), size=30, font="title")
    s.arrow(210, 300, 430, 300, sw=4)
    maquina(s, 560, 270, 0.5, "ajustada", "ON")
    s.text(560, 470, "modelo de texto (la máquina)", 30, font="title")
    s.arrow(650, 300, 830, 300, sw=4)
    i_lampara(s, 920, 250, 1.6, True)
    i_ventilador(s, 1100, 260, 1.4)
    s.text(920, 440, "encender luz", 26, font="note"); s.text(1100, 440, "apagar ventilador", 26, font="note")
    s.text(600, 530, "4 clases: encender/apagar luz · encender/apagar ventilador", 30, font="note")
    return s


def cuadro(s, x, y, w, h, tipo):
    s.rect(x, y, w, h, "white", r=4, sw=5)
    r = s.r
    if tipo == "impresionismo":
        for i in range(46):
            s.ellipse(x + 14 + r.random() * (w - 28), y + 14 + r.random() * (h - 28), 9, 6, r.choice(["blue", "yellow", "green", "pink", "orange"]), sw=1.4, dbl=False)
    elif tipo == "cubismo":
        s.poly([(x + 20, y + 20), (x + w / 2, y + 30), (x + w / 2 - 20, y + h - 20), (x + 30, y + h - 40)], "orange", sw=2.4)
        s.poly([(x + w / 2, y + 30), (x + w - 20, y + 60), (x + w - 40, y + h - 30), (x + w / 2 - 20, y + h - 20)], "blue", sw=2.4)
        s.poly([(x + w / 2 - 30, y + 70), (x + w / 2 + 30, y + 90), (x + w / 2 + 10, y + 130)], "yellow", sw=2.4)
    elif tipo == "expresionismo":
        s.o.append('<rect x="{}" y="{}" width="{}" height="{}" fill="#ffd0a0" opacity=".55"/>'.format(x + 4, y + 4, w - 8, h - 8))
        for k, c in enumerate(("#f0645a", "#ff9d5c", "#5a8fd8", "#f0645a")):
            yy = y + 40 + k * 44
            pts = [(x + 14, yy), (x + w * .3, yy - 26), (x + w * .55, yy + 26), (x + w * .8, yy - 22), (x + w - 14, yy + 6)]
            s.path(pts, False, None, stroke=c, sw=9, amp=2, dbl=False)
        s.ellipse(x + w / 2, y + h - 52, 20, 26, "#cfe6f7", sw=3)
        s.ellipse(x + w / 2 - 7, y + h - 58, 3, 4, "#333", dbl=False, sw=2); s.ellipse(x + w / 2 + 7, y + h - 58, 3, 4, "#333", dbl=False, sw=2)
    elif tipo == "pop":
        for i in range(5):
            for j in range(5):
                s.ellipse(x + 26 + i * (w - 52) / 4, y + 26 + j * (h - 52) / 4, 6, 6, "pink", sw=1.2, dbl=False)
        s.star(x + w / 2, y + h / 2, 62, "yellow")
        s.text(x + w / 2, y + h / 2 + 12, "POP!", 34, font="title", color="#d0302a")
    else:  # realismo: casa, árbol y cielo, todo muy ordenado
        s.rect(x + 8, y + 8, w - 16, h * .55, "#cfe6f7", r=2, sw=1.6, dbl=False)
        s.rect(x + 8, y + h * .58, w - 16, h * .38, "#b8dd8a", r=2, sw=1.6, dbl=False)
        s.rect(x + 34, y + h * .38, 92, 66, "#f3e2c0", r=2, sw=2.6)
        s.poly([(x + 26, y + h * .38), (x + 80, y + h * .38 - 38), (x + 134, y + h * .38)], "#c0503a", sw=2.6)
        s.rect(x + 66, y + h * .38 + 24, 24, 42, "#8b5e3c", r=2, sw=2.2, dbl=False)
        s.line(x + w - 50, y + h * .5, x + w - 50, y + h * .8, sw=5, stroke="#8b5e3c")
        s.ellipse(x + w - 50, y + h * .42, 30, 34, "green", sw=2.6)


def estilos():
    s = Sketch(1300, 560, 72)
    nombres = ["cubismo", "expresionismo", "impresionismo", "pop", "realismo"]
    for i, n in enumerate(nombres):
        x = 25 + i * 252
        cuadro(s, x, 40, 230, 230, n)
        s.text(x + 115, 318, n, 32, font="title")
    s.text(390, 430, "5 clases · unas 15 imágenes por estilo", 32, font="note")
    s.text(390, 470, "+ imágenes de prueba para evaluar", 28, font="note")
    maquina(s, 1050, 460, 0.42, "ajustada", "?")
    s.bubble(830, 350, 250, 56, ["¿qué estilo es?"], tail=(1030, 415), size=30, font="title")
    return s


def camaleon():
    s = Sketch(W, H, 73)
    s.rect(60, 40, 780, 300, "#fde9a8", r=20)
    s.line(140, 300, 780, 300, sw=8, stroke="#8b5e3c")
    # camaleón
    s.path([(360, 300), (330, 240), (370, 190), (450, 170), (540, 190), (580, 250), (560, 300)], True, "green", INK, 3.6, 1.2)
    s.ellipse(570, 200, 50, 40, "green"); s.ellipse(582, 190, 18, 18, "white"); s.dot(586, 192, 6)
    s.path([(360, 290), (300, 300), (270, 270), (290, 245), (312, 262)], False, None, INK, 5, 1)
    s.line(600, 218, 640, 226, sw=3)
    s.text(450, 92, "el camaleón toma el color de lo que ve", 34, font="title")
    i_camara(s, 130, 430, 1.1)
    for i, c in enumerate(("red", "blue", "green", "yellow")):
        s.rect(260 + i * 130, 390, 100, 100, c, r=8)
    s.arrow(200, 430, 250, 440, sw=3)
    s.text(450, 535, "modelo de imágenes: una clase por cada color", 28, font="note")
    return s


def cuadrantes():
    s = Sketch(1100, 600, 74)
    ox, oy, u = 550, 290, 50
    s.rect(ox, oy - 250, 480, 250, "#fff0c2", r=2, sw=0); s.rect(ox - 480, oy - 250, 480, 250, "#d6ecfb", r=2, sw=0)
    s.rect(ox - 480, oy, 480, 250, "#ffd6de", r=2, sw=0); s.rect(ox, oy, 480, 250, "#d9f2b8", r=2, sw=0)
    s.arrow(ox - 500, oy, ox + 500, oy, sw=3.6); s.arrow(ox, oy + 262, ox, oy - 262, sw=3.6)
    s.text(ox + 480, oy + 34, "x", 34, font="title"); s.text(ox + 24, oy - 240, "y", 34, font="title")
    for t, x, y in (("1.º cuadrante", ox + 330, oy - 215), ("2.º cuadrante", ox - 330, oy - 215), ("3.º cuadrante", ox - 330, oy + 232), ("4.º cuadrante", ox + 330, oy + 232)):
        s.text(x, y, t, 32, font="title")
    pts = [(3, 4), (2, 2), (6, 1), (-2, 4), (-5, 2), (-3, 1), (-4, -3), (-2, -4), (-6, -1), (5, -2), (2, -4), (7, -3)]
    for (a, b) in pts:
        s.ellipse(ox + a * u, oy - b * u, 8, 8, "#333", sw=2, dbl=False)
    s.ellipse(ox - 3 * u, oy - 2 * u, 12, 12, "red", sw=2.8)
    s.bubble(ox - 490, oy - 120, 190, 70, ["(−3, 2) → ¿?"], tail=(ox - 3 * u - 12, oy - 2 * u + 4), size=28, font="title")
    s.text(550, 588, "entrada: dos números (x, y) · salida: el cuadrante", 30, font="note")
    return s


def autocompletar():
    s = Sketch(W, H, 75)
    s.rect(270, 30, 360, 500, "gray", r=40)
    s.rect(290, 70, 320, 300, "white", r=14, sw=2.8)
    s.text(450, 130, "Nos vemos mañana", 28, font="note"); s.text(450, 166, "en el ...", 30, font="note")
    for i, w in enumerate(("cole", "parque", "cine")):
        s.rect(298 + i * 104, 390, 96, 46, "blue", r=12, sw=2.8)
        s.text(346 + i * 104, 421, w, 26)
    s.text(450, 480, "teclado predictivo", 28, font="title")
    s.text(140, 250, "un LLM es", 36, font="title"); s.text(140, 292, "un teclado", 36, font="title"); s.text(140, 334, "predictivo", 36, font="title")
    s.text(760, 250, "…gigante", 42, font="title", color="#d0682c")
    s.arrow(680, 260, 640, 280, sw=3)
    return s


def entrenamiento_llm():
    s = Sketch(1300, 640, 76)
    for i, (f, y) in enumerate(((i_libro, 100), (lambda s, x, y, k: window(s, x - 50, y - 36, 100, 72, "web"), 210), (i_doc, 320))):
        f(s, 90, y, 1.0)
    s.text(90, 400, "casi todo lo", 26, font="note"); s.text(90, 428, "escrito", 26, font="note")
    s.arrow(160, 200, 330, 200, sw=4)
    genie(s, 470, 130, 0.62, "think", "ajusta")
    s.text(470, 380, "el genio", 32, font="title"); s.text(470, 412, "ajusta la máquina", 26, font="note")
    maquina(s, 960, 220, 0.85, "ajustando", "…")
    s.text(960, 380, "el modelo (LLM)", 32, font="title"); s.text(960, 412, "una máquina enorme", 26, font="note")
    ys = 500
    ws = ["El", "gato", "se", "sienta", "en", "el"]
    for i, w in enumerate(ws):
        s.rect(80 + i * 130, ys, 116, 56, "white", r=10, sw=2.8)
        s.text(138 + i * 130, ys + 38, w, 32)
    s.arrow(880, ys + 28, 960, ys + 28, sw=3)
    s.rect(970, ys, 150, 56, "green", r=10)
    s.text(1045, ys + 38, "sofá", 32, font="title")
    s.text(1045, ys - 14, "etiqueta", 26, font="note")
    s.text(500, 620, "el texto se etiqueta a sí mismo: la etiqueta es la palabra siguiente", 28, font="note")
    return s


def probabilidades():
    s = Sketch(1000, 560, 77)
    s.text(500, 60, "El gato se sienta en el ...", 48, font="title")
    datos = [("sofá", .40), ("suelo", .25), ("tejado", .15), ("jardín", .10), ("coche", .06), ("zapato", .03), ("otras…", .01)]
    for i, (w, p) in enumerate(datos):
        y = 120 + i * 58
        s.text(150, y + 34, w, 32, anchor="end")
        s.rect(170, y, max(8, p * 640), 44, "blue" if i else "green", r=6, sw=2.8)
        s.text(170 + max(8, p * 640) + 14, y + 34, "{} %".format(int(p * 100)), 30, anchor="start", font="title")
    s.text(500, 540, "el modelo no decide: calcula probabilidades", 30, font="note")
    return s


def temperatura():
    s = Sketch(1300, 560, 78)
    for ox, tit, lvl, col_, vals, txt in ((30, "temperatura baja", .15, "blue", [.7, .15, .08, .04, .03], "«El gato se sienta en el sofá.»\n(siempre lo más probable: previsible)"),
                                           (670, "temperatura alta", .9, "red", [.24, .21, .2, .18, .17], "«El gato se sienta en el submarino…»\n(más variedad: creativo o disparatado)")):
        s.rect(ox, 20, 600, 520, "white", r=18, sw=3)
        s.text(ox + 300, 75, tit, 40, font="title")
        thermometer(s, ox + 90, 250, 220, lvl, col_)
        for i, v in enumerate(vals):
            s.rect(ox + 200 + i * 76, 380 - v * 260, 60, v * 260, "green" if i == 0 else "blue", r=4, sw=2.6)
        s.line(ox + 190, 380, ox + 590, 380, sw=3)
        for j, ln in enumerate(txt.split("\n")):
            s.text(ox + 300, 450 + j * 36, ln, 26 if j == 0 else 24, font="title" if j == 0 else "note")
    return s


def bucle():
    s = Sketch(1300, 560, 79)
    frase = ["El", "gato", "se", "sienta", "en", "el", "sofá"]
    for r_ in range(1, 6):
        y = 30 + (r_ - 1) * 100
        x = 60
        for i in range(r_ + 1):
            w = frase[i]
            wd = 34 + len(w) * 20
            new = (i == r_)
            s.rect(x, y, wd, 60, "yellow" if new else "white", r=12, sw=3 if new else 2.6)
            s.text(x + wd / 2, y + 42, w, 34, font="title" if new else "body")
            x += wd + 14
        if r_ < 5:
            s.arrow(120, y + 66, 120, y + 96, sw=2.6, head=10)
    s.text(1000, 140, "cada palabra elegida", 34, font="title")
    s.text(1000, 184, "pasa a formar parte", 34, font="title")
    s.text(1000, 228, "del contexto", 34, font="title")
    parrot(s, 1080, 400, 0.8, glass=False)
    s.text(650, 540, "prompt → palabra → nuevo contexto → palabra → …", 30, font="note")
    return s


def loro():
    s = Sketch(W, H, 80)
    person(s, 130, 230, 0.9, "orange", "brown", True, "think", "point")
    s.bubble(30, 30, 330, 80, ["«¿Cuánto es 17 × 23?»"], tail=(120, 180), size=28, font="title")
    parrot(s, 640, 260, 1.15, glass=False)
    s.bubble(480, 30, 340, 70, ["«¡391!»… ¿o «¡401!»?"], tail=(600, 130), size=28, font="title")
    s.text(450, 500, "suena seguro, pero solo sigue lo más probable", 32, font="note")
    s.text(450, 540, "«loros estocásticos» (Bender et al., 2021)", 26, font="note")
    return s


def loro_cristal():
    s = Sketch(W, H, 81)
    parrot(s, 450, 300, 1.5, glass=True)
    labs = [(140, 130, "textos de\nentrenamiento", 340, 260), (770, 130, "n-gramas\n(contexto)", 480, 290), (140, 430, "probabilidades", 400, 350), (770, 430, "temperatura", 500, 330)]
    for x, y, t, tx, ty in labs:
        for j, ln in enumerate(t.split("\n")):
            s.text(x, y + j * 32, ln, 30, font="title")
        s.arrow(x + (70 if x < 450 else -70), y + 20, tx, ty, sw=3, bend=15)
    s.text(450, 40, "GlassParrot: un loro de cristal", 40, font="title")
    return s


def ngrama():
    s = Sketch(1300, 560, 82)
    s.rect(30, 40, 420, 240, "white", r=16, sw=3)
    s.text(240, 90, "texto de entrenamiento", 30, font="title")
    for i, ln in enumerate(("el gato duerme en el sofá", "el gato come en la cocina", "el perro duerme en el suelo")):
        s.text(240, 150 + i * 42, ln, 28)
    s.arrow(460, 160, 560, 160, sw=4)
    s.rect(570, 40, 320, 240, "yellow", r=16)
    s.text(730, 90, "n-grama (n = 2)", 30, font="title")
    s.rect(610, 120, 240, 60, "white", r=12, sw=2.8)
    s.text(730, 162, "«el gato»", 34, font="title")
    s.text(730, 230, "las 2 últimas palabras", 26, font="note")
    s.arrow(900, 160, 990, 160, sw=4)
    s.rect(1000, 40, 270, 240, "green", r=16)
    s.text(1135, 90, "siguiente palabra", 28, font="title")
    barras(s, 1030, 230, [.5, .5], 80, 30, 90, "blue", ["duerme", "come"])
    s.text(650, 380, "«duerme»: 50 %      «come»: 50 %", 34, font="title")
    s.text(650, 440, "si el n-grama no aparece en los datos, prueba con uno más corto", 30, font="note")
    s.text(650, 500, "El loro no entiende: cuenta y repite lo que ha visto", 34, font="title")
    s.underline(200, 1100, 512, "yellow", 8)
    return s


def glassparrot_ui():
    s = Sketch(1300, 600, 83)
    window(s, 30, 30, 1240, 540, "GlassParrot", "white", "teal")
    s.text(320, 100, "Entrenamiento", 34, font="title"); s.text(930, 100, "Prueba", 34, font="title")
    s.rect(60, 120, 520, 230, "#f7f7f2", r=10, sw=2.8)
    s.text(320, 240, "«Escribe texto de entrenamiento…»", 26, font="note", color="#999")
    for i, (t, c) in enumerate((("Añadir texto", "blue"), ("Subir", "yellow"), ("Borrar ejemplos", "pink"))):
        s.rect(60 + i * 175, 372, 165, 46, c, r=10, sw=2.8); s.text(142 + i * 175, 404, t, 24)
    s.rect(60, 436, 400, 46, "gray", r=10, sw=2.8); s.text(260, 468, "Ejemplos predefinidos ▾", 24)
    s.rect(60, 500, 160, 50, "green", r=12); s.text(140, 535, "Entrenar", 28, font="title")
    s.rect(680, 120, 500, 60, "white", r=10, sw=2.8); s.text(930, 160, "El gato se sienta en el", 28)
    s.rect(680, 196, 260, 46, "orange", r=10, sw=2.8); s.text(810, 228, "Generar siguiente palabra", 22)
    for i, (w, p) in enumerate((("sofá", .5), ("suelo", .3), ("tejado", .2))):
        s.text(760, 300 + i * 50, w, 26, anchor="end"); s.rect(776, 274 + i * 50, p * 380, 36, "blue", r=6, sw=2.6)
    s.rect(1000, 196, 200, 46, "purple", r=12, sw=2.8); s.text(1100, 228, "Modo avanzado", 24)
    for n, (x, y) in enumerate(((40, 130), (40, 380), (660, 130), (660, 270))):
        s.ellipse(x, y, 20, 20, "red", sw=2.8); s.text(x, y + 10, str(n + 1), 28, font="title", color="white")
    return s


ESCENAS = {"asistente": asistente, "estilos": estilos, "camaleon": camaleon, "cuadrantes": cuadrantes, "autocompletar": autocompletar,
           "entrenamiento-llm": entrenamiento_llm, "probabilidades": probabilidades, "temperatura": temperatura, "bucle": bucle, "loro": loro,
           "loro-cristal": loro_cristal, "ngrama": ngrama, "glassparrot-ui": glassparrot_ui}
