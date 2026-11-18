try:
  with open("clase15_10y22_10\\cosas.txt","r") as archivo:
    numerolineas = len(archivo.readlines())
  print (f"El archivo tiene {numerolineas} líneas.")
except FileNotFoundError as error:
  print(f"Error: {error}")
