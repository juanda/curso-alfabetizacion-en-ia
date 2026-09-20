from sketch import *
from iconos import *

W, H = 900, 560


def caja(s, x, y, w, h, txt, color, size=30, font="title"):
    s.rect(x - w / 2, y - h / 2, w, h, color, r=16)
    ls = txt.split("\n")
    for i, ln in enumerate(ls):
        s.text(x, y + size * 0.32 + (i - (len(ls) - 1) / 2) * size * 1.15, ln, size, font=font)


def prog_tradicional():
    s = Sketch(1300, 520, 51)
    s.top = 100
    caja(s, 200, 190, 300, 100, "REGLAS\nresultado = a × b", "yellow", 30)
    caja(s, 200, 350, 300, 100, "DATOS\n7 × 8", "blue", 30)
    s.arrow(360, 200, 500, 250, sw=4); s.arrow(360, 340, 500, 290, sw=4)
    robot(s, 620, 190, 0.7, "gray", "happy", "down")
    s.text(620, 420, "computadora", 28, font="note")
    s.arrow(720, 270, 900, 270, sw=4)
    caja(s, 1040, 270, 280, 110, "RESPUESTA\n56", "green", 32)
    s.text(650, 490, "las reglas las escribe una persona", 32, font="note")
    return s


def digitos_variados():
    s = Sketch(1300, 560, 52)
    rows = [4, 7]
    for ri, d in enumerate(rows):
        for c in range(7):
            x, y = 100 + c * 185, 90 + ri * 190
            s.rect(x - 70, y - 70, 140, 140, "white", r=12, sw=2.8)
            digit(s, x, y, d, 92, wob=0.07, sw=6)
    s.text(650, 420, "¿Qué reglas describen todas las formas de escribir un 4? ¿y un 7?", 38, font="title")
    s.underline(150, 1150, 435, "yellow", 8)
    s.text(650, 500, "cada persona lo escribe a su manera", 34, font="note")
    return s


def ml_vs_tradicional():
    s = Sketch(1300, 640, 53)
    # arriba
    s.text(30, 50, "Programación tradicional", 38, font="title", anchor="start")
    caja(s, 130, 130, 210, 70, "REGLAS", "yellow", 30); s.text(260, 140, "+", 40, font="title")
    caja(s, 390, 130, 210, 70, "DATOS", "blue", 30)
    s.arrow(500, 130, 600, 130, sw=4)
    caja(s, 720, 130, 210, 90, "programa\n(computadora)", "gray", 26)
    s.arrow(830, 130, 930, 130, sw=4)
    caja(s, 1050, 130, 230, 70, "RESPUESTAS", "green", 30)
    s.line(30, 230, 1270, 230, sw=3, dbl=True)
    # abajo
    s.text(30, 300, "Machine Learning", 38, font="title", anchor="start")
    caja(s, 130, 400, 210, 70, "DATOS", "blue", 30); s.text(260, 410, "+", 40, font="title")
    caja(s, 390, 400, 210, 70, "RESPUESTAS", "green", 26)
    s.arrow(500, 400, 600, 400, sw=4)
    caja(s, 720, 400, 210, 90, "algoritmo\nde ML", "purple", 28)
    s.arrow(830, 400, 930, 400, sw=4)
    caja(s, 1050, 400, 230, 70, "REGLAS", "yellow", 30)
    s.text(1050, 458, "(el modelo)", 26, font="note")
    genie(s, 720, 490, 0.28, "happy", "up")
    s.text(650, 615, "en ML las reglas no las escribimos: las descubre el algoritmo a partir de ejemplos", 30, font="note")
    return s


def genio_maquina():
    s = Sketch(W, H, 54)
    s.rect(270, 150, 360, 300, "gray", r=30)
    s.rect(310, 190, 280, 210, "#cfe6f7", r=90, sw=3.4)
    genie(s, 450, 230, 0.55, "happy", "up")
    gear(s, 300, 470, 26, "yellow"); gear(s, 606, 470, 26, "orange")
    # entrada
    s.rect(30, 220, 110, 120, "white", r=10)
    digit(s, 85, 280, 7, 80, wob=0.05, sw=6, rot=0.1)
    s.arrow(150, 280, 268, 290, sw=4)
    s.text(85, 200, "entrada", 30, font="note")
    # salida
    s.arrow(632, 290, 745, 280, sw=4)
    s.rect(750, 220, 120, 120, "green", r=10)
    s.text(810, 300, "7", 80, font="title")
    s.text(810, 200, "salida", 30, font="note")
    s.text(810, 370, "93 %", 32, font="title")
    s.text(450, 110, "EL MODELO", 44, font="title")
    s.text(450, 520, "un genio que ha aprendido a reconocer, no a obedecer reglas", 28, font="note")
    return s


