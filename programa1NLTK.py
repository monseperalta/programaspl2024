#El ejercicio consiste en encontrar todas las "palabras" de 3 o 4 letras
#Se entiende por "palabra" CUALQUIER coosa entre espacios

import re

carpeta_nombre="Documentos\\"
archivos_nombre="Documento2.txt"

with open(carpeta_nombre+archivos_nombre,"r") as archivo:
    texto=archivo.read()

expresion_regular=re.compile(r"...? ")

resultados_busqueda=expresion_regular.finditer(texto)  #busca en el texto las palabras regualres que cumlan con esta expresion las pone

for resultado in resultados_busqueda:
    print(resultado.group(0))