''' Escribe un programa que gestione un inventario de productos utilizando un diccionario.
 El programa debe permitir al usuario añadir productos con su nombre y cantidad, eliminar productos,
y consultar la cantidad de un producto específico. El programa debe ejecutarse indefinidamente
hasta que el usuario introduzca "SALIR".'''

diccionario_productos = {"Paracetamoles": 4,
                          "Ibuprofeno": 5,
                          "Almax": 6
                         }



while True:
    entrada = input("""
                Introduzca qué quiere hacer:
                1. Añadir productos
                2. eliminar productos
                3. Consultar la cantidad de un producto
                4. SALIR """)

    if entrada == 1:
      entrada = ("Introduzca un par producto: cantidad")
      producto, cantidad = entrada.split(":")
      if producto in diccionario_productos:
        diccionario_productos[producto] += cantidad
      else:
        diccionario_productos[producto] = cantidad
    elif entrada == 2:



