c="C:\\Users\\Monse Peralta\\Documents\\optativa\\"
e="documento2.txt"
s="archivo_nuevo.txt"
#leer archivos y abrirlos
e2=open(c+e,"r")
#print(e2.read())

s2=open(c+s,"w")
t=e2.read()

#se crea la carpeta
t2=t
s2.write(t2)
#s3=open(c+s,"r")
#print(s3.read())

#nueva forma de abrir archivo

with open(c+s,"r") as archivo:
    texto=archivo.read()
palabra=input("Escribe la palabra a buscar: ")
print(texto)

#s3.close()

#e2.close()
#s2.close()

#en el archivo nuevo se va modificando y guardando el contenido

#-------if------------
#buscar la palabra en documento
if palabra in texto:
    print("encontro la palabra ")
else:
    print("No encontro la palabra")


#-----listas ----------
    #las variables pueden tener mas de un valor
    #una variable puede ser una lista
    #el indice de una lista comienza en 0 y pueden agrupar un conjunto de datos relacionados entre si
    #la longitut se dice len
    #append =agregar
    
