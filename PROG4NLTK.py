#GUADALUPE MONSERRAT PERALTA SÁNCHEZ

#El ejercicio consiste en encontrar todos los documentos DOC y DOCX de una carpeta usando
#expresiones regulares.

import os
import re
carpeta_nombre="C://Users//Monse Peralta//Documents//servicio"


archivos_lista=os.listdir(carpeta_nombre)

expresion_regular=re.compile(r"\.docx?$")

for archivos_nombre in archivos_lista:
    resultado_busqueda=expresion_regular.search(archivos_nombre)

if resultado_busqueda:
    print(resultado_busqueda.group(0))
print(archivos_nombre)