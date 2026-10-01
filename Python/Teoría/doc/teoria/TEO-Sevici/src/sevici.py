# Ejercicio1
import csv
from collections import namedtuple
from coordenadas import*
from statistics import mean


# Ejercicio1.1
Estacion = namedtuple('Estacion', 'nombre, bornetas, bornetas_vacias, bicis_disponibles, ubicacion')

# Ejercicio1.2
def lee_estaciones(fichero):
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, bornetas, bornetas_vacias, bicis_disponibles, latitud, longitud in lector:
            bornetas = int(bornetas)
            bornetas_vacias = int(bornetas_vacias)
            bicis_disponibles = int(bicis_disponibles)
            longitud = float(longitud)
            latitud = float(latitud)
            ubicacion = Coordenadas(latitud, longitud)
            tupla = Estacion(nombre, bornetas, bornetas_vacias, bicis_disponibles, ubicacion)
            lista.append(tupla)
    return lista

# Ejercicio2
# Ejercicio2.1
def estaciones_bicis_libres(estaciones, k):
    return sorted((estacion.bicis_disponibles, estacion.nombre) 
                   for estacion in estaciones
                   if estacion.bicis_disponibles >= k)

# Ejercicio2.2
def estaciones_cercanas(estaciones, coordenadas, k):
    return sorted((calcula_distancia(coordenadas, estacion.ubicacion), estacion.nombre, estacion.bicis_disponibles) 
                  for estacion in estaciones 
                  if estacion.bicis_disponibles > 0)[:k]

    # distancias_a_estaciones = []
    # for estacion in estaciones:
    #     # 1. Filtrar estaciones con bicicletas disponibles
    #     if estacion.bicis_disponibles > 0:
    #         # 2. Calcular distancia y crear la tupla deseada
    #         dist = calcula_distancia(coordenadas, estacion.ubicacion)
    #         distancias_a_estaciones.append((dist, estacion.nombre, estacion.bicis_disponibles))

    # # 3. Ordenar la lista por la distancia (primer elemento de la tupla)
    # distancias_a_estaciones.sort(key=lambda x: x[0])

    # # 4. Tomar los primeros k elementos
    # return distancias_a_estaciones[:k]