def entrenamiento():
    s = Sketch(1200, 560, 55)
    s.top = 90
    ex = [(4, "4"), (4, "4"), (7, "7"), (9, "9"), (7, "7"), (0, "0")]
    for i, (d, e) in enumerate(ex):
        x = 120 + i * 155
        s.rect(x - 60, 130, 120, 130, "white", r=10, sw=2.8)
        digit(s, x, 190, d, 80, wob=0.07, sw=6)
        s.rect(x - 45, 280, 90, 44, "yellow", r=10, sw=2.8)
        s.text(x, 312, "es un " + e, 26, font="title")
    s.text(600, 385, "conjunto de datos (dataset): ejemplos + etiquetas", 34, font="note")
    person(s, 150, 470, 0.5, "orange", "brown", True, "happy", "point")
    genie(s, 950, 445, 0.5, "happy", "down")
    s.text(600, 500, "la persona recopila y etiqueta los ejemplos", 30)
    return s


def aprendizaje():
    s = Sketch(1300, 520, 56)
    s.top = 70
    xs = [220, 650, 1080]
    for x in xs:
        s.rect(x - 195, 90, 390, 380, "white", r=18, sw=3)
    # panel 1
    genie(s, xs[0], 220, 0.6, "sad", "down")
    s.rect(xs[0] - 150, 130, 80, 80, "white", r=8, sw=2.8); digit(s, xs[0] - 110, 170, 7, 56, wob=.05, sw=5)
    s.bubble(xs[0] - 10, 110, 150, 60, ["¿un 1?"], tail=(xs[0] + 20, 215), size=30, font="title")
    s.text(xs[0], 445, "1. el modelo falla", 30, font="title")
    # panel 2
    gear(s, xs[1] - 40, 250, 60, "yellow"); gear(s, xs[1] + 50, 200, 42, "orange"); gear(s, xs[1] + 60, 300, 30, "teal")
    s.text(xs[1], 445, "2. el algoritmo ajusta", 30, font="title")
    s.text(xs[1], 130, "«¡ajusta!»", 32, font="note")
    # panel 3
    genie(s, xs[2], 220, 0.6, "happy", "up")
    s.bubble(xs[2] - 190, 110, 130, 60, ["¡un 7!"], tail=(xs[2] - 90, 215), size=30, font="title")
    s.text(xs[2], 445, "3. ahora acierta", 30, font="title")
    s.arrow(430, 280, 450, 280, sw=4); s.arrow(860, 280, 880, 280, sw=4)
    return s


def evaluacion():
    s = Sketch(W, H, 57)
    s.top = 85
    for i, d in enumerate((3, 8, 5)):
        x = 130 + i * 160
        s.rect(x - 60, 110, 120, 120, "white", r=10, sw=2.8)
        digit(s, x, 170, d, 76, wob=.08, sw=6)
        s.text(x, 275, "3 8 6".split()[i], 40, font="title")
        s.text(x + 44, 220, ("✓", "✓", "✗")[i], 36, font="title", color=("#2e9e2e", "#2e9e2e", "#d03030")[i])
    s.text(290, 320, "datos que el modelo NO ha visto", 30, font="note")
    genie(s, 700, 190, 0.6, "think", "cross")
    s.ellipse(700, 470, 110, 62, "green")
    s.text(700, 484, "93 %", 56, font="title")
    s.text(700, 545, "precisión: es probabilística", 26, font="note")
    s.text(190, 440, "¿generaliza?", 44, font="title")
    s.underline(60, 320, 452, "yellow", 8)
    return s


def pipeline():
    s = Sketch(1300, 460, 58)
    pasos = [("1", "Entrenamiento", "recopilar y etiquetar ejemplos", "yellow"), ("2", "Aprendizaje", "el algoritmo construye el modelo", "purple"),
             ("3", "Evaluación", "probar con datos nuevos", "green"), ("4", "Uso", "el modelo dentro de una aplicación", "blue")]
    for i, (n, t, d, c) in enumerate(pasos):
        x = 170 + i * 320
        s.rect(x - 140, 90, 280, 260, c, r=22)
        s.ellipse(x - 100, 90, 24, 24, "white"); s.text(x - 100, 100, n, 30, font="title")
        s.text(x, 160, t, 38, font="title")
        for j, ln in enumerate(wrap(d, 18)):
            s.text(x, 215 + j * 32, ln, 28)
        if i < 3:
            s.arrow(x + 145, 220, x + 175, 220, sw=4)
    s.text(650, 415, "primero enseñamos, luego comprobamos, y solo entonces usamos", 32, font="note")
    return s


