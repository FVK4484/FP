from collections import namedtuple, defaultdict
from typing import List
import csv
from datetime import datetime

PartidoBasket = namedtuple('PartidoBasket','fecha, equipo1, equipo2, competicion, puntos_eq1, puntos_eq2, faltas_eq1, faltas_eq2')

def lee_partidos(fichero):
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for fecha, equipo1, equipo2, competicion, cuartos, faltas_eq1, faltas_eq2 in lector:
            fecha = datetime.strptime(fecha, '%d/%m/%Y').date()
            puntos_eq1 = parsea_y_suma_resultados(cuartos)[0]
            puntos_eq2 = parsea_y_suma_resultados(cuartos)[1]
            faltas_eq1 = int(faltas_eq1)
            faltas_eq2 = int(faltas_eq2)
            tupla = PartidoBasket(fecha, equipo1, equipo2, competicion, puntos_eq1, puntos_eq2, faltas_eq1, faltas_eq2)
            lista.append(tupla)
    return lista

def parsea_y_suma_resultados(cuartos):
    puntosEq1, puntosEq2 = 0, 0 
    cuartos = cuartos.split('*')
    for cuarto in cuartos: 
        eq1, eq2 = cuarto.split('-')
        puntosEq1 += int(eq1) 
        puntosEq2 += int(eq2) 
    return puntosEq1, puntosEq2

def equipo_con_mas_faltas(partidos, equipos = None):
    result = defaultdict(int)
    for partido in partidos:
        if equipos == None or partido.equipo1 in equipos:
            result[partido.equipo] += partido.faltas_eq1
        if equipos == None or partido.equipo2 in equipos:
            result[partidos.equipo] += partido.faltas_eq2
    return max(result.items(), key = lambda x: x[1])[0]
    
def media_puntos_por_equipo(partidos, competiciones):
    dic1 = defaultdict(int)
    for partido in partidos:
        pass

def victorias_por_equipo(partidos: List[PartidoBasket]) -> dict[str, int]:
    dict = defaultdict(int)
    for partido in partidos:
        if partido.puntos_eq1 > partido.puntos_eq2:
            dict[partido.equipo1] += 1
        elif partido.puntos_eq2 > partido.puntos_eq1:
            dict[partido.equipo2] += 1
    return dict

def equipos_minimo_victorias(partidos: List[PartidoBasket], n: int) -> List[str]:
    dicc = victorias_por_equipo(partidos)
    return sorted((equipo for equipo, victorias in dicc.items() if victorias >= n), 
                  key = lambda x:x[1])

def equipos_mas_victorias_por_año(partidos: List[PartidoBasket], n: int) -> dict[int, List[str]]:
    dicc = defaultdict(list)
    for partido in partidos:
        dicc[partido.fecha.year].append(partido)
    res = {}
    for año, partidos_año in dicc.items():
        res[año] = equipos_minimo_victorias(partidos_año, n)
    return res


