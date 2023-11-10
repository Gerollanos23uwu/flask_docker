#!/bin/bash
# Espera durante 10 segundos antes de ejecutar las migraciones
echo 'espera 10 segundos'
sleep 10

echo 'ejecuta el script de la base de datos'
# Define el número de intentos

# Ejecuta tu primer comando (por ejemplo, flask db init)
echo 'ejecuta flask db init'
flask db init

# Ejecuta tu segundo comando (por ejemplo, otro comando)
echo 'ejecuta flask db migrate'
flask db migrate -m "migración inicial"

# Ejecuta tu tercer comando (por ejemplo, otro comando más)
echo 'ejecuta flask db upgrade'
flask db upgrade

# Inicia tu aplicación Flask
echo 'inicia el servidor Gunicorn'
gunicorn app:app --bind 0.0.0.0:5005 --log-level debug --reload #nombre_del_módulo:nombre_de_la_variable_de_la_aplicación

# 0.0.0.0: Esta es la dirección IP del host.
# Usar 0.0.0.0 significa que Gunicorn escuchará en todas las interfaces de red disponibles,
# lo que hace que la aplicación sea accesible desde fuera del contenedor.