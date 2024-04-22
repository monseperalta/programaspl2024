import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

def save_text_to_txt(text, txt_path):
    with open(txt_path, 'w', encoding='utf-8') as file:
        file.write(text)

def count_words(text):
    # Tokenización
    tokens = word_tokenize(text)

    # Remover stopwords
    stop_words = set(stopwords.words('english'))  # Puedes cambiar 'english' por tu idioma
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

    # Contar palabras totales
    total_words = len(filtered_tokens)

    # Contar palabras únicas
    unique_words = set(filtered_tokens)

    # Contar palabras que aparecen solo una vez
    single_occur_words = [word for word in unique_words if filtered_tokens.count(word) == 1]

    # Distribución de frecuencia
    fdist = FreqDist(filtered_tokens)

    # Obtener las 20 palabras más comunes
    top_20_words = fdist.most_common(20)

    return total_words, single_occur_words, fdist, top_20_words

def plot_frequency_distribution(fdist, title="Frequency Distribution"):
    fdist.plot(20, cumulative=False)
    plt.title(title)
    plt.show()

def main():
    pdf_path = 'INVESTIGACION DE PROTOCOLOS_PERALTA.pdf'  # Reemplaza 'documento.pdf' con la ruta de tu archivo PDF
    txt_path = 'PDF_extraido.txt'  # Nombre del archivo .txt donde se guardará el texto extraído

    # Extraer texto del PDF
    extracted_text = extract_text_from_pdf(pdf_path)

    # Guardar texto extraído en un archivo .txt
    save_text_to_txt(extracted_text, txt_path)

    print("Texto extraído y guardado exitosamente en", txt_path)

    # Contar palabras y obtener distribución de frecuencia
    total_words, single_occur_words, fdist, top_20_words = count_words(extracted_text)

    # Imprimir resultados
    print("Número total de palabras:", total_words)
    print("Palabras que aparecen una sola vez:", single_occur_words)
    print("Distribución de frecuencia:", fdist)
    print("20 palabras más comunes:", top_20_words)

    # Graficar distribución de frecuencia
    plot_frequency_distribution(fdist)

if __name__ == "__main__":
    main()


