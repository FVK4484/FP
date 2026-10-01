from calificaciones import*
from collections import namedtuple

# e)
def solicita_notas():
    nombre = input("Digame su nombre: ")
    n1 = input(f"Encantado {nombre}, a continuación inserte sus notas de los 4 cuestionarios de teoría y las de los 2 exámenes prácticos. Cuestionario 1: ")
    n2 = input("Cuestionario 2: ")
    n3 = input("Cuestionario 3: ")
    n4 = input("Cuestionario 4: ")
    p1 = input("Práctica 1: ")
    p2 = input("Práctica 2: ")
    tupla = (nombre, [n1, n2, n3, n4], [p1, p2])
    return tupla

def mostrar_notas(nombre, tupla, tupla2):
    nota1 = nota_teoria(tupla[0], tupla[1])
    nota2 = nota_cuatrimestre(tupla[0], tupla[1], tupla2[0])
    nota3 = nota_teoria(tupla[2], tupla[3])
    nota4 = nota_cuatrimestre(tupla[2], tupla[3], tupla2[1])
    practica1 = tupla2[0]
    practica2 = tupla2[1]
    continua = nota_continua((tupla[0], tupla[1], tupla[2], tupla[3]), (tupla2[0], tupla2[1]))

    print(f"{nombre}. Tus notas del primer cuatrimestre son: Teoria = {nota1}, Práctica = {practica1}, cuatrimestre: {nota2}")
    print(f"Tus notas del segundo cuatrimestre son: Teoria = {nota3}, Práctica = {practica2}, cuatrimestre: {nota4}")
    print(f"Tu nota final de la asignatura es: {continua}")