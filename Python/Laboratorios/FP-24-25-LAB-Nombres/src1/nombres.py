from collections import namedtuple
import csv

lista_frecuencias_nombre = []
FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año, nombre, frecuencia, genero')

def lee_frecuencias_nombres(fichero):
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector) 
        datos = []
        for año, nombre, frecuencia, genero in lector:
            año = int(año)
            frecuencia = int(frecuencia)
            tupla = FrecuenciaNombre(
                año, nombre, frecuencia, genero
            )
            datos.append(tupla)
    return datos
