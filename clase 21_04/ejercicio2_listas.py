"""
Escribe un programa que pida al usuario una lista de palabras separadas por comas
 y cuente cuántas palabras hay en la lista.
 El programa debe imprimir el resultado.

"""
palabras = input("Introduce una serie de palabras separadas por ,: ").split(",")
print(len(palabras))
