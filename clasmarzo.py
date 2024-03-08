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

#nuestra lista de tokens se llama "tokens
tokens_conjunto=set(tokens)
palabras_totales=len(tokens)
palabras_diferentes=len(tokens_conjunto)

riqueza_lexica=palabras_diferentes/palabras_totales
print(riqueza_lexica)