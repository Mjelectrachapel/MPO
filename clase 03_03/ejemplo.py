"""
Entrada y salida de datos
entrada -->>> input() nos permite ingresar datos por teclado a nuestro programa en formato texto.
salida->>> print() nos imprime en pantalla lo que le indiquemos entre los parentesis, puede ser texto, numeros, variables, etc.






"""

módulo = input("¿Cuál es tu módulo favorito?\n")

print(f"Mi módulo favorito es {módulo}")

#Operaciones aritméticas
a= 10
b= 20
print(f"Suma: {a+b}")
print(f"Resta: {a-b}")
print(f"Multiplicación: {a*b}")
print(f"División decimal: {a/b}")
print(f"Division entera: {a//b}")
print(f"Módulo(resto): {a%b}")
print(f"Potencia: {a**b}")

#Operaciones comparativas
edad = int(input("¿Qué edad tienes?")) #Un solo igual asigna un valor a una variable

print(f"Es igual a 18?: {edad == 18}") #Dos iguales comparan valores
print(f"Es diferente a 18?: {edad != 18}")
print(f"Es mayor que 18?: {edad > 18}")
print(f"Es menor que 18?: {edad < 18}")
print(f"Es mayor o igual a 18?: {edad >= 18}")
print(f"Es mayor o igual a 18?: {edad <= 18}")

#Operaciones lógicas
años_cotizados= 40
print(f"Estás en edad de trabajar? {edad>=16 and edad<67}")
print(f"Te puedes prejubilar? {edad >= 60 or años_trabajados >= 35}")
print(f"¿Puedes trabajar?"{not edad<16})


#Asignación compuesta
numero = 1
numero += 2 #3
numero -=2  #1
numero *=5  #5

