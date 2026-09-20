"""Descarga de Wikisource (es) un conjunto de fábulas y cuentos infantiles en dominio público
y los guarda como texto plano en samples/ (para entrenar modelos en Glass Parrot).

Uso:  python3 descargar_samples.py
Requiere: lxml y acceso a es.wikisource.org.

Cada texto se limpia (sin cabeceras, notas ni numeración de página) y se comprueba que el autor de la
cabecera de la página coincide con el esperado. Se genera también samples/FUENTES.md con autor, obra,
año, URL y licencia de cada texto.
"""
import html
import json
import pathlib
import re
import subprocess
import sys
import unicodedata
import urllib.parse

from lxml import html as LH

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "samples"
API = "https://es.wikisource.org/w/api.php"
UA = "Mozilla/5.0 (Claude Code; material didactico CC BY-NC; echidna@echidna.es)"

AUTORES = {
    "Samaniego": ("Félix María Samaniego", 1801, "Fábulas morales", "1781-1784"),
    "Iriarte": ("Tomás de Iriarte", 1791, "Fábulas literarias", "1782"),
    "Quiroga": ("Horacio Quiroga", 1937, "Cuentos de la selva", "1918"),
    "Martí": ("José Martí", 1895, "La Edad de Oro", "1889"),
}

# (clave de autor, título de la página en Wikisource, tipo)
TEXTOS = [
    ("Samaniego", "El cuervo y el zorro", "fábula"),
    ("Samaniego", "El lobo y el perro (Samaniego)", "fábula"),
    ("Samaniego", "El león y el ratón (Samaniego)", "fábula"),
    ("Samaniego", "El lobo y la cigüeña", "fábula"),
    ("Samaniego", "La cigarra y la hormiga", "fábula"),
    ("Samaniego", "La lechera", "fábula"),
    ("Samaniego", "La zorra y las uvas", "fábula"),
    ("Iriarte", "El burro flautista", "fábula"),
    ("Iriarte", "La ardilla y el caballo", "fábula"),
    ("Iriarte", "Los dos loros y la cotorra", "fábula"),
    ("Iriarte", "El oso, la mona y el cerdo", "fábula"),
    ("Quiroga", "El loro pelado", "cuento"),
    ("Quiroga", "Las medias de los flamencos", "cuento"),
    ("Quiroga", "La tortuga gigante", "cuento"),
    ("Quiroga", "La abeja haragana", "cuento"),
    ("Martí", "Los zapaticos de rosa", "cuento"),
    ("Martí", "La muñeca negra", "cuento"),
    ("Martí", "Nené traviesa", "cuento"),
    ("Martí", "Bebé y el señor don Pomposo", "cuento"),
]


