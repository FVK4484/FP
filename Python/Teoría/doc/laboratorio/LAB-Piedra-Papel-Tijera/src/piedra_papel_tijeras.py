import random

# Ejercicio1
# a) // b)
def ordenador_decide_jugada():
    ''' 
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    '''
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

# c) // Ej2 b)
def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario

# d)
def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijeras" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"

# Ejercicio2
# a)
def jugar():
    print("Hola, bienvenido al juego.")
    ordenador = ordenador_decide_jugada()
    usuario = usuario_decide_jugada()
    print("La elección del ordenador es: ", ordenador)
    ganador = determina_ganador(usuario, ordenador)
    res = "El ganador es: Nadie"
    if ganador == "Ganaste":
        res = "El ganador es: Usuario"
    elif ganador == "Perdiste":
        res = "El ganador es: Ordenador"
    print(res)

# Ejercicio3
# a)
def jugar_torneo():
    cont, cont2 = 0, 0
    print("Hola, bienvenido al juego.")
    while(cont < 3 and cont2 < 3):
        ordenador = ordenador_decide_jugada()
        usuario = usuario_decide_jugada()
        print("La elección del ordenador es: ", ordenador)
        ganador = determina_ganador(usuario, ordenador)
        res = "El ganador es: Nadie"
        if ganador == "Ganaste" and cont == 2:
            res = f"El ganador final con {cont} aciertos es Usuario"
            print(res)
            break
        elif ganador == "Perdiste" and cont2 == 2:
            res = f"El ganador final con {cont2} aciertos es Ordenador"
            print(res)
            break
        elif ganador == "Ganaste":
            cont += 1
            res = f"El ganador es: Usuario. El usuario lleva {cont} puntos."
        elif ganador == "Perdiste":
            cont2 += 1
            res = f"El ganador es: Ordenador. El ordenador lleva {cont2} puntos."
        print(res)

if __name__ == "__main__":
    # jugar()
    jugar_torneo()

# c)
# SI

