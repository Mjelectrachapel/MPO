def contarLineasYPalabras(contenido):
  num_lineas = len(contenido)
  num_palabras = 0
  for linea in contenido:
    if linea.strip():
      num_palabras+= len(linea.split())
  return num_lineas, num_palabras


try:
  with open("clase15_10y22_10\\cosas.txt", "r") as archivo:
    num_lineas, num_palabras = contarLineasYPalabras(archivo.readlines())
    print (f"El archivo contiene {num_lineas} lineas y {num_palabras} palabras")
except FileNotFoundError as error:
  print(f"Error: {error}")
