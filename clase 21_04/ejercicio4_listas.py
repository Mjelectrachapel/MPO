"""
Escribe un programa que pida al usuario dos listas de números enteros separados por comas
 y sume los elementos de ambas listas. El programa debe imprimir la lista resultante. 
Si las listas no tienen la misma longitud, el programa debe imprimir un mensaje de error.
"""
numeros1 = input("Introduce una serie de números separados por ,: ")
numeros2 = input("Introduce otra serie de números separados por ,: ")
lista1= [int(x) for x in numeros1.split(",")]
lista2= [int(x) for x in numeros2.split(",")]

if len(lista1)!=len(lista2):
    print("La longitud de las listas no puede ser diferente")
else:
    lista_suma=[x+y for x,y in zip(lista1,lista2)]
    print(f"La suma de los elementos de ambas listas es: {lista_suma}")
