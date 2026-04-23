"""
Escribe un programa que pida al usuario una lista de números enteros separados por comas y la invierta.
 El programa debe imprimir la lista invertida.
"""
numeros = input("Introduce una serie de números separados por ,: ")
lista = [int(x) for x in numeros.split(",")]
lista.reverse()
print(lista)
