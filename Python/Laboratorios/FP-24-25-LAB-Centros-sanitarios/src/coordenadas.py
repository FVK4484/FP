from collections import namedtuple
import math

Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')

def calcular_distancia (c1, c2):
    return math.sqrt( (c2.latitud - c1.latitud)**2 + 
                     (c2.longitud - c1.longitud)**2 )

def calcular_media_coordenadas (coordenadas):
    suma_latitudes = 0
    suma_longitudes = 0
    for c in coordenadas:
        suma_latitudes += c.latitudes
        suma_longitudes += c.longitudes
    media_latitudes = suma_latitudes / len(coordenadas)
    media_longitudes = suma_longitudes / len(coordenadas)
    return Coordenadas(media_latitudes, media_longitudes)