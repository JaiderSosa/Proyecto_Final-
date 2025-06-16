
# vista.py

import tkinter as tk
from tkinter import messagebox

# Clase que representa la interfaz gráfica del juego
class VistaJuego:
    def __init__(self, controlador):
        # Guarda una referencia al controlador
        self.controlador = controlador

        # Crea la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Piedra, Papel o Tijera")

        # Variables que se mostrarán en pantalla
        self.resultado = tk.StringVar()
        self.marcador = tk.StringVar()

        # Botones para elegir cada opción
        self.btn_piedra = tk.Button(self.ventana, text="Piedra", command=lambda: self.controlador.jugar("Piedra"))
        self.btn_papel = tk.Button(self.ventana, text="Papel", command=lambda: self.controlador.jugar("Papel"))
        self.btn_tijera = tk.Button(self.ventana, text="Tijera", command=lambda: self.controlador.jugar("Tijera"))

        # Etiquetas que muestran los resultados
        self.lbl_resultado = tk.Label(self.ventana, textvariable=self.resultado)
        self.lbl_marcador = tk.Label(self.ventana, textvariable=self.marcador)

        # Organización de los elementos en la ventana
        self.btn_piedra.pack()
        self.btn_papel.pack()
        self.btn_tijera.pack()
        self.lbl_resultado.pack()
        self.lbl_marcador.pack()

    def iniciar(self):
        # Inicia el bucle principal de la interfaz
        self.ventana.mainloop()

    def actualizar_resultado(self, resultado_ronda, marcador):
        # Actualiza el texto que muestra el resultado de la ronda y el marcador
        self.resultado.set(resultado_ronda)
        self.marcador.set(marcador)

    def terminar_juego(self, mensaje):
        # Muestra un mensaje cuando alguien gana el juego y cierra la ventana
        messagebox.showinfo("Juego Terminado", mensaje)
        self.ventana.quit()
