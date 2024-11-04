import random

# Dimensiones de la tabla
TABLERO_DIMENSION = 10
# Definir los barcos con sus tamaños
BARCOS = {
    "barco4": 4,
    "barco3_1": 3,
    "barco3_2": 3,
    "barco2_1": 2,
    "barco2_2": 2,
    "barco2_3": 2,
    "barco1_1": 1,
    "barco1_2": 1,
    "barco1_3": 1,
    "barco1_4": 1
}

# Crear el tablero vacío
tablero = [["-" for _ in range(TABLERO_DIMENSION)] for _ in range(TABLERO_DIMENSION)]

# Función para verificar si se puede colocar el barco en la posición
def es_posicion_valida(fila, columna, longitud, orientacion):
    if orientacion == "H":
        if columna + longitud > TABLERO_DIMENSION:
            return False
        for i in range(longitud):
            if not es_espacio_libre(fila, columna + i):
                return False
    else:  # Vertical
        if fila + longitud > TABLERO_DIMENSION:
            return False
        for i in range(longitud):
            if not es_espacio_libre(fila + i, columna):
                return False
    return True

# Función para verificar que cada celda esté vacía y con espacio alrededor
def es_espacio_libre(fila, columna):
    for i in range(-1, 2):
        for j in range(-1, 2):
            f, c = fila + i, columna + j
            if 0 <= f < TABLERO_DIMENSION and 0 <= c < TABLERO_DIMENSION:
                if tablero[f][c] != "-":
                    return False
    return True

# Función para colocar el barco en la posición
def colocar_barco(fila, columna, longitud, orientacion):
    if orientacion == "H":
        for i in range(longitud):
            tablero[fila][columna + i] = "B"
    else:
        for i in range(longitud):
            tablero[fila + i][columna] = "B"

# Colocar cada barco en el tablero aleatoriamente
for barco, longitud in BARCOS.items():
    colocado = False
    while not colocado:
        fila = random.randint(0, TABLERO_DIMENSION - 1)
        columna = random.randint(0, TABLERO_DIMENSION - 1)
        orientacion = random.choice(["H", "V"])
        if es_posicion_valida(fila, columna, longitud, orientacion):
            colocar_barco(fila, columna, longitud, orientacion)
            colocado = True

# Función para imprimir el tablero
def imprimir_tablero():
    print("        A   B   C   D   E   F   G   H   I   J")
    print("       _ _ _ _ _ _ _ _ _ _")
    for i in range(TABLERO_DIMENSION):
        print(f"    {i + 1:<2} | " + " | ".join(tablero[i]) + " |")
        print("       ¯¯¯ ¯¯¯ ¯¯¯ ¯¯¯ ¯¯¯ ¯¯¯ ¯¯¯ ¯¯¯ ¯¯¯ ¯¯¯")

# Mostrar el tablero
imprimir_tablero()