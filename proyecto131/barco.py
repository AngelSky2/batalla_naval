# barco.py
class Barco:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.posiciones = []  # Lista de tuplas (x, y) para las posiciones del barco
        self.hundido = False

    def asignar_posiciones(self, posiciones):
        """Asigna las posiciones en el tablero para este barco."""
        self.posiciones = posiciones

    def esta_hundido(self):
        """Determina si el barco está completamente hundido."""
        return all(pos == (-1, -1) for pos in self.posiciones)

    def recibir_disparo(self, x, y):
        """Procesa un disparo en las coordenadas (x, y). Marca como dañado si el disparo impacta."""
        if (x, y) in self.posiciones:
            # Marcamos la posición como dañada
            self.posiciones[self.posiciones.index((x, y))] = (-1, -1)
            # Verificamos si está completamente hundido
            if self.esta_hundido():
                self.hundido = True
            return True  # Indica que fue un impacto
        return False  # Indica que fue agua
