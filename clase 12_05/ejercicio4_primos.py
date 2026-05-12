def es_primo(numero):
    for i in range (2,numero):
        if numero%i==0:
            return False
        return True
    
numero = int(input("Introduce un número: "))
if es_primo(numero):
    print(f"El número {numero} es primo")
else:
    print(f"El numero {numero} no es primo")
    