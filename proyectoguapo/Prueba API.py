# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 21:37:45 2025

@author: goess
"""


import os
import sqlite3
# from dotenv import load_dotenv
from openai import OpenAI
import sys

# Añadir la ruta donde está proyectoguapo.py
sys.path.append(r"C:\Users\rportatil113\Desktop\Repositorio_data sciense\proyectoguapo")
from proyectoguapo import obtener_reseñas

# Obtener argumento de búsqueda desde línea de comandos
if len(sys.argv) > 1:
    busqueda = " ".join(sys.argv[1:])
else:
    busqueda = input("¿Qué empresa o sitio quieres su reseña (recuerda poner el lugar)? ")

# Cargar variables del entorno
os.chdir(r"C:\Users\rportatil113\Desktop\Repositorio_data sciense\proyectoguapo")
load_dotenv(dotenv_path=".env")
api_key = os.getenv("OPENAI_API_KEY")

# Ejecutar scraping
reseñas = obtener_reseñas(busqueda)


# Crear una conexión a la base de datos SQLite
db_path = r"C:\Users\rportatil113\Desktop\Repositorio_data sciense\proyectoguapo\reseñas_analizadas.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Limpiar la tabla (si ya existía)
cursor.execute('''DELETE FROM ReseñasAnalizadas;''')
cursor.execute('''DELETE FROM sqlite_sequence WHERE name='ReseñasAnalizadas';''')

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ReseñasAnalizadas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        texto TEXT,
        puntuacion DECIMAL(3,2)
    )
''')

# Verificar si hay clave API
if api_key:
    client = OpenAI(api_key=api_key)

    # Armar el texto del prompt
    reseñas_prompt = "\n".join(reseñas)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{
            "role": "user",
            "content": f"""Eres un analista de sentimientos experto en evaluar reseñas de usuarios considerando tres elementos: el texto de la reseña, la fecha en que fue escrita y la puntuación en estrellas (de 1 a 5).

Tu tarea es asignar a cada reseña una puntuación emocional entre -1 (muy negativa) y 1 (muy positiva), teniendo en cuenta matices, contexto, antigüedad del comentario y su coherencia con las estrellas asignadas por el usuario.

Solo debes devolver la puntuación emocional numérica de cada reseña, una por línea, sin texto adicional ni explicaciones. 

Lista de reseñas a analizar (una por línea con formato "Texto. Estrellas: X. Fecha: hace x años/meses/días"):
{reseñas_prompt}
"""
        }]
    )

    resultados = response.choices[0].message.content.strip().splitlines()

    # Verificar cantidad de resultados válidos
    min_length = min(len(reseñas), len(resultados))

    for i in range(min_length):
        try:
            puntuacion = resultados[i].strip()
            puntuacion_float = round(float(puntuacion), 2)
            puntuacion_float = max(-1.0, min(1.0, puntuacion_float))
            puntuacion_str = f"{puntuacion_float:.2f}"

            cursor.execute(
                "INSERT INTO ReseñasAnalizadas (texto, puntuacion) VALUES (?, ?)",
                (reseñas[i], puntuacion_str)
            )

            print(f"✅ Reseña procesada correctamente:")
            print(f"Texto: {reseñas[i]}")
            print(f"Puntuación: {puntuacion_str}")

        except ValueError as e:
            print(f"❌ Error en formato: {resultados[i]} - {str(e)}")
        except Exception as e:
            print(f"❌ Error inesperado: {str(e)}")

    conn.commit()
    conn.close()

else:
    print("❌ No se cargó la API key. Revisa el archivo .env.")
