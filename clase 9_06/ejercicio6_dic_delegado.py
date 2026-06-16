'''
Escribe un programa que simule unas elecciones a delegado de clase.
El programa debe permitir a los alumnos votar por un candidato introduciendo su nombre.
Al finalizar la votación, el programa debe mostrar el nombre del candidato ganador y el número de votos obtenidos.
Si hay un empate, el programa debe informar al usuario del primer candidato que alcanzó el número máximo de votos.
El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "FIN VOTACIONES".

crear un diccionario que sea {candidato,votos} inicialmente votos es 0 en todos
hacer un while true para que en cada iteración añada un voto si los

'''
candidatos = {}

maximo = 0
ganador = ""

while True:
  voto = input("Introduce el nombre del candidato que quiera votar o FIN VOTACIONES para terminar el proceso de votación ")
  if voto == "FIN VOTACIONES":
    print("Votación finalizada")
    break

  elif voto in candidatos:
    candidatos[voto] += 1
  else:
    candidatos[voto] = 1

if candidatos[voto]>maximo:
  maximo = candidatos[voto]
  ganador = voto


print(f"El ganador es {ganador} con {maximo} votos")








