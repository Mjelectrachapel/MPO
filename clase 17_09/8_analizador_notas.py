notas = [int(num) for num in input("Introduce una lista de notas separadas por coma: ").split(",")]
maximo = notas[0]
minimo = notas[0]
suma = 0
aprobados = 0
suspensos = 0
for nota in notas:
  if nota > maximo:
    maximo = nota
  if nota < minimo:
    minimo = nota
  suma += nota
  if nota >= 5:
    aprobados += 1
  else:
    suspensos += 1

media = suma/len(notas)

print(f"Notas = {notas}")
print(f"Máxima: {maximo}")
print(f"Mínima: {minimo}")
print (f"Media: {media}")
print(f"Aprobados: {aprobados}")
print(f"Suspensos: {suspensos}")

