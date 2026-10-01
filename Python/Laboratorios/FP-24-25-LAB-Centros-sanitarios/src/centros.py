from collections import namedtuple
import csv
from coordenadas import calcular_distancia

CentroSanitario = namedtuple('CentroSanitario', 
    'nombre, localidad, coordenadas, estado, num_camas, acceso_minusvalidos, tiene_uci')

def lee_centros(fichero):
    with open(fichero, encoding = 'utf-8') as f:
        centros = []
        lector = csv.reader(f, delimiter= ';')
        next(lector)
        for nombre, localidad, longitud, latitud, estado, num_camas, \
        acceso_minusvalidos, tiene_uci in lector:
            nombre = nombre.strip()
            localidad = localidad.strip()
            coordenadas = (latitud, longitud)
            estado = estado.strip()
            acceso_minusvalidos = parsea_booleanos(acceso_minusvalidos)
            tiene_uci = parsea_booleanos(tiene_uci)
            tupla = CentroSanitario(nombre, localidad, coordenadas, estado,
                 num_camas, acceso_minusvalidos, tiene_uci)
            centros.append(tupla)
    return centros

def parsea_booleanos(cadena):
    cadena = cadena.strip()
    if cadena == "True":
        res = True
    else:
        res = False
    return res

def calcular_total_camas_centros_accesibles(centros):
    suma = 0
    for c in centros:
        if c.acceso_minusvalidos:
            suma += c.num_camas
    return suma

def obtener_centros_con_uci_cercanos_a(centros, ubicacion, d):
    res = []
    for c in centros:
        if c.tiene_uci and \
              calcular_distancia(ubicacion, c.coordenadas) <= d :
            res.append((c.nombre,c.localidad,c.coordenadas))
    return res

def obtener_centros_uci(centros: list[CentroSanitario]) -> list[str]:
    res = set()
    for c in centros:
        if c.tiene_uci:
            res.add(c.localidades)
    return sorted(res)
    
def calcular_numero_centros_uci(centros: list[CentroSanitario], estado:str) -> list[str]:

    # return len(c for c in centros if c.tiene_uci and c.estado == estado)

    # res = []
    contador = 0
    for c in centros:
        if c.tiene_uci and c.estado == estado:
            # res.append(c)
            contador += 1
    # return len(res)
    return contador

def obtener_centro_mas_camas(centros: list[CentroSanitario]) -> str:
    return max(centros, key = lambda c:c.num_camas).nombre

def obtener_n_centros_mas_camas(centros: list[CentroSanitario], \
                                n: int = 3) -> list[tuple[str, str, int]]:
    res = [(c.nombre, c.localidad, c.num_camas) for c in centros]
    res = sorted(res, key = lambda t:t[2], reverse = True)
    return res[:n]

def agrupar_centros_por_estado(centros: list[CentroSanitario]) \
                               -> dict[str, list[CentroSanitario]]:
    res = dict()
    for c in centros:
        estado = c.estado
        if estado not in res:
            res[estado] = [c.nombre]
        else:
            res[estado].append(c.nombre)
    return res

def agrupar_nombres_localidades_por_estado(centros: list[CentroSanitario]) \
                               -> dict[str, set[str]]:
    res = dict()
    for c in centros:
        estado = c.estado
        if estado not in res:
            res[estado] = {c.localidad}
        else:
            res[estado].add(c.localidad)
    return res

def obtener_número_centros_con_estado_por_localidad(centros: list[CentroSanitario], estado: str, localidad) -> dict[str, int]:
    res = dict ()
    for c in centros:
        if c.estado == estado:
            localidad == c.localidad
            if localidad not in res:
                res[localidad] = 1
            else:
                res[localidad] += 1
    return res

def obtener_n_camas_por_localidad(centros: list[CentroSanitario], num_camas: int) -> int:
    pass

def obtener_media_camas_centros_localidades_estado(centros, num_camas):
    pass
