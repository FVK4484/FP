from typing import List, NamedTuple, Tuple
import csv
from datetime import datetime
 
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

def lee_partidas(fichero: str) -> list[Partida]:
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for pj1, pj2, puntuacion, tiempo, fecha_hora, golpes_pj1, golpes_pj2, movimiento_final, combo_finish, ganador in lector:
            puntuacion = int(puntuacion)
            tiempo = float(tiempo)
            fecha_hora = parsea_fecha(fecha_hora)
            golpes_pj1 = parsea_golpes(golpes_pj1)
            golpes_pj2 = parsea_golpes(golpes_pj2)
            combo_finish = parsea_combo(combo_finish)
            tupla = Partida(pj1, pj2, puntuacion, tiempo, fecha_hora, golpes_pj1, golpes_pj2, movimiento_final, combo_finish, ganador)
            lista.append(tupla)
        return lista        

def parsea_fecha(fecha: str) -> datetime:
    return datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")

def parsea_combo(combo: str) -> bool:
    res = False
    if (combo == 1):
        res = True
    return res

def parsea_golpes(golpes: str) -> list[str]:
    lista = []
    golpes = golpes.replace("[", "").replace("]", "")
    for golpe in golpes.split(","):
        lista.append(golpe)
    return lista


def victoria_mas_rapida(partidas: list[Partida]) -> Tuple[str, str, float]:
    lista = []
    for partida in partidas:
        tupla = (partida.pj1, partida.pj2, partida.tiempo)
        if partida.tiempo < tupla[2]:
            lista.append(tupla)
    return lista



print(victoria_mas_rapida(lee_partidas('data\games.csv')))
        