numeros = input("Introduce una serie de números separados por ,: ")
numeros = numeros.split(",")
resultado = 0

for i in numeros:
    resultado += int(i)
print (f"El resultado de la suma es {resultado}")
