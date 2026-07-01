
def elegir_tema():
    print("--------TEMAS--------")
    print("1. One Piece")
    print("2. Mitología")
    print("3. Juego de Tronos")

    opcion = input("Elige un tema: ")

    while opcion not in ("1", "2", "3"):
        print("Opción no válida")
        opcion = input("Elige un tema: ")

    if opcion == "1":
        return "preguntas_one_piece.json"
    elif opcion == "2":
        return "preguntas_mitologia.json"
    elif opcion == "3":
        return "preguntas_got.json"
    
    
def cargar_preguntas(nombre_archivo):
    from pathlib import Path
    import json

    ruta = Path(__file__).parent / nombre_archivo

    with open(ruta, "r", encoding="utf-8") as archivo:
        preguntas = json.load(archivo)
    return preguntas

def mostrar_pregunta(pregunta):
    
    print(pregunta["pregunta"])

    for opcion in pregunta["opciones"]:
        print (opcion)
    
def obtener_respuesta():
    respuesta = input("Introduzca su respuesta( escribiendo A,B,C o D) \n")
    while respuesta not in ("A","B","C","D"):
        print("Ha introducido una respuesta no válida")
        respuesta = input("Introduzca su respuesta( escribiendo A,B,C o D) \n")
        
    return respuesta

def corregir_respuesta(respuesta,correcta):
    if respuesta == correcta:
        return 1
    else:
        return 0

def mostrar_resultados(aciertos,total):
    print("------------------------------")
    print("---------RESULTADOS-----------")
    print(f"Has acertado {aciertos} preguntas de {total}")
    porcentaje = (aciertos*100)/total
    print(f"Tu porcentaje de acierto es del {porcentaje} %")
    if porcentaje >=85:
       print("¡Muy Buen trabajo!")
    elif porcentaje >=70:
        print("Bien hecho, repasa un poco más")    
    else:
        print("Repasa y vuelve a intentarlo")
    print("------------------------------")
    
def actualizar_ranking(nombre,puntuacion):
    import json
    from pathlib import Path

    ruta = Path(__file__).parent / "ranking.json"

    with open(ruta, "r", encoding="utf-8") as archivo:
        ranking = json.load(archivo)

        ranking[nombre] = puntuacion

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(ranking, archivo, indent=4, ensure_ascii=False)

def consultar_ranking():
    import json
    from pathlib import Path

    ruta = Path(__file__).parent / "ranking.json"

    with open(ruta, "r", encoding="utf-8") as archivo:
        ranking = json.load(archivo)

    return ranking
        