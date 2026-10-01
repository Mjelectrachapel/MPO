inventario = ["espada", "poción", "escudo"]
opcion = ""

while opcion != "5":
  print("Menú: ")
  print("""1. Ver inventario
2. Añadir objeto
3. Usar objeto
4. Buscar objeto
5. Salir
""")
  opcion = input("Elige una opción: ")
  if opcion == "1":
    print(f"Inventario: {inventario}")
  elif opcion== "2":
    objeto = input("¿Qué objeto quieres añadir? ")
    inventario.append(objeto)
  elif opcion == "3":
    uso = input("¿Qué objeto quieres usar? ")
    if uso in inventario:
      inventario.remove(uso)
      print(f"Has usado {uso}")
    else:
      print("Ese objeto no está en el inventario")
  elif opcion == "4":
    busqueda= input("Objeto a buscar: ")
    if busqueda in inventario:
      print(f"Sí, tienes {inventario.count(busqueda)} de {busqueda}")
    else:
      print("Ese objeto no está en el inventario")
  elif opcion == "5":
    print("¡Adiós!")
  else:
    print("opción no válida")

