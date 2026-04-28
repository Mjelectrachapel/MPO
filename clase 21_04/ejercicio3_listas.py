"""
Escribe un programa que pida al usuario una lista de números enteros separados por comas
y encuentre el mayor y el menor elemento de la lista.
El programa debe imprimir ambos resultados.

"""
numeros = input("Introduce una serie de números enteros separados por ,: ")
lista_numeros= [int(x) for x in numeros.split(",")]
lista_numeros.sort()
print(f"El menor elemento de la lista introducida es: {lista_numeros[0]}" )
print(f"El mayor elemento de la lista introducida es: {lista_numeros[-1]}" )

