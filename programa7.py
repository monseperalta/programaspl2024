#imprimir un documento linea por linea
carpeta="Documentos\\"
archivo_nombre="Documento2.txt"
with open(archivo_nombre,"r") as archivo: 
    lineas_lista=archivo.readlines()   #readlines separa las lineas, hasta donde hay una marcacion de espacio como , o enter

#me agrega el numero de la linea 
num_linea=1
lin_vacias=0
lin_texto=0
lin_total=len(lineas_lista)

for linea in lineas_lista:
    #nos identifica cuando hay lineas vacias 
    if linea.strip()=="":  #strip ve las lineas vacias , si hay las omite y imprime nada mas las que tengas texto
        print("linea vacia")
        lin_vacias=lin_vacias+1

        continue   #permite que siga ejecutandoce el programa en las siguientes lineas

    print("Numero de linea: ",num_linea,":",linea)
    num_linea=num_linea+1
    lin_texto=lin_texto+1

print("Lineas totales: ",lin_total)
print("Lineas vacias: ",lin_vacias)
print("Lineas con texto: ",lin_texto)


print("Fin del archivo")

    
    
#indicar cuando una linea es vacia
#cuantas acias son
#cuantas con texto son 
