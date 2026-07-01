def mostrar_menu():
    print("--------MENÚ--------")
    print("1. Comenzar cuestionario")
    print("2. Salir")

def cargar_preguntas():
    from pathlib import Path
    import json

    ruta = Path(__file__).parent / "preguntas.json"

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
    