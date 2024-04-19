import os
from docx import Document
import nltk

def convertir_docx_a_txt(ruta_docx, ruta_txt):
    try:
        # Abrir el documento .docx
        doc = Document(ruta_docx)
        
        # Crear/archivar el archivo .txt
        with open(ruta_txt, 'w', encoding='utf-8') as archivo_txt:
            # Escribir el contenido del documento en el archivo .txt
            for parrafo in doc.paragraphs:
                archivo_txt.write(parrafo.text + '\n')
        
        print("El documento .docx se ha convertido exitosamente a .txt.")
    except Exception as e:
        print(f"Error al convertir el documento: {e}")

def validar_documento(doc_nombre):
    if not os.path.exists(doc_nombre):
        print("El documento no existe. Por favor, verifica el nombre y vuelve a intentarlo.")
        return False
    return True

def contar_palabras(ruta_txt):
    try:
        # Abrir el archivo .txt y leer su contenido
        with open(ruta_txt, 'r', encoding='utf-8') as archivo_txt:
            contenido = archivo_txt.read()
        
        # Contar el número de palabras
        palabras = contenido.split()
        num_palabras = len(palabras)
        
        return num_palabras
    except Exception as e:
        print(f"Error al contar palabras: {e}")

def contar_lineas(ruta_txt):
    try:
        # Abrir el archivo .txt y leer su contenido línea por línea
        with open(ruta_txt, 'r', encoding='utf-8') as archivo_txt:
            lineas = archivo_txt.readlines()
        
        # Contar el número de líneas
        num_lineas = len(lineas)
        
        return num_lineas
    except Exception as e:
        print(f"Error al contar líneas: {e}")

def contar_palabra_en_texto(ruta_txt, palabra):
    try:
        # Abrir el archivo .txt y leer su contenido
        with open(ruta_txt, 'r', encoding='utf-8') as archivo_txt:
            contenido = archivo_txt.read()
        
        # Contar el número de veces que aparece la palabra en el texto
        num_veces = contenido.lower().count(palabra.lower())
        
        return num_veces
    except Exception as e:
        print(f"Error al contar la palabra en el texto: {e}")

carpeta_nombre = "Documentos\\"

while True:
    archivo_nombre = input("Ingrese el nombre del documento .docx: ")

    # Combinar la carpeta y el nombre del archivo .docx para obtener la ruta completa
    ruta_docx = os.path.join(carpeta_nombre, archivo_nombre)

    if validar_documento(ruta_docx):
        break

# Nombre del archivo .txt (sin extensión)
nombre_archivo_txt = os.path.splitext(archivo_nombre)[0] + ".txt"

# Combinar la carpeta y el nombre del archivo .txt para obtener la ruta completa
ruta_txt = os.path.join(carpeta_nombre, nombre_archivo_txt)

# Convertir el archivo .docx a .txt
convertir_docx_a_txt(ruta_docx, ruta_txt)

# Contar el número de palabras en el texto
num_palabras = contar_palabras(ruta_txt)
print(f"Número de palabras en el texto: {num_palabras}")

# Contar el número de líneas en el texto
num_lineas = contar_lineas(ruta_txt)
print(f"Número de líneas en el texto: {num_lineas}")

# Palabra a buscar en el texto
palabra_a_buscar = input("Ingrese la palabra que desea buscar en el texto: ")
num_veces_palabra = contar_palabra_en_texto(ruta_txt, palabra_a_buscar)
print(f"La palabra '{palabra_a_buscar}' aparece {num_veces_palabra} veces en el texto.")



# Cargar el texto del archivo
archivo_nombre = "servidor telnet.txt"
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
distribucion_limpia.plot(20)
