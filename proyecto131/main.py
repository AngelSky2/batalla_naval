# main.py
from jugador import Jugador
from barco import Barco
import random
import string

def colocar_barcos_aleatorios(jugador):
    """Coloca barcos aleatorios en el tablero de un jugador."""
    tamaños = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for tamaño in tamaños:
        colocado = False
        while not colocado:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            horizontal = random.choice([True, False])
            barco = Barco(tamaño)
            colocado = jugador.tablero.posicionar_barco(barco, x, y, horizontal)

def juego_dos_jugadores(jugador1, jugador2):
    """Juego entre dos jugadores con ingreso de coordenadas, permite seguir disparando al acertar."""
    # Muestra los tableros iniciales con barcos
    print("Tablero inicial del Jugador 1 (con barcos):")
    jugador1.tablero.mostrar_tablero_con_barcos()
    print("\nTablero inicial del Jugador 2 (con barcos):")
    jugador2.tablero.mostrar_tablero_con_barcos()

    # Empieza el juego ocultando los barcos después del primer turno
    turno = 1
    while True:
        jugador_actual = jugador1 if turno % 2 == 1 else jugador2
        oponente = jugador2 if turno % 2 == 1 else jugador1
        acierto = True

        # Mientras el jugador acierte, continúa disparando
        while acierto:
            print(f"\n{jugador_actual.nombre}, tu tablero:")
            jugador_actual.tablero.mostrar_tablero_oculto()
            print(f"\nTablero oculto del oponente:")
            oponente.tablero.mostrar_tablero_oculto()

            coordenada = input(f"{jugador_actual.nombre}, ingresa la coordenada para disparar (ej. A1): ")
            acierto = jugador_actual.disparar(oponente, coordenada)
            oponente.tablero.mostrar_tablero_oculto()

            if acierto:
                print(f"¡{jugador_actual.nombre} ha acertado! Puede disparar de nuevo.")
            else:
                print(f"{jugador_actual.nombre} ha fallado. Turno del siguiente jugador.")

        turno += 1

def juego_contra_ia(jugador, ia):
    """Juego contra la IA, que responde con coordenadas aleatorias y permite al jugador seguir disparando al acertar."""
    # Muestra el tablero inicial con barcos del jugador
    print("Tablero inicial del Jugador (con barcos):")
    jugador.tablero.mostrar_tablero_con_barcos()

    while True:
        # Turno del Jugador
        acierto = True
        while acierto:
            print(f"\n{jugador.nombre}, tu tablero:")
            jugador.tablero.mostrar_tablero_oculto()
            print("\nTablero oculto de la IA:")
            ia.tablero.mostrar_tablero_oculto()

            coordenada = input(f"{jugador.nombre}, ingresa la coordenada para disparar (ej. A1): ")
            acierto = jugador.disparar(ia, coordenada)
            ia.tablero.mostrar_tablero_oculto()

            if acierto:
                print(f"¡{jugador.nombre} ha acertado! Puede disparar de nuevo.")
            else:
                print(f"{jugador.nombre} ha fallado. Turno de la IA.")

        # Turno de la IA con disparo aleatorio
        acierto = True
        while acierto:
            fila = random.choice(string.ascii_uppercase[:10])
            columna = random.randint(1, 10)
            coordenada_ia = f"{fila}{columna}"
            print(f"IA dispara a {coordenada_ia}")
            acierto = ia.disparar(jugador, coordenada_ia)

            jugador.tablero.mostrar_tablero_oculto()
            if acierto:
                print("¡La IA ha acertado y puede disparar de nuevo!")
            else:
                print("La IA ha fallado. Turno del jugador.")

def main():
    print("Bienvenido a Batalla Naval")
    print("1. Juego de 2 jugadores")
    print("2. Juego contra la IA")
    opcion = input("Elige una opción: ")

    jugador1 = Jugador("Jugador 1")
    jugador2 = Jugador("Jugador 2" if opcion == "1" else "IA")

    # Colocar barcos aleatorios
    colocar_barcos_aleatorios(jugador1)
    colocar_barcos_aleatorios(jugador2)

    if opcion == "1":
        juego_dos_jugadores(jugador1, jugador2)
    else:
        juego_contra_ia(jugador1, jugador2)

if __name__ == "__main__":
    main()
