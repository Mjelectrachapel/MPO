numero = int(input("Introduce un número impar positivo\n"))

print("*"*numero)
for i in range(1, numero-1):

    fila = "*"

    for j in range(1,numero-1):

        if i == j or numero-1-i == j:
            fila += "*"

        else:
            fila += " "


    fila += "*"
    print(fila)

print("*"*numero)
