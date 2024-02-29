import re

carpeta="Documentos\\"
archivo_nombre="Documento2.txt"
with open(archivo_nombre,"r") as archivo:  #r:esta manera, Python sabe que no debe esperar caracteres especiales, más que de expresiones regulares.
    texto=archivo.read()

expresion_regular=re.compile(r"version")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))