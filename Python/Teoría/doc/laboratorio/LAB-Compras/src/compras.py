from collections import defaultdict
from typing import NamedTuple
from datetime import datetime, time
import csv

Compra = NamedTuple('Compra',
                    [('dni', str),
                     ('supermercado', str),
                     ('provincia', str),
                     ('fecha_llegada', datetime),
                     ('fecha_salida', datetime),
                     ('total_compra', float)]
                    )

# EJERCICIO 1
def lee_compras(fichero: str) -> list[Compra]:
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra in lector:
            provincia = str(provincia)
            fecha_llegada = parsea_fecha(fecha_llegada)
            fecha_salida = parsea_fecha(fecha_salida)
            total_compra = float(total_compra)
            tupla = Compra(dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra)
            lista.append(tupla)
        return lista
        
def parsea_fecha(fecha: str) -> datetime:
    return datetime.strptime(fecha, "%d/%m/%Y %H:%M")

# EJERCICIO 2
def compra_maxima_minima_provincia(compras: list[Compra], provincia: str) -> tuple[float, float]:
    lista = []
    for compra in compras:
        if provincia == compra.provincia:
            lista.append(compra.total_compra)
        elif provincia == None:
            lista.append(compra.total_compra)
    return (max(lista), min(lista))

# EJERCICIO 3
def hora_menos_afluencia(compras: list[Compra]) -> tuple[time, int]:
    dicc = defaultdict(list)
    for compra in compras:
        dicc[compra.fecha_llegada.hour].append(compra.dni)
    return (min((dicc.items()), key = lambda x:len(x[1]))[0], len(min((dicc.items()), key = lambda x:len(x[1]))[1]))

# EJERCICIO 4
def supermercados_mas_facturacion(compras: list[Compra], n: int = 3) -> list[tuple[int, tuple[str, float]]]:
    dicc = defaultdict(float)
    for compra in compras:
        dicc[compra.supermercado] += compra.total_compra
    lista = sorted((dicc.items()), key = lambda x:x[1], reverse = True)[:n]
    return list(enumerate(lista))

def clientes_itinerantes(compras: list[Compra], n: int) -> list[tuple[str, list]]:
    dicc = defaultdict(set)
    res = defaultdict(list)
    lista = []
    for compra in compras:
        dicc[compra.dni].add(compra.provincia)
    for dni, set_provincias in dicc.items():
        for provincia in set_provincias:
            res[dni].append(provincia)
    for dni, lista_provincias in res.items():
        if len(lista_provincias) <= n:
            continue
        else:
            lista.append((dni, sorted(res[dni])))
    return lista

def dias_estrella(compras: list[Compra], supermercado: str, provincia: str) -> list[datetime]:
    dicc = defaultdict(float)
    for compra in compras:
        if compra.provincia == provincia and supermercado == compra.supermercado and compra.fecha_llegada.date() == compra.fecha_salida.date():
            dicc[compra.fecha_llegada.date()] = compra.total_compra
    n = 0
    lista = sorted(dicc.items())
    lista2 = []
    for n in range(0, len(lista) - 1):
        n += 1
        if sorted(dicc.items())[n - 1][1] - sorted(dicc.items())[n][1] < 0:
                if sorted(dicc.items())[n + 1][1] - sorted(dicc.items())[n][1] < 0:
                    lista2.append(sorted(dicc.items())[n][0])

    lista3 = []
    for elemento in lista2:
        lista3.append(parseo_fecha2(elemento))
    return lista3
    
def parseo_fecha2(fecha: datetime) -> str:
    return datetime.strftime(fecha, "%d/%m/%Y")
    
