numero= int(input("Introduce un número entero"))

if numero%3==0 and numero%5==0:
  print("El número introducido es múltiplo de cinco y de tres")
elif numero%5==0:
  print("El número introducido es múltiplo de cinco")
elif numero%3==0:
  print("El número introducido es múltiplo de tres")
else:
  print("El número no es múltiplo ni de tres ni de cinco")
