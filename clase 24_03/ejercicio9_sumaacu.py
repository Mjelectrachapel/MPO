numero= int(input("Introduce un número entero\n"))
suma=0

while numero !=0:
  suma += numero
  numero= int(input("Introduce otro número entero\n"))
print(f"Suma de todos los números introducidos: {suma}")
