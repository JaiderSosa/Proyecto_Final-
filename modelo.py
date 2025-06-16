
# modelo.py

import random

# Clase que representa a un jugador
class Jugador:
    def __init__(self, nombre):
        # Asigna el nombre del jugador
        self.nombre = nombre
        # Inicialmente, el jugador no ha hecho una elección
        self.eleccion = None

    def elegir_opcion(self, opcion):
        # Guarda la opción que el jugador elige (Piedra, Papel o Tijera)
        self.eleccion = opcion

# Clase que maneja la lógica del juego
class Juego:
    def __init__(self, jugador):
        # Recibe un objeto jugador como argumento
        self.jugador = jugador
        # Crea un jugador para representar a la computadora
        self.computadora = Jugador("Computadora")
        # Contador de rondas
        self.rondas = 0
        # Puntuación inicial
        self.puntaje_jugador = 0
        self.puntaje_computadora = 0

    def jugar_ronda(self):
        # La computadora elige aleatoriamente una de las tres opciones
        opciones = ["Piedra", "Papel", "Tijera"]
        self.computadora.eleccion = random.choice(opciones)

        # Compara las elecciones de jugador y computadora
        resultado = self.comparar_elecciones(self.jugador.eleccion, self.computadora.eleccion)
        self.rondas += 1  # Se incrementa el número de rondas
        return resultado

    def comparar_elecciones(self, eleccion_jugador, eleccion_computadora):
        # Determina si hay empate
        if eleccion_jugador == eleccion_computadora:
            return "Empate"
        # Casos en los que gana el jugador
        elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijera") or \
             (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra") or \
             (eleccion_jugador == "Tijera" and eleccion_computadora == "Papel"):
            self.puntaje_jugador += 1
            return "Ganaste"
        # Si no empata ni gana, entonces pierde
        else:
            self.puntaje_computadora += 1
            return "Perdiste"

    def mostrar_resultado(self):
        # Devuelve el estado del marcador o si alguien ganó
        if self.puntaje_jugador == 2:
            return f"¡{self.jugador.nombre} gana el juego!"
        elif self.puntaje_computadora == 2:
            return "¡La computadora gana el juego!"
        else:
            return f"Ronda {self.rondas}: {self.jugador.nombre} {self.puntaje_jugador} - Computadora {self.puntaje_computadora}"
