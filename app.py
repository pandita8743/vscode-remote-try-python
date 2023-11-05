#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

print('hello world')

import random

opciones = ['piedra', 'papel', 'tijeras']

while True:
    eleccion_usuario = input('Elige una opción (piedra, papel, tijeras): ').lower()
    if eleccion_usuario not in opciones:
        print('Opción no válida. Inténtalo de nuevo.')
        continue
    eleccion_oponente = random.choice(opciones)
    if eleccion_usuario == eleccion_oponente:
        print('Empate!')
    elif (eleccion_usuario == 'piedra' and eleccion_oponente == 'tijeras') or \
         (eleccion_usuario == 'tijeras' and eleccion_oponente == 'papel') or \
         (eleccion_usuario == 'papel' and eleccion_oponente == 'piedra'):
        print('Ganaste!')
    else:
        print('Perdiste!')
    jugar_de_nuevo = input('¿Quieres jugar de nuevo? (sí/no): ').lower()
    if jugar_de_nuevo != 'sí':
        break
