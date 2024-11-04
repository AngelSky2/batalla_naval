from tablero import Tablero
import string

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tablero = Tablero()

    def disparar(self, oponente, coordenada):
        """Realiza un disparo en el tablero del oponente con coordenadas tipo 'A1'."""
        # Convertir coordenada al formato índice
        fila = string.ascii_uppercase.index(coordenada[0].upper())
        columna = int(coordenada[1:]) - 1

        # Realizar disparo y mostrar el resultado
        resultado = oponente.tablero.recibir_disparo(fila, columna)
        print(f"{self.nombre} dispara a {coordenada}: {resultado}")
        return resultado
