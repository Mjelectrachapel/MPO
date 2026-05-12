
''' Escribe un programa que pida al usuario un texto y cuente cuántas veces aparece cada palabra en el texto.
 El programa debe imprimir un diccionario donde las claves son las palabras 
 y los valores son sus respectivas frecuencias. Ignora la puntuación
  y considera las palabras en minúsculas.'''

import string

diccionario_palabras= {} #crea el diccionario 
texto = input("Introduzca un texto: ") #Pide al usuario un texto
texto = texto.lower().translate(str.maketrans('', '', string.punctuation)) #Convierte el texto a minúsculas y elimina las puntuaciones
palabras = [palabra for palabra in texto.split()] #separa el texto en palabras y usa el espacio como separador, lo mete en una lista 

for palabra in palabras:
    if palabra in diccionario_palabras:
        diccionario_palabras[palabra] += 1
    else:
        diccionario_palabras[palabra] = 1
print(diccionario_palabras)
