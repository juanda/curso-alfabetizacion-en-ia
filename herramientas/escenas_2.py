from sketch import *
from iconos import *

W, H = 900, 560


def linea_ia():
    s = Sketch(1250, 560, 31)
    ev = [("2012", "el deep learning despega", "yellow", 1),
          ("2015", "reconocen imágenes como una persona", "orange", -1),
          ("2016", "AlphaGo vence a Lee Sedol", "pink", 1),
          ("2017", "nace la arquitectura Transformer", "purple", -1),
          ("2020", "GPT-3 y LearningML", "blue", 1),
          ("2022", "ChatGPT llega a todo el mundo", "green", -1),
          ("2025", "la era de los agentes", "teal", 1),
          ("2026", "agentes fuera de control", "red", -1)]
    timeline(s, ev, 280, 100, 150, 28, 20, 38)
    return s


def pioneros():
    s = Sketch(W, H, 32)
    genie(s, 450, 90, 0.5, "happy", "up")
    datos = [(130, "orange", "brown", True, "Jesús"), (320, "green", "#5a3b22", False, "Gregorio"), (580, "purple", "#c0a060", False, "Marcos"), (770, "blue", "#5a3b22", True, "Juan David")]
    for x, sh, ha, gl, n in datos:
        person(s, x, 250, 0.85, sh, ha, gl, "happy", "down", beard=(n == "Juan David"))
    s.rect(60, 410, 780, 26, "#d9b382", r=6)
    laptop(s, 390, 350, 120, 50)
    for x, n in ((130, "Jesús Moreno"), (320, "Gregorio Robles"), (580, "Marcos Román"), (770, "Juan David R.")):
        s.text(x, 486, n, 26, font="note")
    s.text(450, 536, "llevar el Machine Learning al aula", 32, font="title")
    return s


def eclipse():
    s = Sketch(W, H, 33)
    for a in range(0, 360, 30):
        r = math.radians(a)
        s.line(680 + math.cos(r) * 150, 170 + math.sin(r) * 150, 680 + math.cos(r) * 190, 170 + math.sin(r) * 190, sw=4, stroke="#e0a800", dbl=False)
    s.ellipse(680, 170, 130, 130, "yellow", sw=4)
    s.text(680, 165, "IA", 60, font="title")
    s.text(680, 210, "generativa", 34, font="title")
    s.o.append('<ellipse cx="300" cy="440" rx="250" ry="70" fill="#000" opacity="0.13"/>')
    s.rect(240, 410, 80, 70, "#c07a4a", r=6)
    s.line(280, 410, 280, 320, sw=4)
    s.path([(280, 350), (230, 330), (240, 290), (278, 320)], True, "green", INK, 3, 1)
    s.path([(282, 336), (330, 320), (334, 282), (288, 310)], True, "green", INK, 3, 1)
    s.text(280, 520, "alfabetización en IA (ML)", 30, font="title")
    s.arrow(600, 250, 400, 350, bend=-20, sw=3)
    return s


def caja_negra():
    s = Sketch(W, H, 34)
    i_caja(s, 450, 250, 2.6)
    person(s, 100, 220, 0.9, "orange", "brown", False, "think", "point")
    s.arrow(210, 250, 340, 250, sw=4)
    s.text(270, 235, "pregunta", 28, font="note")
    s.arrow(560, 250, 690, 250, sw=4)
    s.text(630, 235, "respuesta", 28, font="note")
    s.bubble(690, 160, 190, 80, ["¡Suena muy", "convincente!"], tail=(700, 250), size=24)
    s.text(450, 470, "no vemos qué pasa dentro", 36, font="title")
    s.underline(250, 650, 480, "yellow", 8)
    return s


