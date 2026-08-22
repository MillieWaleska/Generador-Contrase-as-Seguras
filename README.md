# Generador de Contraseñas Seguras

## 1. Descripción del proyecto

El proyecto consiste en el desarrollo de un sistema en Python para generar contraseñas seguras de manera aleatoria. El usuario puede establecer la longitud de la contraseña y seleccionar los tipos de caracteres que desea utilizar.

El sistema fue desarrollado como parte del proyecto integrador de la asignatura, aplicando conocimientos de programación, estructuras lógicas, organización del código, diseño funcional y arquitectura de software.

## 2. Problema

El uso de contraseñas débiles o fáciles de predecir representa un riesgo para la seguridad de la información. Muchas personas utilizan contraseñas cortas, repetitivas o poco variadas.

Por esta razón, se desarrolló una herramienta que permite generar contraseñas de forma aleatoria a partir de los criterios seleccionados por el usuario.

## 3. Objetivo del sistema

Desarrollar un generador de contraseñas seguras en Python que permita al usuario establecer la longitud de la contraseña y seleccionar diferentes tipos de caracteres para obtener una contraseña aleatoria.

## 4. Funcionalidades

El sistema cuenta con las siguientes funcionalidades:

- Generar una contraseña.
- Seleccionar la longitud de la contraseña.
- Incluir letras mayúsculas.
- Incluir letras minúsculas.
- Incluir números.
- Incluir caracteres especiales.
- Validar que la longitud mínima sea de 8 caracteres.
- Mostrar un mensaje cuando no se seleccione ningún tipo de carácter.
- Guardar las contraseñas generadas durante la ejecución.
- Consultar el historial de contraseñas.
- Finalizar el programa mediante la opción de salida.

## 5. Estructura lógica del programa

El programa utiliza estructuras condicionales y repetitivas para controlar el funcionamiento del sistema.

Entre las estructuras utilizadas se encuentran:

- Condicionales `if`, `elif` y `else`.
- Ciclo `while` para mantener activo el menú principal.
- Ciclos `for` para generar las contraseñas y recorrer el historial.
- Manejo de excepciones mediante `try` y `except`.
- Validación de los datos ingresados por el usuario.

## 6. Organización del código

El proyecto se encuentra organizado en módulos para separar las responsabilidades del programa.

### `programa_principal.py`

Contiene el flujo principal del sistema, el menú, la interacción con el usuario, la validación de opciones y la llamada a las funciones necesarias.

### `funciones.py`

Contiene las funciones encargadas de:

- Generar los caracteres disponibles.
- Generar la contraseña.
- Validar la longitud.
- Guardar el historial.
- Mostrar el historial.
- Mostrar el menú.

Esta organización permite mantener el código de manera clara y estructurada.

## 7. Tecnología utilizada

- Python
- Visual Studio Code
- GitHub
- Módulo `string`
- Módulo `secrets`

El módulo `secrets` se utiliza para realizar la selección aleatoria de caracteres orientada a aplicaciones relacionadas con seguridad.

## 8. Funcionamiento del sistema

El usuario inicia el programa y visualiza un menú con tres opciones:

1. Generar contraseña.
2. Ver historial.
3. Salir.

Al seleccionar la opción de generación, el sistema solicita la longitud de la contraseña y pregunta qué tipos de caracteres desea incluir.

Después de validar la información, el sistema genera la contraseña, la muestra en pantalla y la almacena en el historial de la ejecución.

El usuario puede consultar posteriormente las contraseñas generadas mediante la opción de historial.

## 9. Diagramas del proyecto

El repositorio contiene cinco diagramas desarrollados para representar la funcionalidad y arquitectura del sistema:

1. **Diagrama 1 – Flujo principal:** representa el flujo general del programa y las opciones disponibles.
2. **Diagrama 2 – Generación de contraseña:** representa el proceso de generación de la contraseña.
3. **Diagrama 3 – Selección de caracteres:** representa la selección de mayúsculas, minúsculas, números y caracteres especiales.
4. **Diagrama 4 – Guardar historial:** representa el proceso mediante el cual las contraseñas generadas se almacenan en el historial.
5. **Diagrama 5 – Arquitectura:** representa la organización general del sistema y la relación entre sus componentes.

Los diagramas se encuentran en la carpeta:

`Diagramas_Proyecto_Final/`

## 10. Pruebas de funcionamiento

El sistema fue probado mediante las tres opciones disponibles en el menú:

- Generación de una contraseña.
- Consulta del historial.
- Finalización del programa.

Las pruebas realizadas permitieron comprobar que el sistema genera contraseñas, almacena el resultado en el historial y finaliza correctamente cuando el usuario selecciona la opción correspondiente.

## 11. Estructura principal del repositorio

```text
Generador-Contrase-as-Seguras/
│
├── Codigo/
│   ├── funciones.py
│   └── programa_principal.py
│
├── Diagramas_Proyecto_Final/
│   ├── Diagrama_1_Flujo_Principal.png
│   ├── Diagrama_2_Generar_Contraseña.png
│   ├── Diagrama_3_Seleccion_Caracteres.png
│   ├── Diagrama_4_Guardar_Historial.png
│   └── Diagrama_5_Arquitectura.png
└── README.md
