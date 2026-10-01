import csv
from geopy.distance import geodesic
from collections import namedtuple
from typing import List
Centros_Sanitarios = namedtuple('Centros_Sanitarios', 'nombre, localidad, coordenadas, estado, num_camas, tiene_acceso_discapacitados, tiene_uci')

def leer_centros(fichero):
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for nombre, localidad, latitud, longitud, estado, num_camas, tiene_acceso_discapacitados, tiene_uci in lector:
            latitud = float(latitud)
            longitud = float(longitud)       
            coordenadas = (latitud, longitud)  
            num_camas = int(num_camas)
            tiene_acceso_discapacitados = parsea_booleanos(tiene_acceso_discapacitados)
            tiene_uci = parsea_booleanos(tiene_uci)
            tupla = Centros_Sanitarios(nombre, localidad, coordenadas, estado, num_camas, tiene_acceso_discapacitados, tiene_uci)
            lista.append(tupla)
    return lista

def parsea_booleanos(cadena):
    res = False
    cadena = cadena.strip().lower()
    if cadena == 'true':
        res = True
    return res

def calcular_total_camas_centros_accesibles(centros):
    cont = 0
    for centro in centros:
        if centro.tiene_acceso_discapacitados:
            cont += centro.num_camas
    return cont

def calcular_distancia(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

def obtener_centros_con_uci_cercanos_a(centros, punto_referencia, distancia_umbral):
    centros_filtrados = []
    for centro in centros:
        nombre, localidad, coordenadas, tiene_uci, _, _, _ = centro
        if tiene_uci:
            distancia = calcular_distancia(punto_referencia, coordenadas)
            if distancia <= distancia_umbral:
                centros_filtrados.append((nombre, localidad, coordenadas))
    return centros_filtrados

# def generar_mapa(nombre, localidad, coordenadas(coord1, coord2)):
