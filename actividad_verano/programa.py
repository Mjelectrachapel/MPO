from funciones import *

preguntas=cargar_preguntas()

aciertos= 0
total=len(preguntas)

for pregunta in preguntas:
    mostrar_pregunta(pregunta)
    
    respuesta=obtener_respuesta()

    aciertos += corregir_respuesta(respuesta, pregunta["respuesta_correcta"])

mostrar_resultados(aciertos,total)