# Sesión «Alfabetización en IA: aprender a crear para comprender»

Material para la sesión del curso de IA para docentes del **21 de septiembre de 2026**.
Autor: **Juan David Rodríguez García** · Licencia **CC BY-NC 4.0** (ver `LICENCIA.md`).

## Qué contiene

| Carpeta / fichero | Contenido |
| --- | --- |
| `pdf/presentacion-alfabetizacion-ia.pdf` | Presentación (85 diapositivas, 16:9) lista para proyectar y compartir |
| `pdf/guion-alfabetizacion-ia.pdf` | Guion de apoyo: texto desarrollado, tiempos, demos, actividad de Glass Parrot, anexos |
| `presentacion/presentacion.md` | Fuente de la presentación en **Markdown (Marp)** |
| `presentacion/img/` | Ilustraciones (PNG) y `img/svg/` (SVG vectoriales originales) |
| `presentacion/tema/` | Tema visual `alfabetizacion` (papel crema, trazo a mano) |
| `presentacion/fuentes/` | Tipografías manuscritas (Patrick Hand, Kalam, Caveat · SIL OFL) |
| `guion/guion.md` | Fuente del guion en **Markdown** |
| `samples/` | 19 fábulas y cuentos infantiles en **dominio público** (Wikisource) para entrenar Glass Parrot; índice y licencias en `samples/FUENTES.md` |
| `herramientas/` | Scripts para regenerar ilustraciones y PDF |

## Estructura de la sesión

1. La IA hoy · 2. La IA en el pasado · 3. Por qué alfabetizar en IA · 4. Qué es el Machine Learning ·
5. LearningML · 6. Manos a la obra · 7. IA generativa de texto (LLM) · 8. Glass Parrot · Cierre.
La sesión dura ≈ 3 h y **no incluye ejercicios en clase**: las actividades son tareas para la plataforma (LMS), cuyos enunciados están en el anexo E del guion. El guion incluye la tabla de tiempos y cómo reducirla a ≈ 2 h 30.

## Cómo regenerar

Requisitos: `python3`, `chromium`, `pandoc` y Node.js (para Marp CLI).

```sh
cd herramientas
npm install            # solo la primera vez (instala @marp-team/marp-cli)
./construir.sh         # ilustraciones + presentación PDF + guion PDF
./construir.sh imagenes   # solo ilustraciones (herramientas/escenas_*.py)
./construir.sh pdf        # solo los PDF (tras editar los .md)
python3 descargar_samples.py   # vuelve a descargar los textos de samples/ (requiere lxml)
```

- Para editar la presentación: `presentacion/presentacion.md` (también se puede abrir con Marp for VS Code
  usando el tema `presentacion/tema/alfabetizacion.css`, que se genera con `construir.sh`).
- Para editar una ilustración: la escena correspondiente en `herramientas/escenas_*.py` (librería de dibujo en `sketch.py`).
- `node_modules/` (≈ 130 MB) se puede borrar cuando no se necesite regenerar.

## Antes de la sesión (importante)

- **Verifica los hechos del verano de 2026** (bloque 1): vienen de prensa y fuentes secundarias, y las cifras
  difieren entre fuentes. Ver el anexo A del guion.
- **Referencia corregida**: Gerlich (2025) es de un único autor (*Societies* 15(1), 6); en el discurso original
  figuraba con otros autores.
- Prueba **Glass Parrot** y **LearningML** desde el aula; entra a Glass Parrot por su portada
  (las URL internas devuelven 404 si se escriben directamente).
- Descarga los materiales de las demos (ver bloque 6 del guion).
