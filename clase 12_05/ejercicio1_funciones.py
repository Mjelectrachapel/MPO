import math

def area_circulo(radio):
    print(f"El área del círculo es {radio} es {math.pi*(radio**2):.2f}")

radio = float(input("Introduce el radio del círculo del que quieras saber su área"))
area_circulo(radio)
