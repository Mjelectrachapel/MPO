
evaluaciones = int(input("Introduce el número de evaluaciones: "))

for i in range(1, evaluaciones + 1):
  nota = float(input(f"Notas de la evaluación {i}: "))
  suma_total = 0
  contador_notas= 0
  while nota != -1:
    suma_total += nota
    contador_notas += 1
    nota = float(input())
  print (f"La nota media de la evaluación {i} es {suma_total/contador_notas}")
