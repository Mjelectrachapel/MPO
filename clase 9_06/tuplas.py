'''
colección ordenada e INMUTABLE de elementos.
puede contener elementos de diferentes tipos
son más eficientes en memoria que las listas
si es solo un elemento es obligatorio porner tupla =(4,) esa coma
ejercicio 4, tupla de numeros:
Escribe un programa que pida al usuario una lista de números enteros separados por comas y almacene estos números en una tupla.
Luego, el programa debe calcular y mostrar la suma, el promedio, el número máximo y el número mínimo de la tupla.

'''
numeros = input("Escribe una serie de números separados por comas: ").split(",")
numeros_enteros = lista2= [int(x) for x in numeros]
tupla_nums= tuple(numeros_enteros)
print(tupla_nums)

suma = 0
maximo = tupla_nums[0]
minimo = tupla_nums[0]

for numero in tupla_nums:
  suma += numero
  if numero > maximo:
    maximo = numero
  elif numero < minimo:
    minimo = numero

print (f"Suma: {suma}")
print (f"Máximo: {maximo}")
print (f"Mínimo: {minimo}")
print (f"Promedio: {suma/len(tupla_nums)}")