def pedir(params):
    q = urllib.parse.urlencode(params)
    out = subprocess.run(["curl", "-s", "-A", UA, f"{API}?{q}"], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def slug(titulo):
    t = re.sub(r"\s*\(.*?\)\s*", "", titulo)
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def limpiar(html_pagina):
    """Devuelve (autor, título, bloques de texto). Usa los metadatos de Wikisource (#ws-data)."""
    raiz = LH.fromstring(html_pagina)
    autor = " ".join(x.text_content().strip() for x in raiz.xpath('//*[@id="ws-data"]/span[@class="ws-author"]'))
    titulo = " ".join(x.text_content().strip() for x in raiz.xpath('//*[@id="ws-data"]/span[@class="ws-title"]'))
    nota = " ".join(x.text_content().strip() for x in raiz.xpath('//*[@id="ws-data"]//*[@class="ws-notes"]'))
    # letras capitulares: la inicial va como imagen con el texto en alt; se convierte en texto
    for img in raiz.xpath("//img"):
        alt = (img.get("alt") or "").strip()
        cola = (alt if len(alt) <= 2 and alt.isalpha() else "") + (img.tail or "")
        padre, prev = img.getparent(), img.getprevious()
        if prev is not None:
            prev.tail = (prev.tail or "") + cola
        else:
            padre.text = (padre.text or "") + cola
        padre.remove(img)
    ruido = ('//*[contains(@style,"display:none")]|//style|//script|//*[@id="headertemplate"]|//*[@id="footertemplate"]|//*[@id="ws-data"]|//*[contains(@class,"noprint")]'
             '|//*[contains(@class,"ws-noexport")]|//sup|//*[contains(@class,"mw-editsection")]'
             '|//*[contains(@class,"references")]|//*[contains(@class,"reference")]|//table|//div[@class="np"]')
    for n in raiz.xpath(ruido):
        if n.getparent() is not None:
            n.getparent().remove(n)
    bloques = []
    for el in raiz.iter("p", "h1", "h2", "h3", "h4", "li", "dd", "dt", "pre"):
        for br in el.iter("br"):
            br.tail = "\n" + (br.tail or "")
        txt = html.unescape(el.text_content()).replace("\xa0", " ")
        if el.tag == "pre":                       # verso: se respetan los saltos de estrofa
            lineas = [re.sub(r"[ \t]+", " ", l).strip() for l in txt.split("\n")]
            txt = re.sub(r"\n{3,}", "\n\n", "\n".join(lineas)).strip()
        else:
            lineas = [re.sub(r"[ \t]+", " ", l).strip() for l in txt.split("\n")]
            txt = "\n".join(l for l in lineas if l)
        if txt:
            bloques.append((el.tag, txt))
    return autor, titulo, bloques, nota


def main():
    SALIDA.mkdir(exist_ok=True)
    filas = []
    n = 0
    for clave, pagina, tipo in TEXTOS:
        autor_esp, muerte, obra, anio = AUTORES[clave]
        # si el título es ambiguo (varias versiones de la misma fábula), se prueba la página con «(Autor)»
        for candidata in (pagina, f"{pagina} ({clave})"):
            datos = pedir({"action": "parse", "page": candidata, "prop": "text|revid", "format": "json", "formatversion": 2, "redirects": 1})
            if "parse" not in datos:
                continue
            p = datos["parse"]
            autor, titulo, bloques, nota = limpiar(p["text"])
            if autor_esp.split()[-1] in autor:
                break
            print(f"   (descartada «{candidata}»: autor '{autor or 'desconocido'}')")
        else:
            print(f"   !! OMITIDO: no se encontró una página de {autor_esp} para «{pagina}»")
            continue
        n += 1
        titulo = re.sub(r"\s*\(.*?\)\s*$", "", titulo or p["title"]).strip()
        # quitar el encabezado del cuerpo si repite el título y notas al final del tipo «Fin»
        titulo = titulo.strip(" .")
        cuerpo = [(tg, tx) for tg, tx in bloques
                  if not re.fullmatch(r"(?i)f[aá]bula\s+[ivxlc\d]+\.?", tx.strip())
                  and not (tg.startswith("h") and tx.lower().strip(" .") == titulo.lower())]
        texto = titulo + "\n\n" + "\n\n".join(tx for _, tx in cuerpo) + "\n"
        texto = unicodedata.normalize("NFC", texto)
        nombre = f"{n:02d}-{slug(titulo)}.txt"
        (SALIDA / nombre).write_text(texto, encoding="utf-8")
        palabras = len(texto.split())
        url = "https://es.wikisource.org/wiki/" + urllib.parse.quote(p["title"].replace(" ", "_"))
        filas.append((nombre, titulo, tipo, autor_esp, muerte, obra, anio, url, palabras, nota))
        print(f"{nombre:45s} {palabras:5d} palabras   ({autor})")

    total = sum(f[8] for f in filas)
    md = ["# Textos de ejemplo para Glass Parrot", "",
          f"{len(filas)} fábulas y cuentos infantiles en **dominio público**, en español ({f'{total:,}'.replace(',', '.')} palabras en total), "
          "para usar como texto de entrenamiento en Glass Parrot (botón *Subir* o *Añadir texto*).", "",
          "## Licencia", "",
          "Todas las obras son de autores fallecidos hace más de 80 años (dominio público en España, Argentina, Uruguay, Cuba y "
          "en la mayoría de países). Los textos proceden de **Wikisource en español** (https://es.wikisource.org), que los "
          "transcribe y corrige; su contenido puede reutilizarse libremente (las contribuciones de la comunidad de Wikisource se "
          "publican con licencia CC BY-SA 4.0). Los ficheros `.txt` se han **limpiado** (sin cabeceras, notas ni numeración de "
          "página) y pueden diferir ligeramente de la edición original en la ortografía o los signos.", "",
          "## Índice", "", "| Fichero | Título | Tipo | Autor (†) | Obra | Palabras | Fuente |", "| --- | --- | --- | --- | --- | ---: | --- |"]
    notas = []
    for nombre, titulo, tipo, autor, muerte, obra, anio, url, palabras, nota in filas:
        md.append(f"| `{nombre}` | {titulo} | {tipo} | {autor} (†{muerte}) | {obra} ({anio}) | {palabras} | [Wikisource]({url}) |")
        if not nota and autor == AUTORES["Iriarte"][0]:
            nota = "Transcripción con la ortografía original de 1782 (p. ej. «dixo», «baxo», «hai»)."
        if nota:
            notas.append(f"- `{nombre}`: {nota}")
    if notas:
        md += ["", "## Notas de la transcripción (según Wikisource)", ""] + notas
    md += ["", "## Cómo se han obtenido", "",
           "Con `herramientas/descargar_samples.py` (API de Wikisource). Para regenerarlos: `python3 herramientas/descargar_samples.py`.", ""]
    (SALIDA / "FUENTES.md").write_text("\n".join(md), encoding="utf-8")
    print(f"\n{len(filas)} textos, {total} palabras -> {SALIDA}")


if __name__ == "__main__":
    main()
