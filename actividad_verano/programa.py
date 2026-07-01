from funciones import *
nombre= input("Introduce tu nombre: ")
while True:
    print("--------MENÚ--------")
    print("1. Comenzar cuestionario")
    print("2.Consultar ranking")
    print("3. Salir")
    
    opcion= int(input("Elige qué quieres hacer "))
    match opcion:
        case 1:
            archivo = elegir_tema()
            preguntas = cargar_preguntas(archivo)

            aciertos= 0
            total=len(preguntas)

            for pregunta in preguntas:
                mostrar_pregunta(pregunta)
    
                respuesta=obtener_respuesta()

                aciertos += corregir_respuesta(respuesta, pregunta["respuesta_correcta"])

            mostrar_resultados(aciertos,total)
            actualizar_ranking(nombre,aciertos)
        case 2:
            ranking = consultar_ranking()
            
            print(ranking)
            
        case 3:
            print("Adiós")
            break    

