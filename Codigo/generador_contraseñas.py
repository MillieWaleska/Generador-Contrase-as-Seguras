import string
import secrets
# Mostrar menú e instrucciones
print("====================================")
print("   GENERADOR DE CONTRASEÑAS SEGURAS")
print("====================================")
print("Este programa genera una contraseña")
print("según la longitud y los tipos de")
print("caracteres seleccionados.")
print()
# Bucle principal para generar contraseñas
while True:

    # Solicitar y validar la longitud
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña: "))

            if longitud > 0:
                break
            else:
                print("Error: la longitud debe ser mayor que 0.")

        except ValueError:
            print("Error: debe ingresar un número válido.")

    # Preguntar qué tipos de caracteres desea incluir
    print("\nSeleccione los tipos de caracteres:")
    mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
    minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == "s"
    numeros = input("¿Incluir números? (s/n): ").lower() == "s"
    especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == "s"

    # Crear el conjunto de caracteres
    caracteres = ""

    if mayusculas:
        caracteres += string.ascii_uppercase

    if minusculas:
        caracteres += string.ascii_lowercase

    if numeros:
        caracteres += string.digits

    if especiales:
        caracteres += string.punctuation

    # Validar que al menos una opción haya sido seleccionada
    if caracteres == "":
        print("\nError: debe seleccionar al menos una opción.")
        continue

    # Generar la contraseña
    contraseña = ""

    while len(contraseña) < longitud:
        caracter = secrets.choice(caracteres)
        contraseña += caracter

    # Mostrar la contraseña generada
    print("\nContraseña generada:")
    print(contraseña)

    # Preguntar si desea generar otra contraseña
    otra = input("\n¿Desea generar otra contraseña? (s/n): ").lower()

    if otra != "s":
        print("\nPrograma finalizado.")
        break