numero_secreto = 58
intentos = 0

while True:
  intento = int(input("Adivina el número secreto: "))
  intentos+=1
  if intento == numero_secreto:
    print("¡Correcto!")
    print(f"Intentos: {intentos}")

    break
  elif intento < numero_secreto:
    print("Demasiado bajo")
  else:
    print("Demasiado alto")
