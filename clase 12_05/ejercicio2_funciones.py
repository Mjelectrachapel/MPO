def mensaje_bienvenida(nombre, apellido, edad):
    print (f"Hola {nombre} {apellido}, tu edad es de {edad} años")

nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))

mensaje_bienvenida(nombre,apellido,edad)