def clases():
    s = Sketch(1300, 540, 59)
    for d in range(10):
        c, r = d % 5, d // 5
        x, y = 140 + c * 255, 140 + r * 240
        s.rect(x - 95, y - 85, 190, 200, "white", r=14, sw=3)
        digit(s, x, y - 15, d, 100, wob=.06, sw=7, rot=0.05)
        s.rect(x - 70, y + 60, 140, 42, "yellow", r=10, sw=2.8)
        s.text(x, y + 92, "clase " + str(d), 28, font="title")
    s.text(650, 30, "10 clases · cada una con su etiqueta", 36, font="title")
    return s


def barras(s, x0, y0, valores, wbar=44, gap=12, hmax=260, color="blue", etiquetas=None, resaltar=None):
    s.line(x0 - 10, y0, x0 + len(valores) * (wbar + gap), y0, sw=3.4)
    s.line(x0 - 10, y0, x0 - 10, y0 - hmax - 20, sw=3.4)
    for i, v in enumerate(valores):
        h = v * hmax
        x = x0 + i * (wbar + gap)
        cc = "red" if resaltar and i in resaltar else color
        s.rect(x, y0 - h, wbar, h, cc, r=4, sw=2.8)
        s.text(x + wbar / 2, y0 + 34, str(i) if etiquetas is None else etiquetas[i], 28, font="title")


def balance():
    s = Sketch(1300, 560, 60)
    s.rect(20, 20, 610, 520, "white", r=18, sw=3)
    s.rect(660, 20, 620, 520, "white", r=18, sw=3)
    s.text(325, 75, "desequilibrado", 40, font="title")
    s.text(970, 75, "equilibrado", 40, font="title")
    barras(s, 70, 430, [.3, 1.0, .35, .3, .4, .25, .05, .3, .35, .3], 40, 12, 280, "blue", None, {6})
    barras(s, 715, 430, [.7, .75, .65, .7, .72, .68, .7, .66, .74, .7], 40, 12, 280, "green")
    s.text(325, 510, "muchos 1 y casi ningún 6: al 6 lo confunde", 26, font="note")
    s.text(970, 510, "ejemplos parecidos en cada clase", 26, font="note")
    s.text(560, 200, "¿6?", 34, font="title")
    return s


def cobertura():
    s = Sketch(1300, 560, 61)
    r = s.r
    for (ox, tit, modo) in ((40, "no cubre el espacio", 0), (680, "cubre el espacio", 1)):
        s.rect(ox, 20, 580, 520, "white", r=18, sw=3)
        s.text(ox + 290, 70, tit, 40, font="title")
        s.line(ox + 40, 480, ox + 540, 480, sw=3); s.line(ox + 40, 480, ox + 40, 110, sw=3)
        s.text(ox + 290, 520, "todas las formas posibles de la clase", 24, font="note")
        for i in range(34):
            if modo == 0:
                x, y = ox + 90 + r.random() * 150, 250 + r.random() * 130
            else:
                x, y = ox + 70 + r.random() * 450, 130 + r.random() * 330
            s.ellipse(x, y, 9, 9, "blue", sw=2.4, dbl=False)
        if modo == 0:
            s.ellipse(ox + 440, 190, 12, 12, "red", sw=2.8)
            s.text(ox + 440, 160, "¿? caso nuevo", 28, font="note")
            s.arrow(ox + 410, 200, ox + 250, 280, sw=2.6, bend=10)
            s.text(ox + 360, 300, "fallará", 30, font="title", color="#d03030")
    return s


def pixeles():
    s = Sketch(1100, 560, 62)
    s.rect(30, 120, 250, 250, "white", r=12, sw=3)
    digit(s, 155, 245, 7, 190, wob=.03, sw=12, rot=.02)
    s.text(155, 410, "lo que vemos", 30, font="note")
    s.arrow(300, 245, 400, 245, sw=4)
    g = ["9999990", "0000090", "0000900", "0009000", "0090000", "0090000", "0900000"]
    for r_, row in enumerate(g):
        for c_, v in enumerate(row):
            x, y = 430 + c_ * 88, 80 + r_ * 56
            s.rect(x, y, 84, 52, "#4b4b4b" if v != "0" else "white", r=2, sw=1.8, dbl=False)
            s.text(x + 42, y + 37, v, 32, font="title", color="white" if v != "0" else "#9a9a9a")
    s.text(740, 530, "lo que ve la computadora: números", 32, font="note")
    return s


