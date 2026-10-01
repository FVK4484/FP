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

def filtrar_por_genero(frecuencias, g):
    filtrados = []
    for f in frecuencias:
        if f.genero == g:
            filtrados.append(f)
    return filtrados

def calcular_nombres (frecuencias, genero):
    nombres = set()
    for f in frecuencias:
        if genero == None or f.genero == genero:
            nombres.add(f.nombre)
    return sorted(nombres)

def calcular_top_nombres_de_año (frecuencias, año, n, genero):
    res = []
    for f in frecuencias:
        if f.año == año and f.genero == genero:
            tupla = (f.nombre, f.frecuencia)
            res.append(tupla)
    return sorted(res, key = lambda t:t[1], reverse = True)[:n]