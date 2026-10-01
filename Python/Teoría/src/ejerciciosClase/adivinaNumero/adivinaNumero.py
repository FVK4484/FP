import random

def adivinaNumero():
      numero = random.randint(1,10)
      max_intentos = 3
      cont = 0
      while cont in range(max_intentos):
        numero_escrito = int(input("Escriba un numero: "))
        if numero == numero_escrito:
            print("Has ganado")
        elif cont == 3:
            print(numero)
            break
        else:
            print("Has perdido")
            cont = cont + 1
        
                 

                 