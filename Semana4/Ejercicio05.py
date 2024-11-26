#-----------Ejercicio 5---------------
notas_aprovadas= 0 
notas_desaprovadas= 0 
promedio_aprovadas= 0
promedio_desaprovadas=0
promedio_total=0
contador=1
cantidad_notas= int (input("Ingrese la cantidad de notas: "))

for i in range (contador <= cantidad_notas):
    nota= int(input("Ingrese la nota del estudiante: "))
    if nota >= 70: 
        notas_aprovadas= notas_aprovadas + 1 
        promedio_aprovadas = promedio_aprovadas + nota
    else:
        notas_desaprovadas= notas_desaprovadas + 1
        promedio_desaprovadas= promedio_desaprovadas + nota
    promedio_total= promedio_total + (nota / cantidad_notas)

promedio_aprovadas= promedio_aprovadas / notas_aprovadas
promedio_desaprovadas= promedio_desaprovadas / notas_desaprovadas
print ("la cantidad de aprobadas son: ", notas_aprovadas )
print ("la cantidad de desaprobadas son: ", notas_desaprovadas )
print ("el promedio de aprovadas es: ", promedio_aprovadas )
print ("el promedio de desaprovadas es: ", promedio_desaprovadas )
print ("el promedio total es: ", promedio_total)