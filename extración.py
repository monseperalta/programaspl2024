#Crear un programa que nos permita analisar el texto de una pagina web y almacenarla en un txt
#guadalupe monserrat peralta sánchez

import requests
from bs4 import BeautifulSoup
import re
import nltk 

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

def contar_palabras(texto):
    # Contar el número de palabras en el texto
    palabras = texto.split()
    num_palabras = len(palabras)
    return num_palabras

def contar_lineas(texto):
    # Contar el número de líneas en el texto
    lineas = texto.split('\n')
    num_lineas = len(lineas)
    return num_lineas

def palabras_cortas(texto):
    # Mostrar palabras de 3 o 4 caracteres
    palabras_cortas = re.findall(r'\b\w{3,4}\b', texto)
    return palabras_cortas

def contar_palabra_especifica(texto, palabra):
    # Contar el número de veces que aparece una palabra específica en el texto
    contador = texto.lower().count(palabra.lower())
    return contador

# Solicitar al usuario que ingrese la URL de la página web
url = input("Ingrese la URL de la página web: ")

# Obtener el texto de la página web
texto_pagina = obtener_texto_desde_url(url)

if texto_pagina:
    # Nombre del archivo donde se guardará el texto
    nombre_archivo = 'texto_extraido.txt'
    # Guardar el texto en un archivo de texto
    guardar_texto_en_archivo(texto_pagina, nombre_archivo)

    # Contar el número de palabras
    num_palabras = contar_palabras(texto_pagina)
    print("Número de palabras:", num_palabras)

    # Contar el número de líneas
    num_lineas = contar_lineas(texto_pagina)
    print("Número de líneas:", num_lineas)

    # Mostrar palabras de 3 o 4 caracteres
    palabras_cortas = palabras_cortas(texto_pagina)
    print("Palabras de 3 o 4 caracteres:", palabras_cortas)

    # Contar el número de veces que aparece una palabra específica
    palabra_especifica = input("Ingrese la palabra que desea contar en el texto: ")
    num_veces_palabra = contar_palabra_especifica(texto_pagina, palabra_especifica)
    print(f"La palabra '{palabra_especifica}' aparece {num_veces_palabra} veces en el texto.")

    # Guardar el texto extraído en un archivo de texto
if texto_pagina:
    with open("texto_extraido.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto_pagina)

# Cargar el texto del archivo
archivo_nombre = "texto_extraido.txt"
with open(archivo_nombre, "r", encoding="utf-8") as archivo:
    texto = archivo.read()

print("----------------------------------------------------------------------")

# Cargar palabras funcionales en español de NLTK
palabras_funcionales = nltk.corpus.stopwords.words("spanish")
for palabras_funcional in palabras_funcionales:
    print(palabras_funcional)

print("----------------------------------------------------------------------")

# Tokenizar el texto y eliminar palabras funcionales
tokens = nltk.word_tokenize(texto, "spanish")
tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

# Imprimir algunos detalles sobre los tokens
print(tokens_limpios)
print("Número total de tokens:", len(tokens))
print("Número de tokens limpios:", len(tokens_limpios))

# Crear un objeto Text de NLTK y calcular la distribución de frecuencia
texto_limpio_nltk = nltk.Text(tokens_limpios)
distribucion_limpia = nltk.FreqDist(texto_limpio_nltk)

# Graficar las 40 palabras más comunes
distribucion_limpia.plot(40)