def tipos_ml():
    s = Sketch(1300, 500, 63)
    xs = [220, 650, 1080]
    tit = ["Supervisado", "No supervisado", "Por refuerzo"]
    sub = ["aprende con ejemplos etiquetados", "descubre grupos por sí mismo", "aprende por prueba y recompensa"]
    for x, t, d in zip(xs, tit, sub):
        s.rect(x - 200, 30, 400, 440, "white", r=18, sw=3)
        s.text(x, 90, t, 40, font="title")
        s.text(x, 430, d, 26, font="note")
    # supervisado
    for i, (d, e) in enumerate(((3, "3"), (8, "8"))):
        xx = 160 + i * 130
        s.rect(xx - 50, 150, 100, 100, "white", r=8, sw=2.8); digit(s, xx, 200, d, 64, sw=5)
        s.rect(xx - 40, 268, 80, 38, "yellow", r=8, sw=2.6); s.text(xx, 296, e, 28, font="title")
    # no supervisado
    for cx, cy, c in ((580, 210, "blue"), (740, 190, "orange"), (660, 320, "green")):
        s.ellipse(cx, cy, 62, 50, None, sw=2.6, stroke="#888")
        for k in range(6):
            s.ellipse(cx + s.j(40), cy + s.j(30), 7, 7, c, sw=2, dbl=False)
    # refuerzo
    robot(s, 1030, 170, 0.5, "teal", "happy", "up")
    s.star(1140, 210, 26)
    s.text(1140, 270, "+1", 34, font="title")
    return s


def lml_partes():
    s = Sketch(1300, 520, 64)
    xs = [230, 650, 1070]
    window(s, xs[0] - 190, 60, 380, 300, "learningml.org", "white", "blue")
    genie(s, xs[0], 200, 0.4, "happy", "up")
    s.text(xs[0], 320, "LearningML", 36, font="title")
    window(s, xs[1] - 190, 60, 380, 300, "editor de modelos", "white", "green")
    for i, (t, c) in enumerate((("clase A", "yellow"), ("clase B", "pink"), ("clase C", "blue"))):
        s.rect(xs[1] - 170 + i * 120, 110, 110, 190, c, r=8, sw=2.6)
        s.text(xs[1] - 115 + i * 120, 135, t, 22, font="note")
        for k in range(3):
            s.rect(xs[1] - 156 + i * 120, 155 + k * 44, 84, 34, "white", r=4, sw=2, dbl=False)
    s.rect(xs[1] - 100, 315, 200, 34, "orange", r=10, sw=2.6); s.text(xs[1], 340, "aprender a reconocer", 22, font="note")
    window(s, xs[2] - 190, 60, 380, 300, "editor de programación", "white", "purple")
    for i, (t, c) in enumerate((("al hacer clic en 🏴", "yellow"), ("preguntar y esperar", "blue"), ("reconocer con el modelo", "green"), ("decir resultado", "purple"))):
        s.rect(xs[2] - 150, 110 + i * 56, 300, 46, c, r=8, sw=2.6)
        s.text(xs[2], 141 + i * 56, t.replace(" 🏴", ""), 24, font="body")
    for x, t in zip(xs, ("1 · La web", "2 · Editor de modelos", "3 · Programar (Scratch)")):
        s.text(x, 420, t, 32, font="title")
    s.text(650, 490, "tres piezas: informarse, crear el modelo, programar la aplicación", 28, font="note")
    return s


def lml_historia():
    s = Sketch(1300, 560, 65)
    ev = [("2018", "nace la idea (INTEF)", "yellow", 1), ("2019", "primeros prototipos y pruebas", "orange", -1),
          ("2020", "primera versión y artículo en RED", "pink", 1), ("2021", "evaluación con estudiantes", "purple", -1),
          ("2022", "versión de escritorio y 2.0", "blue", 1), ("2024", "premio All Digital al mejor recurso educativo", "green", -1)]
    timeline(s, ev, 285, 130, 210, 27, 17, 40)
    s.star(130 + 5 * 210, 285, 22, "yellow")
    return s


