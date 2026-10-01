from typing import List, NamedTuple 
from datetime import datetime, date, time 
from collections import defaultdict
import csv
 
Vuelo = NamedTuple("Vuelo",      
  [("operador", str), # Compañía aérea que operaba el vuelo (opcional) 
   ("codigo", str),   # Código de vuelo (opcional) 
   ("ruta", str),     # Ruta del vuelo (opcional) 
   ("modelo", str)])  # Modelo de avión que operaba el vuelo (opcional) 
 
Desastre = NamedTuple("Desastre",      
  [("fecha", date),               # Fecha del desastre aéreo 
    ("hora", time | None),        # Hora del desastre (opcional) 
    ("localizacion", str),        # Localización del desastre 
    ("supervivientes",int),       # Supervivientes 
    ("fallecidos",int),           # Fallecidos     
    ("fallecidos_en_tierra",int), # Fallecidos en tierra (no eran pasajeros del vuelo) 
    ("operacion",str),        # Momento operativo del vuelo cuando ocurrió el desastre 
    ("vuelos", list[Vuelo])]) # Vuelos implicados en el desastre    

# EJERCICIO 1
   
def lee_desastres(ruta:str) -> list[Desastre]:
    lista = []
    with open(ruta, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ";")
        next(lector)
        for fecha, hora, localizacion, operadores, codigos, rutas, modelos, supervivientes, fallecidos, fallecidos_en_tierra, operacion in lector:
            fecha = parsea_fecha(fecha)
            hora = parsea_hora(hora)
            localizacion = str(localizacion)
            vuelos = parsea_vuelos(operadores, codigos, rutas, modelos)
            supervivientes = int(supervivientes)
            fallecidos = int(fallecidos)
            fallecidos_en_tierra = int(fallecidos_en_tierra)
            operacion = str(operacion)
            tupla = Desastre(fecha, hora, localizacion, supervivientes, fallecidos, fallecidos_en_tierra, operacion, vuelos)
            lista.append(tupla)
        return lista          

def parsea_fecha(fecha:str) -> date:
    return datetime.strptime(fecha, "%d/%M/%Y").date()

def parsea_hora(hora:str) -> time | None:
    res = None
    if len(hora) > 0:
        res = datetime.strptime(hora, "%H:%M").time()
    return res

def parsea_vuelos(operadores:str, 
                     codigos:str, 
                     rutas:str, 
                     modelos:str) -> list[Vuelo]:
    result = []
    operadores = parsea_lista(operadores)
    codigos = parsea_lista(codigos)
    rutas = parsea_lista(rutas)
    modelos = parsea_lista(modelos)
    for operadores, codigos, rutas, modelos in zip(operadores, codigos, rutas, modelos):
        result.append(Vuelo(operadores, codigos, rutas, modelos))
    return result

def parsea_lista(cadena: str) -> list[str]:
    return cadena.split("/")

# EJERCICIO 2

def desastres_con_fallecidos_en_tierra(desastres: List[Desastre], numero: int | None = None) -> List[tuple[str, date, time, int]]:
    return sorted(((desastre.localizacion, desastre.fecha, desastre.hora, desastre.fallecidos_en_tierra) 
                  for desastre in desastres 
                  if not None and desastre.fallecidos_en_tierra > 0), key = lambda x:x[3], reverse = True)[:numero]

# EJERCICIO 3

def decada_mas_colisiones(desastres:list[Desastre]) -> tuple[int,int]:            
   return max(((decada, len(desastre)) 
               for decada, desastre 
               in colisiones_por_decada(desastres).items()), 
               key = lambda x:x[1])

    
def colisiones_por_decada(desastres: list[Desastre]) -> dict[int, list[Desastre]]:
    dicc = defaultdict(list)
    for desastre in desastres: 
        if len(desastre.vuelos) > 1:
            dicc[desastre.fecha.year // 10 * 10].append(desastre)
    return dicc

# EJERCICIO 4

def mayor_periodo_sin_desastres(desastres: list[Desastre], 
                                operacion: str|None = None) -> tuple[date, date, int]: 
    
    filtrados_y_ordenados = sorted((desastre for desastre in desastres if operacion == None or desastre.operacion == operacion), key = lambda x:x.fecha)  

    diff = [(desastre1.fecha, desastre2.fecha, (desastre2.fecha - desastre1.fecha).days) for desastre1, desastre2 in zip(filtrados_y_ordenados, filtrados_y_ordenados[1:])]

    return max(diff, key=lambda x: x[2]) 
