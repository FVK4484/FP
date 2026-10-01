from random import randint

def juego_adivina_numero(maximo):
    numero_a_adivinar = randint(1, maximo)
    numero_elegido = int(input(f"Elija un número del 1 a {maximo}: "))
    cont = 0
    while numero_elegido != numero_a_adivinar and cont < 3:
        cont += 1
        if numero_a_adivinar < numero_elegido:
            print("El número a adivinar es más pequeño que el introducido.")
        else:
            print("El número a adivinar es más grande que el introducido.")
        print(f'Este es su {cont} intento.')
        numero_elegido = int(input("Elija otro número: "))
    if numero_a_adivinar == numero_elegido:
        res = "Felicidades lo has acertado."
    else:
        res = 'Has llegado a el máximo de intentos.'
    return res

print(juego_adivina_numero(10))
