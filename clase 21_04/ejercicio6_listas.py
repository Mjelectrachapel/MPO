"""
Escribe un programa que reciba números hasta la introducción de un 0.
Por cada número, suponiendo que el 1 representa el lunes, el 2 el martes, etc.
imprime el nombre del día correspondiente.
"""
numero = int(input("Introduce un número:" ))
semana = ["stop","lunes","martes","miércoles","jueves","viernes","sábado","domingo"]

while numero != 0:
  print(f"El día de la semana es:{semana[numero]} ")
  numero= int(input("Introduce otro número\n"))
