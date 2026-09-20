#!/bin/sh
# Envoltorio para que Marp pueda lanzar Chromium en entornos sin sandbox de usuario.
exec /usr/bin/chromium --no-sandbox --disable-gpu "$@"
