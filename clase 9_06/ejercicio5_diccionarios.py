'''
Escribe un programa que gestione una biblioteca digital utilizando un diccionario.
El programa debe permitir al usuario añadir libros con su título, autor y año de publicación.
El usuario debe poder consultar los libros por autor o por año de publicación.
El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR".

'''

biblioteca = []

while True:
  print("OPCIONES DE BIBLIOTECA")
  print("1. Añadir libro")
  print("2. Consultar libros por autor")
  print("3. Consultar libros por año de publicación")
  print("4. Salir" )

  opcion = int(input("Selecciona una opción: "))
  match opcion:
    case 1:
      #pedir título
      #pedir autor
      #pedir año de publicacion
      titulo = input("Introduce al título del libro: ")
      autor = input("Introduce el autor del libro: ")
      año =int(input("Introduce el año de publicación del libro"))
      libro = {
        "título": titulo,
        "autor": autor,
        "año": titulo,
      }
      biblioteca.append(libro)
      print(f"Se ha añadido el libro {titulo} correctamente.")
    case 2:
      autor = input("Introduce el autor a consultar: ")
      for libro in biblioteca:
         if autor == libro["autor"]:
          print(f"Los libros de {autor} son {libro[titulo]}")
    case 3:
      año = int(input("Introduce el año de publicación a consultar: "))
      for libro in biblioteca:
        if año == libro["año"]:
          print(f"Los libros del {año} son {libro[titulo]}")
    case 4:
      print("Adiós")
      break

