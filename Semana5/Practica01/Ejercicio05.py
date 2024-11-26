#Ejercicio 5 
#Cree un programa que le pida al usuario 10 números, y al final le 
# muestre todos los números que ingresó, seguido del numero ingresado más alto.
numeros = []
for i in range(10):
    numero = int(input("Ingrese 1 número: "))
    numeros.append(numero)
    if i == 0:
        numero_maximo = numero
    elif numero > numero_maximo:
        numero_maximo = numero
print(numeros)
print(f"El número más alto fue {numero_maximo}.")
