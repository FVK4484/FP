from typing import NamedTuple
from datetime import datetime
from parsers import parsea_fecha 
from collections import Counter
import csv 

Compra = NamedTuple('Compra',
                    [('dni', str),
                     ('supermercado', str),
                     ('provincia', str),
                     ('fecha_llegada', datetime),
                     ('fecha_salida', datetime),
                     ('total_compra', float)]
                    )

def lee_compras(fichero: str) -> list[Compra]:
    with open(fichero, encoding = 'utf-8') as f:
        compras = []
        lector = csv.reader(f)
        next(lector)
        for dni, supermercado, provincia, fecha_llegada,\
        fecha_salida, total_compra in lector:
            fecha_llegada = parsea_fecha(fecha_llegada)
            fecha_salida = parsea_fecha(fecha_salida)
            total_compra = float(total_compra)
        tupla = Compra (dni, supermercado, provincia, \
                        fecha_llegada, fecha_salida, \
                        total_compra)
        compras.append(tupla)
    return compras

def compra_maxima_minima_provincia (compras: list[Compra], \
                                    provincia: str | None = None) -> tuple[float, float]:
    # Filtrar lista de compras
    compras_provincia = []
    for c in compras:
        if provincia is None or provincia == c.provincia:
            compras_provincia.append(c.total_compra)

    # Obtener compra mínima y máxima 
    compra_mínima = min(compras_provincia)
    compra_máxima = max(compras_provincia)

    return compra_mínima, compra_máxima

def hora_menos_afluencia (compras: list[Compra]) -> int:
    dic = numero_clientes_por_hora(compras)
    return min(dic, key = dic.get)

def numero_clientes_por_hora(compras: list[Compra]) -> dict[int, int]:
    return Counter(c.fecha_llegada.hour for c in compras)