def maquina_habla():
    s = Sketch(W, H, 35)
    robot(s, 620, 230, 1.0, "blue", "happy", "up")
    person(s, 190, 270, 0.95, "orange", "brown", True, "surprised", "up")
    s.bubble(380, 40, 380, 90, ["Hola, soy una IA.", "¿En qué te ayudo?"], tail=(560, 170), size=32, font="title")
    s.text(450, 520, "30 de noviembre de 2022: la máquina consigue hablar", 30, font="note")
    return s


def historia_escritura():
    s = Sketch(1300, 500, 36)
    xs = [130, 450, 770, 1090]
    # tablilla
    s.rect(xs[0] - 55, 130, 110, 100, "#d9b382", r=12)
    s.text(xs[0], 200, "A B", 46, font="title")
    # imprenta
    s.rect(xs[1] - 60, 190, 120, 40, "gray", r=6)
    s.line(xs[1], 190, xs[1], 120, sw=6)
    s.line(xs[1] - 30, 120, xs[1] + 30, 120, sw=6)
    s.rect(xs[1] - 45, 150, 90, 30, "white", r=4, sw=2.6)
    # ordenador
    laptop(s, xs[2] - 60, 130, 120, 80)
    s.text(xs[2], 180, "0110", 28, font="title")
    # robot
    robot(s, xs[3], 130, 0.5, "blue", "happy", "up")
    tit = ["Alfabeto", "Imprenta", "Computadora", "IA generativa"]
    sub = ["almacenar y transmitir el conocimiento", "democratizar la cultura", "escribir y procesar de forma automática", "entrenada con casi todo lo escrito"]
    for i, x in enumerate(xs):
        s.text(x, 340, tit[i], 40, font="title")
        for j, ln in enumerate(wrap(sub[i], 22)):
            s.text(x, 380 + j * 30, ln, 26)
        if i < 3:
            s.arrow(x + 110, 180, xs[i + 1] - 110, 180, sw=4)
    s.text(650, 470, "más de 3.500 años de historia", 34, font="note")
    return s


def mago():
    s = Sketch(W, H, 37)
    s.poly([(0, 470), (900, 470), (900, 560), (0, 560)], "#8d6e63", sw=3)
    robot(s, 330, 200, 0.9, "purple", "happy", "up")
    # sombrero de copa
    s.poly([(280, 130), (380, 130), (372, 62), (288, 62)], "#3b3b3b", sw=3.4)
    s.rect(262, 126, 136, 16, "#3b3b3b", r=6, sw=3)
    # varita
    s.line(430, 250, 520, 190, sw=5, stroke="#3b3b3b")
    s.star(530, 182, 12)
    # palabras saliendo
    for (x, y, t, r) in ((610, 110, "verdad", -8), (700, 190, "plausible", 6), (560, 260, "citas", -5), (720, 300, "datos", 8)):
        s.rect(x - 60, y - 24, 120, 44, "white", r=8, sw=2.8)
        s.text(x, y + 8, t, 26, font="note", rot=r)
    person(s, 130, 388, 0.55, "orange", "brown", False, "surprised", "up")
    person(s, 690, 400, 0.5, "pink", "#5a3b22", True, "surprised", "up", long_hair=True)
    s.text(450, 520, "prestidigitación matemática", 40, font="title", color="white")
    s.sparks(330, 80, 60, 5)
    return s


def boton():
    s = Sketch(W, H, 38)
    s.ellipse(450, 400, 140, 40, "gray")
    s.rect(330, 320, 240, 80, "red", r=30)
    s.ellipse(450, 320, 120, 36, "#ff8c84")
    s.text(450, 335, "PREGUNTAR", 34, font="title")
    person(s, 120, 290, 0.6, "yellow", "#5a3b22", False, "happy", "point")
    tags = [(150, 90, "productividad", "green"), (450, 60, "impacto ecológico", "teal"), (750, 90, "derechos de autor", "yellow"),
            (740, 250, "desinformación", "pink"), (715, 400, "sesgos y alucinaciones", "orange"), (140, 470, "dependencia", "purple")]
    for x, y, t, c in tags:
        w = 30 + len(t) * 13
        s.rect(x - w / 2, y - 28, w, 50, c, r=18)
        s.text(x, y + 8, t, 26, font="title")
    s.arrow(450, 300, 450, 130, sw=3)
    s.arrow(500, 310, 700, 270, sw=3, bend=10)
    s.text(450, 530, "tan fácil de usar como difícil de entender", 30, font="note")
    return s


