from ejercicio1 import*
from ejercicio2 import*

def imprime_estados_nutricionales(personas):
    cont = 0
    for persona in personas:
        cont += 1
        imc = calcula_imc(persona[0], persona[1])
        estado_nutricional = calcula_estado_nutricional(persona[0], persona[1])
        print(f'El IMC de la persona {cont} es {imc}, y su estado nutricional es {estado_nutricional}.')
    
personas = [
    (60.0, 1.6),
    (75.4, 1.75),
    (87.9, 1.69),
    (45.1, 1.65)
]
imprime_estados_nutricionales(personas)