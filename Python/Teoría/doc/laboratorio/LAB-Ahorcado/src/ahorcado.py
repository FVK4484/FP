import random

# Ej1
# a)
def cargar_palabras(ruta):
    '''
    Recibe la ruta de un fichero de texto que contiene una palabra por línea y devuelve
    dichas palabras en una lista.
    '''
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip()) # strip() elimina los espacios en blanco y saltos de línea al principio y al final
        return res

# b)
def elegir_palabra(palabras):
    '''
    Elige la palabra a adivinar:
    - Selecciona una palabra aleatoria de la lista 'palabras'
    - Devuelve la palabra seleccionada
    Ayuda: 
    - La función 'random.choice' del paquete 'random' recibe una lista de opciones y 
      devuelve una de ellas seleccionada aleatoriamente.
    '''
    palabra_aleatoria = random.choice(palabras)

    return palabra_aleatoria

# c)
def enmascarar_palabra(palabra, letras_probadas):
    '''
    Enmascarar la palabra:
    - Inicializar una lista vacía. 
    - Recorrer cada letra de la palabra, añadiendola a la lista 
      si forma parte de las letras_probadas, o añadiendo un '_' en caso contrario. 
    - Devuelve una cadena concatenando los elementos de la lista (ver 'Ayuda')
    Ayuda: 
    - Utilice el método join de las cadenas. Observe el siguiente ejemplo:
        ' '.join(['a','b','c']) # Devuelve "a b c"
    '''
    lista=[]
    for letra in palabra:
        if letra in letras_probadas:
            lista.append(letra)
        else:
            lista.append('_')
    return ''.join(lista)

# d)
def pedir_letra(letras_probadas):
    '''
    Pedir la siguiente letra:
    - Pedirle al usuario que escriba la siguiente letra por teclado
    - Comprobar si la letra indicada ya se había propuesto antes y pedir otra si es así
    - Considerar las letras en minúsculas aunque el usuario las escriba en mayúsculas
    - Devolver la letra
    Ayuda:
    - La función 'input' permite leer una cadena de texto desde la entrada estándar
    - El método 'lower' aplicado a una cadena devuelve una copia de la cadena en minúsculas
    '''
   
    letra_introducida = input("Adivina una letra: ")
    letra_minuscula = letra_introducida.lower()
    for letra_minuscula in letra_introducida:
        if letra_minuscula in letras_probadas:
            input("Ya has probado con esa letra. Intenta con otra: ")
        else:
            return letra_minuscula
    
# e)
def comprobar_letra(palabra_secreta, letra):
    '''
    Comprobar letra:
    - Comprobar si la letra está en la palabra secreta o no
    - Mostrar el mensaje correspondiente informando al usuario
    - Devolver True si estaba y False si no
    '''
    if letra in palabra_secreta:
        print("¡Bien hecho! Esa letra está en la palabra.")
        return True
    else: 
        print("Lo siento, esa letra no está en la palabra.")
    
# f)
def comprobar_palabra_completa(palabra_secreta, letras_probadas):
    if letras_probadas == set(palabra_secreta):
        return True

# g)
def ejecutar_turno(palabra_secreta, letras_probadas):
    print(f"Palabra: {enmascarar_palabra(palabra_secreta, letras_probadas)}")
    letra_pedida = input("Adivina una letra: ")
    set(letras_probadas).add(letra_pedida)
    if letra_pedida in letras_probadas:
        return False
    elif letra_pedida in palabra_secreta:
        return True
    else:
        return False
    
# Ej2
# a)
def jugar(max_intentos, palabras):
    print("=========================================")
    print("¡Bienvenido al juego del Ahorcado!")
    print("=========================================")
    palabra_secreta = random.choice(palabras) 
    letras_probadas = set()
    intentos_fallidos = 0
    # Ejecutar los turnos de juego
    while True:
        # Mostrar estado actual del juego
        print(f"Palabra: {enmascarar_palabra(palabra_secreta, letras_probadas)}")
        intentos_restantes = max_intentos - intentos_fallidos
        print(f"Te quedan {intentos_restantes} intentos.")
        print(f"Letras probadas: {', '.join(sorted(letras_probadas))}")

        # Pedir una nueva letra
        letra = pedir_letra(letras_probadas)
        letras_probadas.add(letra)

        # Averiguar si ha habido acierto o fallo
        if letra in palabra_secreta:
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
        else:
            print(f"¡Oh, no! La letra '{letra}' no está en la palabra.")
            intentos_fallidos += 1

        # Comprobar si se ha completado la palabra (condición de victoria)
        if comprobar_palabra_completa(palabra_secreta, letras_probadas):
            print("\n" + ("*"*30))
            print(f"¡Felicidades! ¡Has adivinado la palabra: '{palabra_secreta}'!")
            print("*"*30)
            break  # Termina el juego

        # Comprobar si se ha superado el número de fallos máximo (condición de derrota)
        if intentos_fallidos >= max_intentos:
            print("\n" + ("="*30))
            print("¡Has perdido! Te has quedado sin intentos.")
            print(f"La palabra secreta era: '{palabra_secreta}'.")
            print("="*30)
            break # Termina el juego
# Iniciar el juego
if __name__ == "__main__":
    palabras = cargar_palabras("data/palabras_ahorcado.txt")
    jugar(6, palabras)
