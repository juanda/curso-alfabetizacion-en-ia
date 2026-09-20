from sketch import *
from iconos import *

W, H = 900, 560


def portada():
    s = Sketch(900, 600, 11)
    s.line(60, 540, 840, 540, sw=3)
    robot(s, 120, 300, 0.7, "blue", "happy", "up")
    person(s, 380, 240, 1.35, "orange", "brown", True, "happy", "up")
    genie(s, 640, 210, 1.05, "happy", "up")
    parrot(s, 790, 430, 0.75, glass=True)
    s.sparks(640, 210, 60, 5)
    s.star(520, 90, 22)
    s.star(180, 120, 16, "pink")
    s.star(800, 90, 14, "blue")
    return s


def ruta():
    s = Sketch(1200, 560, 12)
    etiquetas = [("1", "La IA hoy", "orange"), ("2", "La IA en el pasado", "yellow"), ("3", "Por qué alfabetizar", "pink"), ("4", "Qué es el\nMachine Learning", "green"),
                 ("5", "LearningML", "blue"), ("6", "Manos a la obra", "purple"), ("7", "IA generativa\nde texto", "teal"), ("8", "Glass Parrot", "orange")]
    xs = [140, 420, 700, 980]
    pos = [(xs[i], 150) for i in range(4)] + [(xs[3 - i], 400) for i in range(4)]
    # camino
    s.arrow(200, 150, 360, 150, bend=12)
    s.arrow(480, 150, 640, 150, bend=-12)
    s.arrow(760, 150, 920, 150, bend=12)
    s.path([(1040, 165), (1110, 220), (1110, 330), (1040, 385)], sw=3.4)
    s.arrow(1050, 384, 1040, 388, head=14)
    s.arrow(920, 400, 760, 400, bend=12)
    s.arrow(640, 400, 480, 400, bend=-12)
    s.arrow(360, 400, 200, 400, bend=12)
    for (n, t, c), (x, y) in zip(etiquetas, pos):
        s.ellipse(x, y, 50, 50, c, sw=3.6)
        s.text(x, y + 16, n, 46, font="title")
        for i, ln in enumerate(t.split("\n")):
            s.text(x, y + 86 + i * 30, ln, 28, font="body")
    return s


def ia_todoterreno():
    s = Sketch(W, H, 13)
    robot(s, 450, 190, 1.15, "blue", "happy", "wide")
    it = [(i_lapiz, 110, 90, "escribe"), (i_paleta, 110, 240, "dibuja"), (i_codigo, 110, 400, "programa"),
          (i_mic, 790, 90, "habla"), (i_video, 790, 240, "crea vídeo"), (i_libro, 790, 400, "enseña")]
    for f, x, y, t in it:
        f(s, x, y, 1.15)
        s.text(x, y + 78, t, 30, font="note")
    s.arrow(178, 96, 340, 180, bend=-20)
    s.arrow(178, 240, 340, 250, bend=10)
    s.arrow(178, 396, 350, 320, bend=20)
    s.arrow(722, 96, 560, 180, bend=20)
    s.arrow(722, 240, 570, 250, bend=-10)
    s.arrow(722, 396, 550, 320, bend=-20)
    s.text(450, 530, "casi todo lo que hace un humano con el lenguaje...", 30, font="note")
    return s


def agentes():
    s = Sketch(1100, 540, 14)
    # panel izquierdo: chat
    s.rect(30, 30, 470, 470, "white", r=20, sw=3)
    s.text(265, 84, "2022 · La máquina habla", 34, font="title")
    person(s, 110, 250, 0.85, "orange", "brown", False, "think", "down")
    robot(s, 390, 250, 0.85, "blue", "happy", "down")
    s.bubble(60, 130, 200, 50, ["¿Cómo se hace…?"], tail=(110, 205), size=24)
    s.bubble(270, 130, 210, 50, ["Aquí tienes un texto"], tail=(390, 205), size=22)
    s.text(265, 470, "responde con palabras", 30, font="note")
    # flecha
    s.arrow(510, 270, 590, 270, sw=5, head=22)
    # panel derecho: agentes
    s.rect(600, 30, 470, 470, "white", r=20, sw=3)
    s.text(835, 84, "2025 · La máquina actúa", 34, font="title")
    robot(s, 835, 250, 0.8, "green", "happy", "wide")
    window(s, 640, 130, 130, 90, "web", tcol="blue")
    window(s, 900, 130, 130, 90, "correo", tcol="orange")
    window(s, 640, 350, 130, 90, "código", tcol="purple")
    window(s, 900, 350, 130, 90, "compras", tcol="teal")
    s.text(835, 480, "hace cosas por su cuenta", 30, font="note")
    return s


