"""Proyecto 2: Gestor de archivos en consola."""
import os
import datetime

def mostrar_menu():
    print("\n=== GESTOR DE ARCHIVOS ===")
    print("Ruta actual:", os.getcwd())
    print("1. Listar contenido")
    print("2. Crear directorio")
    print("3. Crear archivo")
    print("4. Escribir en archivo")
    print("5. Eliminar archivo o directorio")
    print("6. Mostrar información")
    print("7. Salir")


def listar_contenido():
    elementos = os.listdir(".")
    for elemento in elementos:
        if os.path.isdir(elemento):
            print(f"[CARPETA] {elemento}")
        else:
            print(f"[ARCHIVO] {elemento}")


def crear_directorio():
    nombre = input("Nombre del nuevo directorio: ")
    if nombre.strip() == "":
        print("Error: el nombre no puede estar vacío.")
        return
    try:
        os.mkdir(nombre)
        print(f"Directorio creado: {nombre}")
    except FileExistsError:
        print("Error: ya existe algo con ese nombre.")
    except PermissionError:
        print("Error: no tienes permisos para crear aquí.")
    except OSError as error:
        print(f"Error: no se pudo crear el directorio ({error})")


def crear_archivo():
    nombre = input("Nombre del archivo: ")
    if nombre.strip() == "":
        print("Error: el nombre no puede estar vacío.")
        return
    try:
        if os.path.exists(nombre):
            print("Error: ya existe un archivo con ese nombre")
        else:
            contenido = input("Contenido inicial: ")
            with open(nombre, "w") as archivo:
                archivo.write(contenido + "\n")
            print(f"Archivo creado: {nombre}")
    except PermissionError:
        print("Error: no tienes permisos para crear aquí.")
    except OSError as error:
        print(f"Error: no se pudo crear el archivo ({error})")


def escribir_en_archivo():
    nombre = input("Nombre del archivo: ")
    if nombre.strip() == "":
        print("Error: el nombre no puede estar vacío.")
        return
    try:
        if not os.path.isfile(nombre):
            print("Error: no existe ningun archivo con ese nombre.")
        else:
            texto = input("Texto a añadir: ")
            with open(nombre, "a") as archivo:
                archivo.write(texto + "\n")
            print(f"Texto añadido al archivo: {nombre}")
    except PermissionError:
        print("Error: no tienes permisos para escribir aquí.")
    except OSError as error:
        print(f"Error: no se pudo escribir en el archivo ({error})")


def eliminar_elemento():
    nombre = input("Nombre del archivo o directorio a eliminar: ")
    if nombre.strip() == "":
        print("Error: el nombre no puede estar vacío.")
        return
    try:
        if not os.path.exists(nombre):
            print("Error: no existe ningun archivo o directorio con ese nombre")
        elif os.path.isfile(nombre):
            os.remove(nombre)
            print(f"Archivo eliminado: {nombre}")
        else:
            os.rmdir(nombre)
            print(f"Directorio eliminado: {nombre}")
    except PermissionError:
        print("Error: no tienes permisos para eliminar aquí.")
    except OSError as error:
        print(f"Error: no se pudo borrar el elemento seleccionado ({error})")


def mostrar_informacion():
    nombre = input("Nombre del archivo o directorio: ")
    if nombre.strip() == "":
        print("Error: el nombre no puede estar vacío.")
        return
    if not os.path.exists(nombre):
        print(f"Error: no existe ningun archivo o directorio llamado {nombre}.")
    else:
        if os.path.isfile(nombre):
            tipo = "Archivo"
        else:
            tipo = "Carpeta"
        tamanio = os.path.getsize(nombre)
        segundos = os.path.getmtime(nombre)
        fecha = datetime.datetime.fromtimestamp(segundos)

        print(f"Nombre: {nombre}")
        print(f"Tipo: {tipo}")
        print(f"Tamaño: {tamanio} B")
        print(f"Última modificación: {fecha.strftime('%d/%m/%Y %H:%M:%S')}")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            listar_contenido()
        elif opcion == "2":
            crear_directorio()
        elif opcion == "3":
            crear_archivo()
        elif opcion == "4":
            escribir_en_archivo()
        elif opcion == "5":
            eliminar_elemento()
        elif opcion == "6":
            mostrar_informacion()
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")


main()
