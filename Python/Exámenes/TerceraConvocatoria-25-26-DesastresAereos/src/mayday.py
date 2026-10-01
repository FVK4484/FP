from collections import Counter, defaultdict
import statistics
from typing import NamedTuple 
from datetime import datetime, date, time 
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

def lee_desastres(fichero:str)->list[Desastre]:
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for fecha, hora, localizacion, operadores, codigos, rutas, modelos, supervivientes, fallecidos, fallecidos_en_tierra, operacion in lector:
            fecha = parsea_fecha(fecha)
            hora = parsea_hora(hora)
            vuelos = parsea_vuelos(operadores, codigos, rutas, modelos)
            supervivientes = int(supervivientes)
            fallecidos = int(fallecidos)
            fallecidos_en_tierra = int(fallecidos_en_tierra)
            tupla = Desastre(fecha, hora, localizacion, supervivientes, fallecidos, fallecidos_en_tierra, operacion, vuelos)
            lista.append(tupla)
        return lista           

def parsea_fecha(fecha: str)->date: 
    return datetime.strptime(fecha, "%d/%m/%Y").date()

def parsea_hora(hora: str)->time|None:
    res = None
    if len(hora) > 0:
        res = datetime.strptime(hora, "%H:%M").time()
    return res

def parsea_vuelos(operadores: str, codigos: str, rutas: str, modelos: str)->list[Vuelo]:
    lista = []
    operadores = parsea_lista(operadores)
    codigos= parsea_lista(codigos)
    rutas = parsea_lista(rutas)
    modelos = parsea_lista(modelos)
    for operador, codigo, ruta, modelo in zip(operadores, codigos, rutas, modelos):
        tupla = Vuelo(operador, codigo, ruta, modelo)
        lista.append(tupla)
    return lista

def parsea_lista(lista: str)->str:
    return lista.split("/")

# EJERCICIO 2

def desastres_con_fallecidos_en_tierra(desastres:list[Desastre],n:int|None=None)->list[tuple[str,date,time,int]]:
    return sorted(((desastre.localizacion, desastre.fecha, 
                   desastre.hora, desastre.fallecidos_en_tierra) 
                   for desastre in desastres), key = lambda x:x[3], reverse = True)[:n]

# EJERCICIO 3

def decada_mas_colisiones(desastres:list[Desastre]) -> tuple[int,int]:
    dicc1 = defaultdict(int)
    dicc2 = defaultdict(int)
    for desastre in desastres:
        if len(desastre.vuelos) > 1:
            dicc1[desastre.fecha.year] += 1
    for año, colisiones in dicc1.items():
        dicc2[año // 10 * 10] += colisiones
    return max(dicc2.items(), key = lambda x:x[1])

# EJERCICIO 4

def mayor_periodo_sin_desastres(desastres: list[Desastre],operacion: str|None = None) -> tuple[date, date, int]: 
    filtrados = (desastre for desastre in desastres if operacion == None or desastre.operacion == operacion) 
    ordenados = sorted(filtrados, key=lambda x: x.fecha) 
    diff = [(desastre1.fecha, desastre2.fecha, (desastre2.fecha-desastre1.fecha).days)
            for desastre1, desastre2 in zip(ordenados, ordenados[1:])]           
    return max(diff, key=lambda x: x[2]) 

# EJERCICIO 5

def estadisticas_por_operacion(desastres: list[Desastre], 
                               limite_tasa_supervivencia: float|None = None)->dict[str, tuple[int, float, float]]: 
    
    d = desastres_por_operacion(desastres, limite_tasa_supervivencia) 
    
    return {operacion: estadisticas_alt(desastres) for operacion, desastres in d.items()} 
 
def desastres_por_operacion(desastres: list[Desastre], limite_tasa_supervivencia: float|None = None) -> dict[str, list]: 
    result = defaultdict(list) 
    for d in desastres: 
        if limite_tasa_supervivencia == None or tasa_supervivencia(d) <= limite_tasa_supervivencia: result[d.operacion].append(d) 
    return result 
   
def estadisticas(desastres: list[Desastre]) -> tuple[int, float, float]: 
   return (len(desastres), 
            statistics.mean(d.supervivientes for d in desastres),
            statistics.mean(d.fallecidos for d in desastres))

def estadisticas_alt(desastres: list[Desastre]) -> tuple[int, float, float]: 
    supervivientes = 0 
    fallecidos = 0 
    for d in desastres: 
        supervivientes += d.supervivientes 
        fallecidos += d.fallecidos 
    res = None 
    if len(desastres) > 0: 
        res = (len(desastres), supervivientes / len(desastres),    
            fallecidos / len(desastres))   
    return res 
 
def tasa_supervivencia(desastre: Desastre) -> float: 
   return desastre.supervivientes / (desastre.supervivientes + desastre.fallecidos)