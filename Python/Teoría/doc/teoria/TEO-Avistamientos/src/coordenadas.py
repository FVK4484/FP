## Definición de tipos
# Creación de una tupla con nombre para las coordenadas
from collections import namedtuple
from math import radians, sin, cos, asin, sqrt

Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')

def a_radianes(coordenadas):
    '''Convierte unas coordenadas en grados a radianes

    @param coordenadas: Coordenadas que se quieren convertir a radianes
    @type coordenadas: Coordenadas(float, float)
    @return: Las coordenadas convertidas a radianes
    @rtype: Coordenadas(float, float)
    
    Ayuda:
    Usa la función radians para convertir a radianes. Por ejemplo,
    latitud_radianes = radians(latitud)
    '''
    latitud_radianes = radians(coordenadas[0])
    longitud_radianes = radians(coordenadas[1])
    return (latitud_radianes, longitud_radianes)

def distancia_harvesine(coordenadas1, coordenadas2):
    '''Devuelve la distancia de harvesine entre dos coordenadas

    @param coordenadas1: Coordenadas del primer punto
    @type coordenadas1: Coordenadas(float, float)
    @param coordenadas2: Coordenadas del segundo punto
    @type coordenadas2: Coordenadas(float, float)
    @return: La distancia harvesine entre las dos coordenadas dadas como parámetro
    @rtype: float
    '''
    lat = coordenadas2[0] - coordenadas1[0]
    lon = coordenadas2[1] - coordenadas1[1]
    R = 6371
    a = sin(lat/2)**2 + cos(coordenadas1[0]) * cos(coordenadas2[0]) * sin(lon/2)**2
    d = 2 * R * asin(sqrt(a))
    return d

def redondear(coordenadas):
    '''Devuelve unas coordenadas cuya latitud y longitud son 
    el redondeo de la latitud y la longitud de las coordenadas originales

    @param coordenadas: Coordenadas que se quieren convertir a radianes
    @type coordenadas: Coordenadas(float, float)
    @return: Las coordenadas redondeadas
    @rtype: Coordenadas(float, float)

    Ayuda:
    Usa la función round para redondear. Por ejemplo,
    latitud_redondeada = round(latitud)
    '''
    pass