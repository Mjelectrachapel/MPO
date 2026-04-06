numero= int(input("Introduce un número entero"))
for i in range(numero+1):
  if i%3==0 and i%5==0:
    print(f"El número {i} es múltiplo de cinco y de tres")
  elif i%5==0:
    print(f"El número {i} es múltiplo de cinco")
  elif i%3==0:
    print(f"El número {i} es múltiplo de tres")
  else:
    print(f"El número {i} no es múltiplo ni de tres ni de cinco")