def construccionismo():
    s = Sketch(W, H, 66)
    person(s, 150, 230, 0.95, "orange", "brown", True, "happy", "up")
    # bloques
    for (x, y, w, h, c) in ((330, 430, 90, 60, "yellow"), (430, 430, 90, 60, "blue"), (380, 370, 90, 60, "green"), (480, 370, 90, 60, "pink"), (430, 310, 90, 60, "purple")):
        s.rect(x, y, w, h, c, r=6)
    genie(s, 700, 200, 0.6, "happy", "up")
    person(s, 800, 400, 0.4, "pink", "#5a3b22", False, "surprised", "up", long_hair=True)
    s.bubble(60, 20, 300, 76, ["¡Mira lo que", "he construido!"], tail=(150, 140), size=28, font="title")
    s.text(450, 520, "aprender construyendo algo que se puede compartir", 32, font="note")
    s.text(470, 290, "mi modelo", 28, font="note")
    return s


def clasificaciones():
    s = Sketch(1300, 560, 67)
    cards = [("Estilos artísticos", ["impresionismo", "cubismo", "surrealismo"], i_paleta, "yellow"),
             ("Tipos de textos", ["narrativo", "poema", "noticia"], i_doc, "blue"),
             ("Elementos electrónicos", ["resistencia", "condensador", "LED"], i_bombilla, "green"),
             ("Edades de la historia", ["Paleolítico", "Neolítico", "Edad de los metales"], i_libro, "pink")]
    for i, (t, chips, ic, c) in enumerate(cards):
        x = 170 + i * 320
        s.rect(x - 150, 30, 300, 500, "white", r=18, sw=3)
        ic(s, x, 110, 1.1)
        for j, ln in enumerate(wrap(t, 14)):
            s.text(x, 200 + j * 36, ln, 34, font="title")
        for j, ch in enumerate(chips):
            s.rect(x - 125, 290 + j * 68, 250, 52, c, r=14, sw=2.8)
            s.text(x, 326 + j * 68, ch, 28)
    return s


def ciclo():
    s = Sketch(1100, 600, 68)
    genie(s, 550, 250, 0.55, "happy", "up")
    pasos = [(550, 60, "1 · Aprendo el tema", "yellow"), (900, 220, "2 · Recopilo y clasifico\nejemplos (entrenamiento)", "orange"),
             (830, 470, "3 · La máquina aprende\n(algoritmo → modelo)", "purple"), (270, 470, "4 · Evalúo el modelo", "green"),
             (200, 220, "5 · Lo uso en una\naplicación (Scratch)", "blue")]
    for x, y, t, c in pasos:
        ls = t.split("\n")
        w = 350
        s.rect(x - w / 2, y - 34, w, 46 + 30 * len(ls), c, r=18)
        for i, ln in enumerate(ls):
            s.text(x, y + 6 + i * 30, ln, 27, font="title")
    s.arrow(700, 75, 800, 170, bend=-20); s.arrow(920, 300, 880, 440, bend=-20)
    s.arrow(680, 490, 420, 490, bend=15); s.arrow(220, 440, 200, 320, bend=-20)
    s.arrow(300, 160, 400, 75, bend=-20)
    s.text(550, 580, "…y si falla, mejoro los datos y vuelvo a empezar", 30, font="note")
    return s


def scratch_bloques():
    s = Sketch(1000, 560, 69)
    bl = [("al hacer clic en la bandera", "yellow"), ("preguntar «¿qué quieres?» y esperar", "blue"), ("reconocer texto (respuesta)\ncon el modelo de ML", "green"),
          ("si resultado = «enciende la lámpara»", "orange"), ("   mostrar la lámpara", "purple")]
    y = 40
    for i, (t, c) in enumerate(bl):
        ls = t.split("\n")
        h = 26 + 34 * len(ls)
        s.rect(60 + (40 if i == 4 else 0), y, 600 - (40 if i == 4 else 0), h, c, r=14)
        for j, ln in enumerate(ls):
            s.text(90 + (40 if i == 4 else 0), y + 38 + j * 34, ln.strip(), 30, anchor="start", font="body")
        y += h + 14
    genie(s, 830, 200, 0.75, "happy", "up")
    s.text(830, 460, "el modelo hace de «cerebro»", 28, font="note")
    return s


ESCENAS = {"prog-tradicional": prog_tradicional, "digitos-variados": digitos_variados, "ml-vs-tradicional": ml_vs_tradicional,
           "genio-maquina": genio_maquina, "entrenamiento": entrenamiento, "aprendizaje": aprendizaje, "evaluacion": evaluacion,
           "pipeline": pipeline, "clases": clases, "balance": balance, "cobertura": cobertura, "pixeles": pixeles, "tipos-ml": tipos_ml,
           "lml-partes": lml_partes, "lml-historia": lml_historia, "construccionismo": construccionismo, "clasificaciones": clasificaciones,
           "ciclo": ciclo, "scratch-bloques": scratch_bloques}
