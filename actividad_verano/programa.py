from funciones import *

while True:
    print("--------MENÚ--------")
    print("1. Comenzar cuestionario")
    print("2. Salir")
    
    opcion= int(input("Elige qué quieres hacer"))
    match opcion:
        case 1:
            preguntas=cargar_preguntas()

            aciertos= 0
            total=len(preguntas)

            for pregunta in preguntas:
                mostrar_pregunta(pregunta)
    
                respuesta=obtener_respuesta()

                aciertos += corregir_respuesta(respuesta, pregunta["respuesta_correcta"])

            mostrar_resultados(aciertos,total)
        case 2:
            print("Adiós")
            break    
