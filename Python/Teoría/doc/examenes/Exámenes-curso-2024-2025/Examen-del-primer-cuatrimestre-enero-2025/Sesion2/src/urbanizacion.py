from collections import defaultdict
from typing import NamedTuple 
from datetime import datetime, date 
import csv

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

# Ejercicio 1
def lee_viviendas(ruta: str) -> list[Vivienda]:
    lista = []
    with open(ruta, encoding = "utf-8") as f:
        lector = csv.reader(f, delimiter = ";")
        next(lector)
        for propietario, calle, numero, fecha_adquisicion, metros, precio, mejoras in lector:
            numero = int(numero)
            fecha_adquisicion = parsea_fecha(fecha_adquisicion)
            metros = float(metros)
            precio = float(precio)
            mejoras = parsea_mejoras(mejoras)
            tupla = Vivienda(propietario, calle, fecha_adquisicion, numero, metros, precio, mejoras)
            lista.append(tupla)
        return lista

def parsea_fecha(fecha: str) -> date:
    return datetime.strptime(fecha, "%d/%m/%Y").date()

def parsea_mejoras(mejoras: str) -> Mejora:
    mejoras1 = mejoras.split("*")
    mejoras2 = []
    for mejora in mejoras1:
        mejoras2.append(mejora.split("-"))
    lista = []
    for elemento in mejoras2:
        if len(elemento) > 1:
            tupla = Mejora(elemento[0], int(elemento[1]), parsea_fecha(elemento[2]))
            lista.append(tupla)
    return lista

# Ejercicio 2
def total_mejoras_por_calle (viviendas: list[Vivienda], par_impar: str) -> dict[str,int]:
    dicc1 = defaultdict(list)
    dicc2 = defaultdict(list)
    dicc3 = defaultdict(int)
    for vivienda in viviendas:
        if vivienda.numero % 2 == 0:
            dicc1[vivienda.calle] += vivienda.mejoras
        else:
            dicc2[vivienda.calle] += vivienda.mejoras
    if par_impar == "par":
        for calle, lista_mejoras in dicc1.items():
            dicc3[calle] = len(lista_mejoras)
    else:
        for calle, lista_mejoras in dicc2.items():
            dicc3[calle] = len(lista_mejoras)
    return dicc3

# Ejercicio 3
def vivienda_con_mejora_mas_rapida(viviendas: list[Vivienda]) -> tuple[str,str,int,int,str]:
    g = ((vivienda, mejora) for vivienda in viviendas for mejora in vivienda.mejoras) 
 
    vivienda, mejora = min(g, key = lambda x: dias_vivienda_mejora(x[0], x[1])) 
    return (vivienda.propietario, vivienda.calle, vivienda.numero, dias_vivienda_mejora(vivienda, mejora),mejora.denominacion) 

def dias_vivienda_mejora(vivienda: Vivienda, mejora: Mejora) -> int: 
    return (mejora.fecha - vivienda.fecha_adquisicion).days

# Ejercicio 4
def calle_mayor_diferencia_precios(viviendas: list[Vivienda]) -> str:
    dicc1 = defaultdict(int)
    dicc2 = defaultdict(int)
    for vivienda in viviendas:
        if vivienda.numero % 2 == 0:
            dicc1[vivienda.calle] += vivienda.precio
        else:
            dicc2[vivienda.calle] += vivienda.precio
    ordenados1 =  sorted(dicc1.values(), reverse = True)
    ordenados2 =  sorted(dicc2.values(), reverse = True)
    return ordenados2

# def calcula_diferencias():



print(calle_mayor_diferencia_precios(lee_viviendas(r"doc\examenes\Exámenes-curso-2024-2025\Examen-del-primer-cuatrimestre-enero-2025\Sesion2\data\urbanizacion.csv")))