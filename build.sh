#!/bin/bash

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Aplicando migraciones..."
# python manage.py migrate --noinput   <-- comentar esta línea

echo "Recolectando estáticos..."
python manage.py collectstatic --noinput --clear
