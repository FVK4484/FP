from collections import namedtuple
Persona = namedtuple("Persona", "nombre, edad")

# def lee_personas(n):
#   personas_leidas = []
#   for persona in range(n):
#     nombre = input(f"Introduce el nombre de la persona {persona + 1}: ")
#     while True:
#       try:
#         edad = int(input(f"Introduce la edad de {nombre}: "))
#         break 
#       except ValueError:
#         print("Por favor, introduce un número entero válido para la edad.")

#     personas_leidas.append(Persona(nombre, edad))
#   return personas_leidas

# n = 3
# personas = lee_personas(n)
# print(personas)

personas = [Persona(nombre='Aitor', edad=19), Persona(nombre='Jesús', edad=18), Persona(nombre='Laura', edad=15)]

def edad_media(personas):
    suma_edad = 0
    for persona in personas:
        suma_edad += persona.edad
    return suma_edad / len(personas)

print(edad_media(personas))

def mayores_18(personas):
   return sorted(persona.nombre for persona in personas if persona.edad >=18)

print(mayores_18(personas))

def edades_distintas(personas):
    return sorted(set(persona.edad for persona in personas))

print(edades_distintas(personas))

def persona_mas_joven(personas):
    return sorted(persona.nombre for persona in personas if min(persona.edad for persona in personas) == persona.edad)

print(persona_mas_joven(personas))