def descarga():
    s = Sketch(W, H, 39)
    person(s, 120, 120, 0.65, "orange", "brown", False, "happy", "point")
    s.text(310, 70, "delega parte del esfuerzo", 28, font="note")
    s.arrow(200, 140, 500, 140, sw=4)
    pesa(s, 350, 120, 0.6)
    robot(s, 640, 100, 0.6, "blue", "happy", "up")
    s.line(450, 250, 260, 320, sw=3.4)
    s.line(450, 250, 640, 320, sw=3.4)
    s.rect(80, 325, 360, 205, "#d9f2b8", r=18)
    s.rect(460, 325, 360, 205, "#ffd0cc", r=18)
    i_bombilla(s, 260, 395, 1.0)
    s.text(260, 462, "descarga + aprendizaje", 30, font="title")
    s.text(260, 496, "= descarga positiva", 26)
    brain(s, 640, 395, 0.55, "gray")
    s.text(640, 462, "solo descarga", 30, font="title")
    s.text(640, 496, "= deuda cognitiva", 26)
    return s


def deuda():
    s = Sketch(W, H, 40)
    brain(s, 300, 260, 1.5, "pink")
    s.ellipse(270, 250, 12, 14, "white", sw=3); s.ellipse(340, 250, 12, 14, "white", sw=3)
    s.dot(272, 254, 4); s.dot(342, 254, 4)
    s.path([(276, 310), (306, 298), (336, 310)], sw=3.4)
    robot(s, 700, 200, 0.7, "blue", "happy", "up")
    s.bubble(560, 30, 300, 70, ["«¡Yo te lo hago!", "No tienes que pensar»"], tail=(660, 130), size=26)
    s.rect(470, 380, 340, 100, "yellow", r=8)
    s.rect(470, 395, 340, 18, "#3b3b3b", r=2, sw=2)
    s.text(640, 456, "DEUDA COGNITIVA", 32, font="title")
    s.text(450, 530, "hoy comodidad, mañana a pagar con intereses", 28, font="note")
    s.arrow(470, 420, 380, 350, sw=3, bend=-15)
    return s


def sedentarismo():
    s = Sketch(1200, 540, 41)
    # sofá
    s.rect(30, 30, 560, 480, "white", r=20, sw=3)
    s.text(310, 82, "sedentarismo cognitivo", 38, font="title")
    s.rect(100, 300, 320, 110, "purple", r=24)
    s.rect(80, 260, 60, 150, "purple", r=20)
    s.rect(380, 260, 60, 150, "purple", r=20)
    brain(s, 260, 250, 0.9, "pink")
    s.line(210, 300, 180, 330, sw=3.4); s.line(300, 300, 340, 330, sw=3.4)
    s.dot(240, 240, 3.5); s.dot(280, 240, 3.5)
    s.line(240, 262, 262, 262, sw=3, dbl=False)
    robot(s, 490, 300, 0.42, "blue", "happy", "up")
    s.text(310, 470, "«hazme la tarea»", 30, font="note")
    # gimnasio
    s.rect(610, 30, 560, 480, "white", r=20, sw=3)
    s.text(890, 82, "ejercicio cognitivo", 38, font="title")
    brain(s, 890, 300, 0.95, "pink")
    s.line(830, 280, 770, 220, sw=3.4); s.line(950, 280, 1010, 220, sw=3.4)
    pesa(s, 890, 190, 1.4)
    s.line(850, 340, 830, 400, sw=3.4); s.line(930, 340, 950, 400, sw=3.4)
    s.dot(866, 290, 3.5); s.dot(910, 290, 3.5)
    s.path([(868, 312), (890, 324), (912, 312)], sw=3)
    sudor(s, 800, 250); sudor(s, 980, 250)
    s.text(890, 470, "esfuerzo con sentido: hard fun", 30, font="note")
    return s