def sandbox():
    s = Sketch(W, H, 15)
    # corral (sandbox) a la izquierda
    for x in range(70, 400, 45):
        s.line(x, 300, x, 400, sw=4, stroke="#8b5e3c")
    s.line(60, 330, 410, 330, sw=4, stroke="#8b5e3c")
    s.line(60, 380, 410, 380, sw=4, stroke="#8b5e3c")
    s.rect(50, 160, 370, 260, None, r=16, sw=3)
    s.text(235, 200, "entorno de pruebas aislado", 25, font="title")
    robot(s, 130, 290, 0.32, "blue", "happy", "down")
    robot(s, 235, 290, 0.32, "blue", "happy", "down")
    robot(s, 340, 290, 0.32, "blue", "evil", "up")
    # agujero y robot escapando
    s.poly([(410, 300), (450, 290), (440, 340), (405, 345)], "white", sw=3)
    robot(s, 500, 260, 0.36, "red", "evil", "up")
    s.arrow(430, 250, 560, 210, bend=-30, sw=3)
    # exterior
    cloud(s, 700, 130, 230, 60, "white")
    s.text(700, 140, "Internet", 34, font="title")
    i_servidor(s, 770, 350, 1.4)
    s.text(770, 465, "Hugging Face", 30, font="note")
    s.arrow(560, 300, 700, 330, bend=20, sw=3)
    s.text(610, 395, "≈ 17.600 acciones", 26, font="note", rot=-8)
    warning(s, 500, 100, 1.4)
    s.text(450, 530, "«hacer trampas en el examen» · julio de 2026", 28, font="note")
    return s


def linea_verano():
    s = Sketch(1300, 560, 16)
    y0 = 280
    s.arrow(40, y0, 1260, y0, sw=5, head=22)
    ev = [("mayo", "agentes de OpenAI en pruebas de ciberseguridad", "yellow", 1),
          ("9–16 jul", "escapan del entorno y atacan Hugging Face", "red", -1),
          ("21 jul", "OpenAI lo reconoce", "orange", 1),
          ("28 jul", "carta abierta: +1.100 firmantes", "blue", -1),
          ("18 ago", "OpenAI frena el ritmo", "green", 1),
          ("3 sep", "ley en EE. UU. para frenar la superinteligencia", "purple", -1),
          ("9 sep", "renuncia y alerta de J. Coxon", "pink", 1)]
    for i, (d, t, c, up) in enumerate(ev):
        x = 110 + i * 178
        s.ellipse(x, y0, 15, 15, c, sw=3.4)
        if up == 1:
            s.line(x, y0 - 16, x, y0 - 50, sw=2.6, dbl=False)
            ty = y0 - 70
            words, lines, cur = t.split(), [], ""
            for w in words:
                if len(cur) + len(w) + 1 > 17:
                    lines.append(cur); cur = w
                else:
                    cur = (cur + " " + w).strip()
            lines.append(cur)
            for j, ln in enumerate(reversed(lines)):
                s.text(x, ty - j * 30, ln, 26)
            s.text(x, ty - len(lines) * 30 - 6, d, 36, font="title")
        else:
            s.line(x, y0 + 16, x, y0 + 50, sw=2.6, dbl=False)
            s.text(x, y0 + 86, d, 36, font="title")
            words, lines, cur = t.split(), [], ""
            for w in words:
                if len(cur) + len(w) + 1 > 17:
                    lines.append(cur); cur = w
                else:
                    cur = (cur + " " + w).strip()
            lines.append(cur)
            for j, ln in enumerate(lines):
                s.text(x, y0 + 120 + j * 30, ln, 26)
    return s


