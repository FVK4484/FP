from collections import defaultdict
import csv
from statistics import mean
import statistics
from typing import NamedTuple 
from datetime import datetime,date 
 
Mejora = NamedTuple("Mejora",      
       [("denominacion", str),  
        ("coste", int),  
        ("fecha", date)]) 
 
Vivienda = NamedTuple("Vivienda",      
      [("propietario", str), 
       ("calle", str), 
       ("fecha_adquisicion", date), 
       ("numero", int), 
       ("metros",float), 
       ("precio",int),         
       ("mejoras", list[Mejora])])

# Ejercicio 1.
def lee_viviendas(ruta: str) -> list[Vivienda]:
    lista = []
    with open(ruta, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for propietario, calle, numero, fecha_adquisicion, metros, precio, mejoras in lector:
            numero = int(numero)
            fecha_adquisicion = parsea_fecha(fecha_adquisicion)
            metros = float(metros)
            precio = int(precio)
            mejoras = parsea_mejoras(mejoras)
            tupla = Vivienda(propietario, calle, fecha_adquisicion, numero, metros, precio, mejoras)
            lista.append(tupla)
        return lista

def parsea_fecha(fecha: str) -> date:
    return datetime.strptime(fecha, "%d/%m/%Y").date()

def parsea_mejoras(mejoras: str) -> list[Mejora]:
    mejoras_nuevas = parsea_lista(mejoras)
    lista = []
    for mejora in mejoras_nuevas:
        denominacion, coste, fecha = mejora.split('-')
        coste = int(coste)
        fecha = parsea_fecha(fecha)
        tupla = Mejora(denominacion, coste, fecha)
        lista.append(tupla)
    return lista

def parsea_lista(lista: str) -> list[str]:
    if len(lista) > 0:
        lista = lista.split('*')
    else:
        lista = []
    return lista

# Ejercicio 2.
def total_mejoras_por_calle(viviendas: list[Vivienda], par_impar: str) -> dict[str,int]:
    dicc = defaultdict(int)
    for vivienda in viviendas:
        if (par_impar == 'par') and (vivienda.numero % 2 == 0):
            dicc[vivienda.calle] += len(vivienda.mejoras)
        elif (par_impar == 'impar') and (vivienda.numero % 2 != 0):
            dicc[vivienda.calle] += len(vivienda.mejoras)
    return dicc

def es_par(numero: int) -> bool:
    res = False
    if (numero % 2) == 0:
        res = True
    return res

# Ejercicio 3.
def vivienda_con_mejora_mas_rapida(viviendas: list[Vivienda]) -> tuple[str, str, int, 
int, str]: 
    aux = list() 
    for v in viviendas: 
        for m in v.mejoras: 
            aux.append((v, dias_vivienda_mejora(v, m), m.denominacion)) 
    vivienda, dias, denominacion = min(aux, key = lambda e: e[1]) 
    return (vivienda.propietario, vivienda.calle, vivienda.numero, dias, denominacion)

def dias_vivienda_mejora(vivienda: Vivienda, mejora: Mejora) -> int: 
    return (mejora.fecha - vivienda.fecha_adquisicion).days 

# Ejercicio 4.
def calle_mayor_diferencia_precios(viviendas: list[Vivienda]) -> str:
    dicc1 = defaultdict(int)
    dicc2 =defaultdict(int)

    for vivienda in viviendas:
        if es_par(vivienda.numero):
            dicc1[vivienda.calle] += vivienda.precio
        else:
            dicc2[vivienda.calle] += vivienda.precio

    todas_las_calles = set(dicc1.keys()) | set(dicc2.keys())  
    dicc_diferencias = defaultdict(int)
    
    for calle in todas_las_calles: 
        suma_par = dicc1[calle]
        suma_impar = dicc2[calle]        
        dicc_diferencias[calle] = abs(suma_par - suma_impar)

    dicc_ordenado = sorted(dicc_diferencias.items(), key=lambda x: x[1], reverse=True)
    
    return dicc_ordenado[0][0]

# Ejercicio 5.
def n_viviendas_top_valoradas_por_calle(viviendas: list[Vivienda], 
                                        fecha: date|None = None, 
                                        n: int = 3) -> dict[str,list[tuple[str,int,int]]]:
    dicc = defaultdict(list)
    for vivienda in viviendas:

        if fecha is None or fecha <= vivienda.fecha_adquisicion:
            dicc[vivienda.calle].append((vivienda.propietario, vivienda.numero, calcula_valor_vivienda(vivienda.precio, vivienda.mejoras)))
    # return {calle: sorted(vivienda, key = lambda x:x[2], reverse = True)[:n] 
    #         for calle, vivienda in dicc.items()}
    dicc2 = defaultdict(list)
    for calle, vivienda in dicc.items():
        dicc2[calle] = sorted(vivienda, key = lambda x:x[2], reverse = True)[:n]
    return dicc2

def calcula_valor_vivienda(precio: int, mejoras: list[Mejora]) -> int:
    suma_coste = 0
    for mejora in mejoras:
        suma_coste += mejora.coste
    return suma_coste + precio

# Ejercicio 6.
def valor_metro_cuadrado_por_calle_y_año(viviendas: list[Vivienda]) -> list[tuple[int,list[tuple[str,float]]]]:
    d = agrupar_viviendas_por_anyo(viviendas) 
    d2 = {anyo: promedio_metro_cuadrado_por_calle(lista_viviendas)for anyo, lista_viviendas in d.items()} 
    return sorted(d2.items())

def agrupar_viviendas_por_anyo(viviendas: list[Vivienda]) -> dict[int, list[Vivienda]]: 
    res = defaultdict(list) 
    for v in viviendas: 
        res[v.fecha_adquisicion.year].append(v) 
    return res 

def agrupar_viviendas_por_calle(viviendas: list[Vivienda]) -> dict[int, list[Vivienda]]: 
    res = defaultdict(list) 
    for v in viviendas: 
        res[v.calle].append(v) 
    return res 
 
def promedio_metro_cuadrado_por_calle(viviendas: list[Vivienda]) -> list[tuple[str, 
float]]: 
    d = agrupar_viviendas_por_calle(viviendas) 
    d2 = {calle: statistics.mean(precio_metro(v) for v in lista_viviendas) for calle, lista_viviendas in d.items()} 
    return sorted(d2.items(), key = lambda it: it[1], reverse = True) 
 
def precio_metro (vivienda: Vivienda) -> float: 
    return vivienda.precio/vivienda.metros 