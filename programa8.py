#lista de archivos
import os   #instrucciones del sistema operativo, son las que ponemos en la consola 
carpeta_nombre="Documentos\\"
archivos_lista=os.listdir(carpeta_nombre)   #lisdir es para mostrar el directorio , instruccion mas basica

#nos permite ver elemento por elemento 

for archivo_nombre in archivos_lista:
    print(archivo_nombre)
