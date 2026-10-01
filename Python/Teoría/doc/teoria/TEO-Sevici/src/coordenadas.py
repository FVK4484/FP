# Ejercicio1.1
from collections import namedtuple
from math import sqrt
from statistics import mean

Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')

# Ejercicio2.2
def calcula_distancia(coordenadas1, coordenadas2):
    return sqrt((coordenadas2[0] - coordenadas1[0]) ** 2 + (coordenadas2[1] - coordenadas1[1]) ** 2)

# Ejercicio3
def media_coordenadas(estaciones): # Cambiado 'coordenadas' a 'estaciones' para ser más consistente
    '''Devuelve una coordenada cuya latitud es la media de las latitudes y
    cuya longitud es la media de las longitudes.
    ENTRADA
        :param estaciones: lista de estaciones de las que se obtendrán las coordenadas
        :ptype estaciones: [Estacion(str, int, int, int, Coordenadas(float, float))]
    SALIDA
        :return: Una coordenada cuya longitud es la media de las longitudes, y la 
             latitud la media de las latitudes
        :rtype: Coordenadas(float, float)
    '''
    if not estaciones: # Manejar el caso de una lista vacía
        return Coordenadas(0.0, 0.0)

    latitudes = [estacion.ubicacion.latitud for estacion in estaciones]
    longitudes = [estacion.ubicacion.longitud for estacion in estaciones]
    
    # Usando statistics.mean para mayor claridad
    media_latitud = mean(latitudes)
    media_longitud = mean(longitudes)

    return Coordenadas(media_latitud, media_longitud)