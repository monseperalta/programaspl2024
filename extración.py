#Crear un programa que nos permita analisar el texto de una pagina web y almacenarla en un txt
#guadalupe monserrat peralta sánchez

import requests
from bs4 import BeautifulSoup

def obtener_texto_desde_url(url):
    # Realizar la solicitud GET para obtener el contenido HTML de la página
    respuesta = requests.get(url)
    # Verificar si la solicitud fue exitosa
    if respuesta.status_code == 200:
        # Utilizar BeautifulSoup para analizar el HTML
        soup = BeautifulSoup(respuesta.content, 'html.parser')
        # Extraer el texto del contenido HTML
        texto = soup.get_text()
        return texto
    else:
        # Si la solicitud falla, imprimir un mensaje de error
        print("Error al obtener la página:", respuesta.status_code)
        return None

def guardar_texto_en_archivo(texto, nombre_archivo):
    # Escribir el texto en un archivo de texto
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(texto)
    print(f"El texto ha sido guardado en el archivo '{nombre_archivo}'.")

# URL de la página web que deseas analizar
url = 'https://es.wikipedia.org/wiki/BTS'

# Obtener el texto de la página web
texto_pagina = obtener_texto_desde_url(url)

if texto_pagina:
    # Nombre del archivo donde se guardará el texto
    nombre_archivo = 'texto_extraido.txt'
    # Guardar el texto en un archivo de texto
    guardar_texto_en_archivo(texto_pagina, nombre_archivo)
