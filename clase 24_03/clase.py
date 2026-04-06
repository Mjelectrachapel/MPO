#Bucle while
#while condition:
#   líneas de codigo que se van a ejecutar
#programa que cuenta el numero de la clase hasta que pongamos el nombre del profesor (Jordi)
#nombre= input("Introduce nombre del alumno o de profesor(para acabar)")
#num_alumnos=0
#while nombre != "Jordi":
 # num_alumnos+=1
  #nombre= input("Introduce nombre del alumno o de profesor(para acabar)")

#print(f"Total de alumnos: {num_alumnos}")




#programa que vaya recibiendo numeros y vaya sumando hasta recibir un numero negativo

numero= int(input("Introduce un número\n"))
suma=0

while numero >=0:
  suma= suma + numero
  numero= int(input("Introduce otro número\n"))
print(f"Suma de todos los números positivos: {suma}")
