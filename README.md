# Proyecto_Final-
# Piedra, Papel o Tijera - Aplicación en Python (Patrón MVC)

Este proyecto implementa el clásico juego de "Piedra, Papel o Tijera" utilizando el lenguaje de programación Python y la biblioteca `tkinter` para la interfaz gráfica. El diseño sigue el patrón de arquitectura Modelo-Vista-Controlador (MVC), lo cual permite una separación clara entre la lógica del juego, la interfaz de usuario y el control de flujo.

## Estructura del Proyecto

El proyecto está dividido en los siguientes archivos:

- `modelo.py`: Define las clases que representan el modelo del juego, incluyendo al jugador y la lógica para determinar el resultado de cada ronda.
- `vista.py`: Contiene la implementación de la interfaz gráfica utilizando `tkinter`.
- `controlador.py`: Administra la interacción entre la vista y el modelo. Se encarga de responder a las acciones del usuario y actualizar el estado del juego.
- `main.py`: Punto de entrada principal que inicializa y ejecuta el programa.

## Requisitos

- Python 3.7 o superior

No se requieren bibliotecas adicionales aparte de las que ya vienen incluidas en la instalación estándar de Python.

## Cómo ejecutar el programa

1. Asegúrese de que todos los archivos (`modelo.py`, `vista.py`, `controlador.py`, `main.py`) estén en el mismo directorio.
2. Desde una terminal o consola, diríjase a la carpeta del proyecto.
3. Ejecute el siguiente comando:

```bash
python main.py
