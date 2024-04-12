#poder ver la frecuecnia con que se utilizan las palabras en el docuemno y  tambien obtener la
#frecuencia de una palabra en particular.

#observar de una manera visual cómo
#cambia la frecuencia de las palabras. 
 #Las distribuciones de NLTK tienen opciones para obtener gráficas.
#se utilizara la fucion plot()
import nltk

carpeta_nombre="Documentos\\"
archivos_nombre="Documento2.txt"

with open(carpeta_nombre+archivos_nombre,"r") as archivo:
    texto=archivo.read()

    tokens=nltk.word_tokenize(texto,"spanish")  #el idioma del texto que tengo
    texto_nltk=nltk.Text(tokens)
    distribucion=nltk.FreqDist(texto_nltk)
    lista_frecuencias=distribucion.most_common()
    print(lista_frecuencias)

    #A esta altura ya tenemos la lista de tokens en "tokens"

    texto_nltk=nltk.Text(tokens)
    distribucion=nltk.FreqDist(texto_nltk)
    print(distribucion["Instituto"]) 