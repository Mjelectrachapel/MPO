''' Escribe un programa que gestione un inventario de productos utilizando un diccionario.
 El programa debe permitir al usuario añadir productos con su nombre y cantidad, eliminar productos,
y consultar la cantidad de un producto específico. El programa debe ejecutarse indefinidamente 
hasta que el usuario introduzca "SALIR".'''

diccionario_productos = {}
 
entrada = input("Introduzca qué quiere hacer: 1. Añadir productos, 2. eliminar productos, 3. Consultar la cantidad de un producto, 4. SALIR ")
while entrada != "4":
    if entrada == 1:
        entrada = ("Introduzca un par producto: cantidad")
        producto, cantidad = entrada.split(":")
    diccionario_productos[producto] = cantidad
    entrada = ("Introduzca un par producto: cantidad")
    if entrada == 2:
        
