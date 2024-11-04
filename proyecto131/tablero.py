# tablero.py
from barco import Barco
import random
import string

class Tablero:
    TAMANIO = 10  # Tamaño del tablero 10x10

    def __init__(self):
        self.tablero = [[" " for _ in range(self.TAMANIO)] for _ in range(self.TAMANIO)]
        self.barcos = []

    def posicionar_barco(self, barco, x, y, horizontal):
        """Posiciona un barco en el tablero verificando espacio y distancia de otras embarcaciones."""
        tamaño = barco.tamaño
        posiciones = []

        # Verifica si el barco cabe en la posición
        if horizontal:
            if x + tamaño > self.TAMANIO: return False
            posiciones = [(x + i, y) for i in range(tamaño)]
        else:
            if y + tamaño > self.TAMANIO: return False
            posiciones = [(x, y + i) for i in range(tamaño)]

        # Verifica que las posiciones estén libres y con la distancia de 1 casilla alrededor
        for (px, py) in posiciones:
            if self.tablero[px][py] != " " or not self.espacio_entre_barcos(px, py):
                return False

        # Coloca el barco y actualiza el tablero
        for (px, py) in posiciones:
            self.tablero[px][py] = "B"  # Representa parte del barco
        barco.asignar_posiciones(posiciones)
        self.barcos.append(barco)
        return True

    def espacio_entre_barcos(self, x, y):
        """Verifica que haya espacio libre alrededor de la posición (x, y)."""
        for i in range(max(0, x - 1), min(self.TAMANIO, x + 2)):
            for j in range(max(0, y - 1), min(self.TAMANIO, y + 2)):
                if self.tablero[i][j] == "B":
                    return False
        return True

    def recibir_disparo(self, x, y):
        """Recibe un disparo y devuelve el resultado (Impacto o Agua)."""
        if self.tablero[x][y] == "B":
            self.tablero[x][y] = "X"  # Marcamos como impacto
            for barco in self.barcos:
                if barco.recibir_disparo(x, y):
                    return "Impacto"
            return "Impacto"
        elif self.tablero[x][y] == " ":
            self.tablero[x][y] = "O"  # Marcamos como agua
            return "Agua"
        return "Ya disparado"  # Ya se disparó a esta posición

    def mostrar_tablero_con_barcos(self):
        """Muestra el tablero completo incluyendo los barcos al inicio."""
        print("   | " + " | ".join(str(i) for i in range(1, self.TAMANIO + 1)) + " |")
        print("----" + "----" * self.TAMANIO)
        for idx, fila in enumerate(self.tablero):
            letra_fila = string.ascii_uppercase[idx]
            print(f" {letra_fila} | " + " | ".join(fila) + " |")

    def mostrar_tablero_oculto(self):
        """Muestra el tablero sin barcos, revelando solo las coordenadas marcadas."""
        print("   | " + " | ".join(str(i) for i in range(1, self.TAMANIO + 1)) + " |")
        print("----" + "----" * self.TAMANIO)
        for idx, fila in enumerate(self.tablero):
            letra_fila = string.ascii_uppercase[idx]
            fila_oculta = [" " if celda == "B" else celda for celda in fila]  # Oculta barcos
            print(f" {letra_fila} | " + " | ".join(fila_oculta) + " |")
