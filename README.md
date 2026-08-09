## Generador de Contraseñas Seguras

## Descripción

Este proyecto consiste en el desarrollo de un programa en Python para generar contraseñas seguras de manera aleatoria.

El usuario puede seleccionar la longitud de la contraseña y los tipos de caracteres que desea incluir:

- Letras mayúsculas
- Letras minúsculas
- Números
- Caracteres especiales

El programa valida los datos ingresados y genera una contraseña utilizando los caracteres seleccionados.

## Investigación y fundamento

Para el desarrollo del Generador de Contraseñas Seguras se investigó el uso de mecanismos de generación aleatoria aplicados a contraseñas. La documentación oficial de Python establece que el módulo `secrets` permite generar valores aleatorios criptográficamente fuertes y apropiados para aplicaciones relacionadas con seguridad, como la generación de contraseñas.

A partir de esta información, se decidió utilizar el módulo `secrets` en el programa. Esta decisión permite realizar la selección aleatoria de caracteres utilizando una herramienta de Python destinada a aplicaciones relacionadas con seguridad.

Además, el programa permite seleccionar diferentes tipos de caracteres y establecer la longitud de la contraseña. Esta decisión busca proporcionar flexibilidad al usuario, manteniendo validaciones que evitan configuraciones inválidas.

### Fuente consultada

Python Software Foundation. *secrets — Generate secure random numbers for managing secrets*. Documentación oficial de Python.

https://docs.python.org/3/library/secrets.html

## Posición del estudiante

La posición adoptada en este proyecto es que un generador de contraseñas debe permitir al usuario configurar las características de la contraseña, pero debe mantener validaciones que garanticen el funcionamiento correcto del proceso.

Por esta razón, el programa permite seleccionar la longitud y los tipos de caracteres que se desean utilizar, pero no permite continuar cuando no se ha seleccionado ningún tipo de carácter.

Esta decisión busca equilibrar la personalización proporcionada al usuario con las condiciones necesarias para que el generador produzca una contraseña válida.

## Objetivo

Diseñar e implementar un generador de contraseñas seguras aplicando los conceptos de lógica de programación, diagramas de flujo y estructuras de control.

## Funcionalidades

- Solicitar la longitud de la contraseña.
- Validar que la longitud sea un número válido y mayor que cero.
- Seleccionar los tipos de caracteres.
- Validar que al menos un tipo de carácter sea seleccionado.
- Generar una contraseña aleatoria.
- Mostrar la contraseña generada.
- Permitir generar otra contraseña.
- Finalizar el programa cuando el usuario lo indique.

## Conclusiones y logros

El desarrollo del Generador de Contraseñas Seguras permitió transformar los procesos representados inicialmente mediante diagramas de flujo en un programa funcional desarrollado en Python.

Durante las pruebas se comprobó que el programa genera correctamente una contraseña cuando los datos ingresados son válidos. También se verificó que una longitud de `0` es rechazada mediante una validación y que el programa no permite continuar cuando no se selecciona ningún tipo de carácter.

Además, se comprobó que el usuario puede generar una nueva contraseña sin reiniciar el programa y puede finalizar el proceso cuando lo desea.

Los resultados obtenidos muestran que las principales decisiones planteadas durante el diseño fueron implementadas en el código y comprobadas mediante diferentes casos de prueba.

## Competencias adquiridas

Durante el desarrollo del proyecto se aplicaron conocimientos de lógica de programación mediante el uso de variables, estructuras condicionales, estructuras repetitivas, validaciones y generación aleatoria.

También se aplicó un proceso de desarrollo en el que primero se representaron las funcionalidades mediante diagramas de flujo y posteriormente se transformaron esas representaciones en código Python.

El funcionamiento del programa fue evaluado mediante diferentes casos de prueba, incluyendo datos válidos y situaciones de error. Esto permitió comprobar el comportamiento del programa y verificar que las validaciones respondieran correctamente a las entradas del usuario.

## Perspectivas y decisiones alternativas

Durante el diseño del programa se consideró la relación entre la personalización de la contraseña y la necesidad de mantener condiciones de funcionamiento válidas.

Una alternativa sería seleccionar automáticamente todos los tipos de caracteres para aumentar la variedad de la contraseña. Sin embargo, esta opción reduciría la capacidad del usuario para configurar el resultado.

La solución implementada permite que el usuario seleccione los tipos de caracteres que desea utilizar, pero establece como condición que al menos un tipo debe ser seleccionado.

Esta decisión busca mantener un equilibrio entre la libertad de configuración del usuario y las validaciones necesarias para generar una contraseña válida.

## Pensamiento innovador

La solución desarrollada integra en un mismo proceso la selección de longitud, la selección de tipos de caracteres, la validación de los datos y la generación aleatoria de la contraseña.

Una característica de la solución es que el usuario puede configurar la contraseña sin modificar el código fuente. Además, el programa permite repetir el proceso para generar nuevas contraseñas sin necesidad de reiniciar la aplicación.

Estas decisiones permiten transformar el proceso de generación de caracteres en una herramienta interactiva y sencilla de utilizar.

## Relación entre los diagramas y el código

Los diagramas de flujo fueron utilizados como representación previa de la lógica del programa. Posteriormente, cada proceso fue transformado en instrucciones de Python.

| **Proceso representado** | **Implementación en el programa** |
|---|---|
| Solicitar la longitud | Entrada de datos mediante `input()` |
| Validar la longitud | Estructuras condicionales |
| Seleccionar tipos de caracteres | Condicionales para cada opción |
| Crear el conjunto de caracteres | Unión de los caracteres seleccionados |
| Generar la contraseña | Selección aleatoria mediante `secrets` |
| Alcanzar la longitud solicitada | Estructura repetitiva `while` |
| Generar otra contraseña | Repetición del proceso mediante un ciclo |
| Finalizar el programa | Condición de salida |

De esta manera, los diagramas de flujo funcionan como una representación visual de la lógica utilizada posteriormente para desarrollar el código.

El proceso realizado fue:

**Diagramas de flujo → lógica del programa → código Python → pruebas de funcionamiento.**

## Tecnología utilizada

- Python
- Visual Studio Code
- GitHub
  
## Estructura del proyecto

```text
Generador-Contrase-as-Seguras/
│
├── Codigo/
│   └── generador_contraseñas.py
│
├── Diagramas/
│   ├── Diagrama_Flujo_1.png
│   ├── Diagrama_Flujo_2.png
│   ├── Diagrama_Flujo_3.png
│   └── README.md
│
├── Documentacion/
│   └── Manual.pdf
│
└── README.md
