"""Proyecto 2: Gestor de archivos en consola."""
import os
import datetime

def mostrar_menu():
    """Muestra las opciones del menú y la ruta actual"""
    print("\n=== GESTOR DE ARCHIVOS ===")
    print("Ruta actual:", os.getcwd())
    print("1. Listar contenido")
    print("2. Crear directorio")
    print("3. Crear archivo")
    print("4. Escribir en archivo")
    print("5. Eliminar archivo o directorio")
    print("6. Mostrar información")
    print("7. Salir")
    print("8. Subir al directorio padre")
    print("9.Renombrar archivo o directorio")


def listar_contenido():
    """Lista el contenido indicando si es archivo o carpeta"""
    elementos = os.listdir(".")
    for elemento in elementos:
        if os.path.isdir(elemento):
            print(f"[CARPETA] {elemento}")
        else:
            print(f"[ARCHIVO] {elemento}")


def crear_directorio():
    """Pide un nombre y crea una carpeta nueva"""
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
    """Crea un archivo de texto con un contenido inicial"""
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
    """Añade texto al final de un archivo existente"""
    nombre = input("Nombre del archivo: ")
    if nombre.strip() == "":
        print("Error: el nombre no puede estar vacío.")
        return
    try:
        if not os.path.isfile(nombre):
            print("Error: no existe ningún archivo con ese nombre.")
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
    """Elimina un archivo o un directorio vacío"""
    nombre = input("Nombre del archivo o directorio a eliminar: ")
    if nombre.strip() == "":
        print("Error: el nombre no puede estar vacío.")
        return
    try:
        if not os.path.exists(nombre):
            print("Error: no existe ningún archivo o directorio con ese nombre")
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
    """Muestra tipo, tamaño y fecha de modificación"""
    nombre = input("Nombre del archivo o directorio: ")
    if nombre.strip() == "":
        print("Error: el nombre no puede estar vacío.")
        return
    if not os.path.exists(nombre):
        print(f"Error: no existe ningún archivo o directorio llamado {nombre}.")
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


def ir_a_directorio_padre():
    """Sube al directorio padre del directorio actual"""
    os.chdir("..")
    print("Ahora estás en:", os.getcwd())


def renombrar_elemento():
    """Cambia el nombre de un archivo o directorio"""
    antiguo = input("Nombre actual: ")
    if antiguo.strip() == "":
        print("Error: el nombre no puede estar vacío.")
        return
    nuevo = input("Nombre nuevo: ")
    if nuevo.strip() == "":
        print("Error: el nuevo nombre no puede estar vacío.")
        return
    try:
        if not os.path.exists(antiguo):
            print("Error: no existe ningún archivo o directorio con ese nombre")
        elif os.path.exists(nuevo):
            print("Error: ya existe un archivo o directorio con ese nombre")
        else:
            os.rename(antiguo, nuevo)
            print(f"Renombrado: {antiguo} -> {nuevo}")
    except PermissionError:
        print("Error: no tienes permisos para cambiar el nombre.")
    except OSError as error:
        print(f"Error: no se pudo cambiar el nombre del elemento seleccionado ({error})")


def main():
    """Ejecuta el bucle principal del menú"""
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
        elif opcion == "8":
            ir_a_directorio_padre()
        elif opcion == "9":
            renombrar_elemento()
        else:
            print("Opción no válida")


main()
