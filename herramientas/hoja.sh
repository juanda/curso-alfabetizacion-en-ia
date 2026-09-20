#!/bin/sh
# Hoja de contactos para revisar ilustraciones: ./hoja.sh salida.png nombre1 nombre2 ...
out="$1"; shift
IMG="$(dirname "$0")/../presentacion/img"
files=""
for n in "$@"; do files="$files $IMG/$n.png"; done
montage $files -background '#fffdf6' -geometry 880x+8+8 -tile 2x "$out"
