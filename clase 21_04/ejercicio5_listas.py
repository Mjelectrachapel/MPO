"""
Escribe un programa que pida al usuario una lista de números enteros separados por comas y la invierta.
 El programa debe imprimir la lista invertida.
"""
numeros = [int(x) for x in input("Introduce una serie de números separados por ,: ").split(",")]
numeros.reverse()
print(numeros)
