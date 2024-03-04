import nltk
nltk.download('punkt')

carpeta_nombre="Documentos\\"
archivos_nombre="Documento2.txt"

with open(carpeta_nombre+archivos_nombre,"r") as archivo:
 texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")
for token in tokens:
 print(token)

palabras_total=len(tokens)
print(palabras_total)