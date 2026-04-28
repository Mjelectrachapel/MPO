numero = int(input("Introduce un número: "))
contador = 0

for i in range(2, numero):
  if numero % i == 0:
    print("El número no es primo")
    break
  if i == numero:
    print("El número es primo")
