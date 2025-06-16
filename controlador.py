
# controlador.py

from modelo import Jugador, Juego
from vista import VistaJuego

# Clase que conecta la vista con el modelo
class Controlador:
    def __init__(self):
        # Se crea el jugador y el juego
        self.jugador = Jugador("Jugador")
        self.juego = Juego(self.jugador)
        # Se instancia la vista y se le pasa el controlador
        self.vista = VistaJuego(self)

    def jugar(self, opcion):
        # El jugador elige una opción
        self.jugador.elegir_opcion(opcion)
        # Se juega una ronda
        resultado_ronda = self.juego.jugar_ronda()
        marcador = self.juego.mostrar_resultado()

        # Se actualiza la interfaz con el resultado de la ronda
        self.vista.actualizar_resultado(resultado_ronda, marcador)

        # Si alguien gana, termina el juego
        if self.juego.puntaje_jugador == 2 or self.juego.puntaje_computadora == 2:
            self.vista.terminar_juego(marcador)

    def iniciar_juego(self):
        # Inicia la interfaz gráfica
        self.vista.iniciar()
