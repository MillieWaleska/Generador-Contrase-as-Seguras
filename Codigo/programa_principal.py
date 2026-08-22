from funciones import (
    generar_caracteres,
    generar_contrasena,
    validar_longitud,
    guardar_historial,
    mostrar_historial,
    mostrar_menu
)


historial = []


while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        try:
            longitud = int(input("Ingrese la longitud de la contraseña: "))

            if validar_longitud(longitud):

                mayusculas = input(
                    "¿Incluir mayúsculas? (s/n): "
                ).lower() == "s"

                minusculas = input(
                    "¿Incluir minúsculas? (s/n): "
                ).lower() == "s"

                numeros = input(
                    "¿Incluir números? (s/n): "
                ).lower() == "s"

                especiales = input(
                    "¿Incluir caracteres especiales? (s/n): "
                ).lower() == "s"

                caracteres = generar_caracteres(
                    mayusculas,
                    minusculas,
                    numeros,
                    especiales
                )

                if caracteres == "":
                    print("Debe seleccionar al menos un tipo de carácter.")

                else:
                    contrasena = generar_contrasena(
                        longitud,
                        caracteres
                    )

                    guardar_historial(
                        historial,
                        contrasena
                    )

                    print("\nContraseña generada:")
                    print(contrasena)

            else:
                print("La longitud debe ser de mínimo 8 caracteres.")

        except ValueError:
            print("Error: debe ingresar un número válido.")

    elif opcion == "2":

        mostrar_historial(historial)

    elif opcion == "3":

        print("Programa finalizado.")
        break

    else:

        print("Opción no válida. Seleccione 1, 2 o 3.")