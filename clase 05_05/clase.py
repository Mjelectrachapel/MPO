#Un diccionario es un tipo de dato complejo
#que almacena pares clave-valor

#Para inicializar un diccionario podemos:
mi_diccionario = {}
mi_diccionario2 = dict(profes="Vic", módulos=["PSP","DIW"])

#Para crear una entrada en el diccionario podemos usar:
mi_diccionario["Jordi"] = ["Entornos de desarrollo", "MPO"] #Elv
mi_diccionario["Jose"] = ["Programación"]
mi_diccionario["Alberto"] = ["BDD"]
mi_diccionario["Susana"] = ["Sistemas", "Lenguajes de marcas"]
mi_diccionario["Ismael"] = ["IPE"]

#Para acceder a un valor del diccionario, debo hacerlo por su clave:
nombre_profe = "Jordi"
print(f"El profesor {nombre_profe} es {mi_diccionario[nombre_profe]}")

#Para elimina un par clave-valor
del mi_diccionario["Jose"]
print(mi_diccionario.pop("Jordi"))

#Para comprobar si una clave existe, podemos hacerlo:
if "Alberto" in mi_diccionario:
  print(f"La clave Alberto existe y tiene valor {mi_diccionario["Alberto"]}")

#Recorrer un diccionario podemos hacerlo de 3 maneras:
# 1. Por claves
# 2. Por valores
# 3. Por pares clave-valor
for nombre_profe in mi_diccionario:
  print(f"La clave{nombre_profe} tiene el valor {mi_diccionario^[nombre_profe]}")

for asignaturas in mi_diccionario.values():
  print(f"Módulos impartidos: {asignaturas}")

for nombre_profe, asignaturas in mi_diccionario.items():
  print(f"El profe {nombre_profe} imparte los módulos{asignaturas}")

#Añade una entrada al diccionario
mi_diccionario["Jesus"]=["Aún nada"]
