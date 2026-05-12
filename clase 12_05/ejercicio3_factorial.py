def factorial (numero):
    resultado = 1
    for i in range (numero,0,-1):
        resultado *= i
    return resultado

numero = int(input("Introduce el numero del que quieres calcular el fatorial"))
print(f"El factorial de {numero} es {factorial(numero)}")
