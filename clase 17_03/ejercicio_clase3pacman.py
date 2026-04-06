numero1= int(input("Introduce el número de la casilla de Pacman: "))
numero2= int(input("Introduce el número de la casilla del Fantasma: "))
clave= input("Indica si la palabra clave es caramelo o normal: ")

if clave=="normal" and numero1==numero2:
  print("Pacman ha sido atrapado")
elif clave=="caramelo" and numero1==numero2:
  print("Pacman ha comido al fantasma")
else:
  print("Pacman ha escapado")