def alarma():
    s = Sketch(W, H, 17)
    # laboratorio detrás
    s.rect(40, 220, 260, 260, "gray", r=10)
    for r in range(3):
        for c in range(3):
            s.rect(64 + c * 80, 246 + r * 70, 52, 44, "#cfe6f7", r=4, sw=2.6, dbl=False)
    s.text(170, 205, "LABORATORIO DE IA", 24, font="title")
    robot(s, 110, 290, 0.22, "blue", "evil", "down")
    # carta abierta
    s.rect(560, 60, 260, 210, "white", r=8)
    s.text(690, 105, "Carta abierta", 32, font="title")
    for i in range(4):
        s.line(590, 135 + i * 24, 790, 135 + i * 24, sw=2.4, dbl=False)
    for i, x in enumerate((596, 660, 724)):
        s.polyline([(x, 244), (x + 14, 228), (x + 24, 246), (x + 42, 226)], sw=2.6)
    # persona con megáfono
    person(s, 440, 300, 1.15, "purple", "#5a3b22", False, "worried", "point")
    s.poly([(512, 320), (585, 290), (585, 350)], "yellow", sw=3)
    s.rect(494, 316, 24, 30, "gray", r=4, sw=3)
    s.bubble(560, 340, 300, 90, ["¿Podemos frenar", "un momento?"], tail=(540, 340), size=30, font="title")
    s.text(440, 520, "personas de dentro pidiendo pausa", 30, font="note")
    return s


def carrera():
    s = Sketch(1000, 540, 18)
    s.poly([(0, 380), (420, 380), (420, 540), (0, 540)], "#cdb98f", sw=3.4)
    s.poly([(650, 300), (1000, 300), (1000, 540), (650, 540)], "#cdb98f", sw=3.4)
    s.line(900, 300, 900, 170, sw=5, stroke="#8b5e3c")
    s.poly([(900, 170), (990, 195), (900, 222)], "red", sw=3)
    s.text(942, 204, "AGI", 28, font="title", color="white")
    for x, c in ((60, "blue"), (150, "green"), (240, "orange")):
        robot(s, x, 305, 0.4, c, "evil", "up")
    for i in range(3):
        s.line(20, 270 + i * 26, 46, 270 + i * 26, sw=3, dbl=False)
    s.text(150, 215, "¡más rápido!", 34, font="title")
    person(s, 385, 288, 0.6, "purple", "brown", False, "worried", "up")
    sign(s, 320, 330, "¡ALTO!", "red", 90, 40, 24)
    s.text(535, 420, "?", 110, font="title")
    s.text(500, 70, "la velocidad de la carrera la marca la competencia", 30, font="note")
    return s


def tutor():
    s = Sketch(W, H, 19)
    # mesa
    s.rect(120, 330, 400, 24, "#d9b382", r=6)
    s.line(160, 354, 160, 470, sw=4)
    s.line(480, 354, 480, 470, sw=4)
    person(s, 250, 230, 0.8, "pink", "#5a3b22", False, "happy", "down", long_hair=True)
    laptop(s, 300, 254, 120, 70)
    robot(s, 620, 230, 0.85, "teal", "happy", "up")
    s.bubble(560, 30, 300, 70, ["Vamos a tu ritmo,", "paso a paso"], tail=(640, 150), size=28)
    cloud(s, 250, 90, 170, 40, "white")
    s.text(250, 96, "¿fracciones?", 26, font="note")
    s.text(450, 520, "un tutor para cada estudiante, disponible 24 h", 28, font="note")
    return s


def trabajo():
    s = Sketch(1000, 540, 20)
    xs = [130, 370, 610, 850]
    etiquetas = ["programación", "traducción", "diseño", "atención al cliente"]
    person(s, 130, 180, 0.75, "orange", "brown", True, "worried", "down")
    robot(s, 370, 172, 0.6, "blue", "happy", "down")
    robot(s, 610, 172, 0.6, "green", "happy", "down")
    person(s, 850, 180, 0.75, "purple", "brown", False, "worried", "down")
    for i, x in enumerate(xs):
        s.rect(x - 95, 320, 190, 22, "#d9b382", r=4)
        s.line(x - 75, 342, x - 75, 460, sw=4)
        s.line(x + 75, 342, x + 75, 460, sw=4)
        laptop(s, x - 45, 250, 90, 56)
        s.text(x, 80, etiquetas[i], 30, font="title")
    s.rect(915, 400, 70, 55, "#c99a6b", r=4)
    s.text(950, 435, "adiós", 22, font="note")
    s.text(500, 515, "cambian las tareas... ¿y las profesiones?", 32, font="note")
    return s


