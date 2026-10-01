from collections import Counter, defaultdict
from typing import NamedTuple, List, Tuple
from datetime import datetime
import csv
 
Partida = NamedTuple("Partida", [
    ("pj1", str),
    ("pj2", str),
    ("puntuacion", int),
    ("tiempo", float),
    ("fecha_hora", datetime),
    ("golpes_pj1", List[str]),
    ("golpes_pj2", List[str]),
    ("movimiento_final", str),
    ("combo_finish", bool),
    ("ganador", str),
    ])

# EJERCICIO1

def lee_partidas(fichero: str) -> List[Partida]:
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for pj1, pj2, puntuacion, tiempo, fecha_hora, golpes_pj1, golpes_pj2, movimiento_final, combo_finish, ganador in lector:
            puntuacion = int(puntuacion)
            tiempo = float(tiempo)
            fecha_hora = datetime.strptime(fecha_hora, '%Y-%m-%d  %H:%M:%S')
            golpes_pj1 = parsea_lista(golpes_pj1)
            golpes_pj2 = parsea_lista(golpes_pj2)
            combo_finish = parsea_booleanos(combo_finish)
            tupla = Partida(pj1, pj2, puntuacion, tiempo, fecha_hora, golpes_pj1, golpes_pj2, movimiento_final, combo_finish, ganador)
            lista.append(tupla)
        return lista

def parsea_booleanos(cadena: str) -> bool:
    res = False
    if cadena == '1':
        res = True
    return res

def parsea_lista(cadena: str) -> List[str]:
    lista = []
    cadena = cadena.replace('[', '').replace(']', '')
    for elemento in cadena.split(','):
        lista.append(elemento)
    return lista

# EJERCICIO2

def victoria_mas_rapida(partidas: List[Partida]) -> Tuple[str, str, float]:

    partida_mas_rapida = partidas[0]

    for partida in partidas:
        
        tiempo_actual = partida[3]
        tiempo_mas_rapido = partida_mas_rapida[3]

        if tiempo_actual < tiempo_mas_rapido:

            partida_mas_rapida = partida

    tupla = (partida_mas_rapida[0], partida_mas_rapida[1], partida_mas_rapida[3])

    return tupla

# EJERCICIO3

def top_ratio_medio_personajes(partidas: List[Partida], n: int) -> List[str]:
    dicc = defaultdict(list)
    dicc2 = defaultdict(float)
    for partida in partidas:
        dicc[partida.ganador].append(ratio_eficacia_media(partida.puntuacion, partida.tiempo))
    for nombre, lista_ratios in dicc.items():
        dicc2[nombre] = sum(lista_ratios) / len(lista_ratios)
    lista_ordenada = sorted(dicc2.items(), key = lambda x:x[1])
    return [elemento[0] for elemento in lista_ordenada][:n]

def ratio_eficacia_media(puntuacion: int, tiempo: float) -> float:
    return puntuacion / tiempo

# EJERCICI4
def enemigos_mas_debiles(partidas: List[Partida], personaje: str) -> Tuple[list[str], int]:
    dicc1 = defaultdict(list)
    dicc2 = defaultdict(list)

    for partida in partidas:
        if partida.pj1 == personaje and partida.ganador == personaje:         
            dicc1[personaje].append(partida.pj2)
        elif partida.pj2 == personaje and partida.ganador == personaje:
            dicc2[personaje].append(partida.pj1)

    lista1 = []
    lista2 = []  

    for _ , lista_enemigos1 in dicc1.items():
        lista1 = lista_enemigos1   
    
    for _ , lista_enemigos2 in dicc2.items():
        lista2 = lista_enemigos2
    
    lista_total = lista1 + lista2

    dicc3 = Counter(lista_total)

    dicc4 = defaultdict(list)

    for nombre, numero in dicc3.items():
        dicc4[numero].append(nombre)
    tupla = max(dicc4.items())

    return (tupla[1], tupla[0])

# EJERCICIO5

print(enemigos_mas_debiles(lee_partidas(r"FP_25_26\doc\laboratorio\LAB-Street-Fighter\data\games.csv"), "Ken"))