def hard_fun():
    s = Sketch(1000, 540, 42)
    s.poly([(0, 520), (120, 470), (350, 340), (600, 190), (760, 120), (760, 520)], "#cdb98f", sw=3.6)
    s.line(760, 120, 760, 30, sw=5, stroke="#8b5e3c")
    s.poly([(760, 30), (860, 55), (760, 80)], "green", sw=3)
    person(s, 420, 222, 0.5, "orange", "brown", False, "happy", "up")
    sudor(s, 385, 190); sudor(s, 460, 185)
    s.ellipse(890, 90, 44, 44, "yellow")
    s.bubble(60, 60, 300, 100, ["Es divertido hacer", "cosas difíciles si", "tienen sentido"], tail=(230, 250), size=26, font="title")
    s.text(330, 500, "hard fun · Seymour Papert", 32, font="note")
    return s


def mapa_aprendizajes():
    s = Sketch(1000, 560, 43)
    genie(s, 400, 190, 0.5, "happy", "ajusta")
    maquina(s, 585, 270, 0.3, "ajustada")
    s.text(500, 420, "construir modelos de IA", 34, font="title")
    ramas = [(150, 70, "el papel\nde los datos", "yellow"), (500, 40, "derechos\nde autor", "pink"), (850, 70, "impacto\necológico", "green"),
             (175, 320, "naturaleza\nestadística, sesgo\ny alucinaciones", "orange"), (890, 300, "ética", "purple"), (500, 500, "pensamiento crítico", "blue")]
    for x, y, t, c in ramas:
        ls = t.split("\n")
        w = 30 + max(len(l) for l in ls) * 14
        s.rect(x - w / 2, y - 30, w, 34 + 30 * len(ls), c, r=20)
        for i, ln in enumerate(ls):
            s.text(x, y + 6 + i * 30, ln, 28, font="title")
    s.arrow(250, 90, 410, 160, sw=3); s.arrow(500, 110, 500, 130, sw=3); s.arrow(750, 95, 590, 160, sw=3)
    s.arrow(300, 330, 410, 270, sw=3); s.arrow(830, 300, 680, 262, sw=3); s.arrow(500, 470, 500, 430, sw=3)
    return s


def leer_escribir():
    s = Sketch(1300, 520, 44)
    cols = [(230, "Letras", "leer", "escribir"), (650, "Números", "ver precios", "calcular"), (1070, "Código", "consumir apps", "crear apps")]
    for i, (x, t, a, b) in enumerate(cols):
        (i_libro, i_calc, i_codigo)[i](s, x, 90, 1.2)
        s.text(x, 192, t, 48, font="title")
        s.rect(x - 150, 230, 300, 70, "gray", r=16)
        s.text(x, 280, a, 38)
        s.arrow(x, 306, x, 340, sw=4)
        s.rect(x - 150, 350, 300, 80, "yellow", r=16)
        s.text(x, 406, b, 42, font="title")
    s.text(650, 490, "alfabetizar es enseñar a escribir, no solo a leer", 38, font="note")
    return s


ESCENAS = {"linea-ia": linea_ia, "pioneros": pioneros, "eclipse": eclipse, "caja-negra": caja_negra, "maquina-habla": maquina_habla,
           "historia-escritura": historia_escritura, "mago": mago, "boton": boton, "descarga": descarga, "deuda": deuda,
           "sedentarismo": sedentarismo, "hard-fun": hard_fun, "mapa-aprendizajes": mapa_aprendizajes, "leer-escribir": leer_escribir}
