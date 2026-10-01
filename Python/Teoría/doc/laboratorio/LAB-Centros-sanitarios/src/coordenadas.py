from math import sqrt
from collections import namedtuple
import csv
from statistics import mean

Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')

def leer_coordenadas(fichero):
    with open(fichero, encoding = 'utf-8') as f:
        lista = []
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for nombre, localidad, latitud, longitud, estado, num_camas, tiene_acceso_discapacitados, tiene_uci in lector:
            nombre = str(nombre)
            localidad = str(localidad)
            estado = str(estado)
            latitud = float(latitud)
            longitud = float(longitud)         
            num_camas = int(num_camas)
            tiene_acceso_discapacitados = bool(tiene_acceso_discapacitados)
            tiene_uci = bool(tiene_uci)
            tupla = Coordenadas(latitud, longitud)
            lista.append(tupla)
    return lista

def calcular_distancia(Coordenada1: Coordenadas, Coordenada2: Coordenadas):
    return float(sqrt(Coordenada1.longitud - Coordenada2.longitud**2 + Coordenada1.latitud - Coordenada2.latitud**2))

def calcular_media_coordenadas(lista_puntos):

    y=[]
    x=[]

    for p in lista_puntos:
        y.append(p.y)
        x.append(p.x)

    punto_promedio=Coordenadas(mean(y),mean(x))
    return punto_promedio

  
