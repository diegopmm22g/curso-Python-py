"""
¡Piedra, papel o tijeras!

Juego de piedra, papel o tijeras hecho en Python.
"""

import random


def eleccion_computadora():
    """Obtiene una opción aleatoria para que la computadora la use."""

    computadora = random.choice(opciones)
    return computadora


def eleccion_usuario():
    """Obtiene la opción que usará el jugador."""

    usuario = str(input("Selecciona tu jugada para esta ronda: piedra, papel o tijeras.\n"))
    usuario = usuario.lower()
    if usuario in opciones:
        return usuario
    else:
        raise Exception("Tu elección no es válida. Revisa errores de escritura e inténtalo de nuevo.")


def jugar():
    """Inicia y maneja el juego de principio a fin."""

    rondas = 3
    victorias_usuario = 0
    victorias_computadora = 0

    print("*" * 15)
    print("El juego comenzará ahora.")
    print("*" * 15)
    
    while True:
        computadora = eleccion_computadora()
        usuario = eleccion_usuario()
        print(f"{usuario} vs {computadora}, ")
            
        if usuario == computadora:
            rondas -= 1
            print(f"""
            ¡Empate!
            Ambos eligieron {usuario}
            Quedan {rondas} rondas.
            """)

        if (usuario == "tijeras" and computadora == "papel") or \
           (usuario == "piedra" and computadora == "tijeras") or \
           (usuario == "papel" and computadora == "piedra"):
        
            rondas -= 1
            victorias_usuario += 1

            print(f"""
            ¡Ganaste esta ronda!
            {usuario} vence a {computadora}!
            Quedan {rondas} rondas.
            """)

        if (computadora == "tijeras" and usuario == "papel") or \
           (computadora == "piedra" and usuario == "tijeras") or \
           (computadora == "papel" and usuario == "piedra"):
    
            rondas -= 1
            victorias_computadora += 1
            
            print(f"""
            Perdiste esta ronda.
            {computadora} vence a {usuario}!
            Quedan {rondas} rondas.
            """)

        if rondas <= 0:
            if victorias_usuario == victorias_computadora:
                print("Empate, terminaron el juego con la misma cantidad de puntos.")
                break
            if victorias_computadora > victorias_usuario:
                print(f"Juego terminado. La computadora gana con {victorias_computadora} puntos.")
                break
            if victorias_computadora < victorias_usuario:
                print(f"Juego terminado. ¡Tú ganas con {victorias_usuario} puntos!")
                break


if __name__ == "__main__":
    # Opciones globales del juego.
    opciones = ("piedra", "papel", "tijeras")
    jugar()
