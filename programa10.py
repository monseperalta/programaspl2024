#EXPRESIONES REGULARES:

#sirven para identificar patrones y comportamientos
import re

carpeta="Documentos\\"
archivo_nombre="Documento2.txt"
with open(archivo_nombre,"r") as archivo:  #r:esta manera, Python sabe que no debe esperar caracteres especiales, más que de expresiones regulares.
    texto=archivo.read()
    expresion_regular=re.compile(r"^version")   #busca la palabra como expresion no como cadena, es lo que indica la R
    resultado_busqueda=expresion_regular.search(texto)   #search muestra la primera coincidencia que se enceuntre: solo una
    print(resultado_busqueda.group(0))

#busca todas la palabra y muestra todas las veces que apares.ca
expresion_regular=re.compile(r"^version")   #el astedisco permite cualquier cantidad de repeticiones del simbolo que procede
resultado_busqueda=expresion_regular.finditer(texto)
print(resultado.group(0))

