import random

def ordenador_decide_jugada():
    ''' 
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    '''
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res

def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario

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
    
def jugar():
    #Muestre mensaje de bienvenida
    print('Bienvenido al juego Piedra, Papel o Tijera')

    #Haga que el ordenador decida su jugada
    eleccion_ordenador = ordenador_decide_jugada()

    #Haga que el jugador decida su jugada
    eleccion_usuario = usuario_decide_jugada()

    #Muestre un mensaje indicando la elección del ordenador
    print('El ordenador ha elegido', eleccion_ordenador)

    #Determine quién es el ganador
    resultado = determina_ganador(eleccion_usuario, eleccion_ordenador)

    #Muestre un mensjae con el resultado de la ronda
    print('El resultado es:', resultado)
    
if __name__ == "__main__":
    jugar()