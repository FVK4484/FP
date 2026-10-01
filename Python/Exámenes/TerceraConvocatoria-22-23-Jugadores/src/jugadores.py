from collections import defaultdict, namedtuple
from datetime import*
import csv
from statistics import mean

Jugador = namedtuple('Jugador', 'ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act, senior, resultados') 

# Ejercicio 1.
def lee_jugadores(fichero: str) -> list[Jugador]:
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act, senior, resultados in lector:
            fecha_ncto = parsea_fecha(fecha_ncto)
            handicap = float(handicap)
            fec_hor_act = parsea_fecha_hora(fec_hor_act)
            senior = parsea_senior(senior)
            resultados = parsea_resultados(resultados)
            tupla = Jugador(ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act, senior, resultados)
            lista.append(tupla)
        return lista

def parsea_fecha(fecha: str) -> date:
    return datetime.strptime(fecha, "%d/%m/%Y").date()

def parsea_fecha_hora(fecha_hora: str) -> datetime:
    return datetime.strptime(fecha_hora, "%d/%m/%Y %H:%M:%S")

def parsea_senior(senior: str) -> bool:
    res = False
    if senior == 'S':
        res = True
    return res

def parsea_resultados(resultados: str) -> list[int]:
    lista = []
    for resultado in resultados.split(','):
        lista.append(int(resultado))
    return lista

# Ejercicio 2.
def mejores_jugadores(jugadores: list[Jugador], anyo: int, n: int) -> list[tuple[str, str, float]]:
    return sorted(((jugador.licencia, jugador.ape_nom, jugador.handicap) for jugador in jugadores if jugador.fecha_ncto.year == anyo), key = lambda x:x[2])[:n]

# Ejercicio 3.
def jugadores_por_golpes(jugadores: list[Jugador]) -> list[tuple[int, set[str]]]:
    dicc = defaultdict(set)
    lista = []
    for jugador in jugadores:
        for elemento in jugador.resultados:
            dicc[elemento].add(jugador.licencia)
    ordenado = sorted(dicc.items(), key = lambda x:x[0], reverse = True)
    for resultado, licencias in ordenado:
        lista.append((resultado, licencias))
    return lista

# Ejercicio 4.
def promedio_ultimos_resultados(jugadores: list[Jugador], f1: date = None, f2: date = None) -> list[tuple[str, float]]:
    return [(jugador.licencia, promedio_golpes(jugador.resultados)) for jugador in jugadores if jugador.senior and en_fecha(jugador, f1, f2)]

def promedio_golpes(resultados: list[int]) -> float:
    # suma = 0
    # for resultado in resultados:
    #     suma += resultado
    # return suma / len(resultados)
    return mean(resultados)

# def en_fecha(jugador, f1, f2):
#     res = False 
#     if f1 == None and f2 == None: 
#         res = True 
#     elif f1 == None: 
#         res = jugador.fec_hor_act.date() <= f2 
#     elif f2 == None: 
#         res = f1 <= jugador.fec_hor_act.date() 
#     else: 
#         res = f1 <= jugador.fec_hor_act.date() <= f2 
#     return res 

def en_fecha(jugador, f1, f2): 
    return (f1 == None or f1 <= jugador.fec_hor_act.date()) and (f2 == None or jugador.fec_hor_act.date() <= f2)

# Ejercicio 5.
def jugador_menor_handicap_por_federacion(jugadores: list[Jugador]) -> dict[str, tuple[str, float]]:
    dicc = defaultdict(list)
    for jugador in jugadores:
        dicc[jugador.federacion].append((jugador.ape_nom, jugador.handicap))
    dicc_actu = defaultdict(tuple)
    for federacion, lista_tuplas in dicc.items():
        dicc_actu[federacion] = min_lista_tuplas(lista_tuplas)
    return dicc_actu

def min_lista_tuplas(lista_tuplas: list[tuple[str, int]]) -> tuple[str, int]:
    return min(lista_tuplas, key = lambda x:x[1])

# Ejercicio 6.
def comparativa_de_mejores_resultados_segun_handicap(jugadores: list[Jugador]) -> list[tuple[str, float]]:
    dicc = funcion_aux_A(jugadores)
    return funcion_aux_B(dicc)

# a) 
def funcion_aux_A(jugadores: list[Jugador]) -> dict[float, float]:
    dicc1 = defaultdict(list)
    for jugador in jugadores:
        dicc1[jugador.handicap].append(mejores_resultados(jugador.resultados))
    dicc2 = defaultdict(float)
    for handicap, lista_resultados in dicc1.items():
        dicc2[handicap] = mean(lista_resultados)
    return dicc2

def mejores_resultados(resultados: list[int]) -> int:
    return min(resultados)

# b)
def funcion_aux_B(diccionario: dict[float, float]) -> list[tuple[str, float]]:
    dicc_ordenado = sorted(diccionario.items())
    return [ (f"{d1[0]} vs {d2[0]}", d1[1] - d2[1]) for d1, d2 in zip(dicc_ordenado, dicc_ordenado[1:])]