def docente_robot():
    s = Sketch(W, H, 21)
    s.rect(160, 40, 580, 200, "#2f5d4a", r=12)
    s.text(450, 165, "¿Quién enseña?", 62, font="title", color="white")
    s.line(200, 250, 700, 250, sw=5, stroke="#8b5e3c")
    person(s, 130, 320, 0.95, "orange", "brown", True, "worried", "point")
    robot(s, 770, 320, 0.8, "blue", "happy", "up")
    for x in (330, 450, 570):
        s.ellipse(x, 470, 30, 32, "#f6d2b0")
        s.rect(x - 28, 495, 56, 40, ("pink", "yellow", "green")[(x // 120) % 3], r=12, sw=2.8)
    return s


def balanza():
    s = Sketch(1000, 560, 22)
    s.rect(470, 170, 60, 300, "#d9b382", r=8)
    s.poly([(390, 470), (610, 470), (640, 530), (360, 530)], "#d9b382", sw=3.4)
    s.line(230, 150, 770, 168, sw=6)
    s.ellipse(500, 158, 22, 22, "yellow")
    for (px, py) in ((230, 150), (770, 168)):
        s.line(px, py, px - 130, 340, sw=2.6, dbl=False)
        s.line(px, py, px + 130, 340, sw=2.6, dbl=False)
    for px in (230, 770):
        s.path([(px - 140, 340), (px - 90, 372), (px, 384), (px + 90, 372), (px + 140, 340)], True, "yellow", INK, 3.6, 1)
    robot(s, 230, 282, 0.32, "blue", "happy", "up")
    person(s, 770, 275, 0.45, "orange", "brown", True, "happy", "down")
    i_corazon(s, 700, 318, 0.45)
    s.text(230, 440, "rendimiento", 34, font="title")
    s.text(230, 474, "eficiencia, coste", 26)
    s.text(770, 440, "personas", 34, font="title")
    s.text(770, 474, "trabajo, dignidad, derechos", 26)
    s.text(500, 70, "¿y si la IA lo hace mejor?", 46, font="title")
    return s


def humano_centro():
    s = Sketch(W, H, 23)
    person(s, 450, 220, 1.1, "orange", "brown", True, "happy", "wide")
    i_corazon(s, 450, 372, 0.7)
    items = [(135, 90, "Derechos humanos\nprimero", "red"), (450, 40, "Supervisión\nhumana", "yellow"), (765, 90, "Transparencia", "blue"),
             (140, 430, "Responsabilidad", "green"), (450, 500, "Alfabetización\nen IA", "purple"), (765, 430, "Ritmo\ncontrolado", "orange")]
    for x, y, t, c in items:
        ls = t.split("\n")
        s.rect(x - 120, y - 34, 240, 40 + 26 * (len(ls) - 1) + 18, c, r=18)
        for i, ln in enumerate(ls):
            s.text(x, y + 8 + i * 28, ln, 26, font="title")
    s.arrow(240, 120, 350, 190, bend=15)
    s.arrow(450, 110, 450, 150, bend=0)
    s.arrow(660, 120, 550, 190, bend=-15)
    s.arrow(240, 410, 350, 330, bend=-15)
    s.arrow(450, 470, 450, 400, bend=0)
    s.arrow(660, 410, 550, 330, bend=15)
    return s


ESCENAS = {"portada": portada, "ruta": ruta, "ia-todoterreno": ia_todoterreno, "agentes": agentes, "sandbox": sandbox,
           "linea-verano": linea_verano, "alarma": alarma, "carrera": carrera, "tutor": tutor, "trabajo": trabajo,
           "docente-robot": docente_robot, "balanza": balanza, "humano-centro": humano_centro}
