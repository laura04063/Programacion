#Ejercicio 4
#Cree un programa que elimine todos los números impares de una lista.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(lista):
    if lista[i] % 2 != 0:
        lista.pop(i)
    else:
        i += 1
print(lista)