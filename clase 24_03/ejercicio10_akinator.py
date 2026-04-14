import random

numero = random.randint (1,100)
guess = int(input("Adivina el número que estoy pensando:\n"))

while guess != numero:
  if guess < 1 or guess > 100:
    print ("El número debe ser entre 1 y 100")
  elif guess > numero:
    print ("El número que estoy pensando es menor que ese")
  else:
    print ("El número que estoy pensando es mayor que ese")
  guess = int(input("Vuelve a intentarlo\n"))

print (f"¡Muy bien! Lo has adivinado, el numero que he pensado era: {numero}")



