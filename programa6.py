carpeta="Documents\\"
archivo_nombre="Documento2.txt"
with open(archivo_nombre,"r") as archivo: 
    texto=archivo.read() 
    palabras_lista=texto.split() 
    palabras_lista.sort() 
for palabra in palabras_lista: 
    print(palabra)   
    