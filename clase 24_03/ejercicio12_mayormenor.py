numero = int(input("Introduce un numero: "))
maximo = 0
minimo = 0

while numero != 0:
  if numero>maximo:
    maximo=numero
  elif numero < minimo:
    minimo = numero
  numero = int(input("introduce un número:"))
print(f"El mayor es {maximo}")
print(f"El menor es {minimo}")

