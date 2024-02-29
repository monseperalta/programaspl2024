#listas------------------
#este ejemplo utiliza listas, como los dias de la semana
semana_laboral=["Lunes","Martes","Miercoles","Jueves","Viernes"]
print("Semana Laboral=",semana_laboral)
print("Dia 1: ",semana_laboral[4])
semana_laboral[4]="sabado"
print("Semana Laboral=",semana_laboral)
semana_laboral[4]="Viernes"
longitud_lista=len(semana_laboral)
print("longitud: ",longitud_lista)
posicion=semana_laboral.index("Miercoles")
print("Posicion de miercoles= ",posicion)
semana_laboral.append("Sabado")  #append agregar datos, lo agrega al final de la lista
print("semana laboral: ", semana_laboral)
del semana_laboral[4]  #borra un elementoo de la lista 
print("Semana Laboral: ",semana_laboral)

