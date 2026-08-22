import string
import secrets


def generar_caracteres(mayusculas, minusculas, numeros, especiales):
    caracteres = ""

    if mayusculas:
        caracteres += string.ascii_uppercase

    if minusculas:
        caracteres += string.ascii_lowercase

    if numeros:
        caracteres += string.digits

    if especiales:
        caracteres += string.punctuation

    return caracteres


def generar_contrasena(longitud, caracteres):
    contrasena = ""

    for i in range(longitud):
        contrasena += secrets.choice(caracteres)

    return contrasena

def validar_longitud(longitud):
    if longitud < 8:
        return False

    return True

def guardar_historial(historial, contrasena):
    historial.append(contrasena)


def mostrar_historial(historial):
    if len(historial) == 0:
        print("No hay contraseñas en el historial.")
    else:
        print("\n===== HISTORIAL DE CONTRASEÑAS =====")

        for i, contrasena in enumerate(historial, start=1):
            print(f"{i}. {contrasena}")

def mostrar_menu():
    print("\n===== GENERADOR DE CONTRASEÑAS SEGURAS =====")
    print("1. Generar contraseña")
    print("2. Ver historial")
    print("3. Salir")