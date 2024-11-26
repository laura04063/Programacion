#Ejercicio 3
#Cree un programa que intercambie el primer y ultimo elemento 
# de una lista. Debe funcionar con listas de cualquier tamaño.
elementos = ["estas", "como", "Hola,"]

if len(elementos) > 1:
    primer_elemento = elementos[0]
    ultimo_elemento = elementos[-1]
    elementos[0] = ultimo_elemento
    elementos[-1] = primer_elemento
print(elementos)