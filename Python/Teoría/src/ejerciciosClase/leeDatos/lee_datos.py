import csv
from collections import namedtuple

Persona = namedtuple('Persona', 'nombre, edad, ciudad')

def lee_datos(fichero):
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, edad, ciudad in lector:
            edad = int(edad)
            tupla = Persona(nombre, edad, ciudad)
            lista.append(tupla)
        return lista