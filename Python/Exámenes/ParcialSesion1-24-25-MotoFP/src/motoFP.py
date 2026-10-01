from collections import defaultdict, Counter
import csv
from datetime import*
from typing import NamedTuple 
 
Piloto=NamedTuple("Piloto", [("nombre", str),("escuderia", str)]) 
 
CarreraFP=NamedTuple("CarreraFP",[ 
        ("fecha_hora",datetime),  
        ("circuito",str),                     
        ("pais",str),  
        ("seco",bool), # True si el asfalto estuvo seco, False si estuvo mojado 
        ("tiempo",float),  
        ("podio", list[Piloto])])

# Ejercicio 1.
def lee_carreras(filename: str) -> list[CarreraFP]:
    lista = []
    with open(filename, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for fecha_hora, circuito, pais, asfalto, tiempo, nombre_ganador, marca_ganador, nombre_segundo_clasificado, marca_segundo_clasificado, nombre_tercer_clasificado, marca_tercer_clasificado in lector:
            fecha_hora = parsea_fecha_hora(fecha_hora)
            seco = parsea_asfalto(asfalto)
            tiempo = float(tiempo)
            podio = parsea_podio(nombre_ganador, marca_ganador, nombre_segundo_clasificado, marca_segundo_clasificado, nombre_tercer_clasificado, marca_tercer_clasificado)
            tupla = CarreraFP(fecha_hora, circuito, pais, seco, tiempo, podio)
            lista.append(tupla)
        return lista
        
def parsea_fecha_hora(fecha_hora: str) -> datetime:
    return datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")

def parsea_asfalto(asfalto: str) -> bool:
    res = False
    if asfalto == 'Seco':
        res = True
    return res

def parsea_podio(nombre_ganador, marca_ganador, nombre_segundo_clasificado, marca_segundo_clasificado, nombre_tercer_clasificado, marca_tercer_clasificado) -> list[Piloto]:
    lista = []
    tupla1 = Piloto(nombre_ganador, marca_ganador)
    tupla2 = Piloto(nombre_segundo_clasificado, marca_segundo_clasificado)
    tupla3 = Piloto(nombre_tercer_clasificado, marca_tercer_clasificado)
    lista.append(tupla1)
    lista.append(tupla2)
    lista.append(tupla3)
    return lista

# Ejercicio 2.
def maximo_dias_sin_ganar(carreras: list[CarreraFP], piloto: str) -> int|None: 
    filtradas = (c for c in carreras if c.podio[0].nombre == piloto) 
    ord = sorted(filtradas, key=lambda c:c.fecha_hora) 
    res = None 
    if len(ord) >= 2: 
        gen_dif = ((c2.fecha_hora - c1.fecha_hora).days for c1, c2 in zip(ord, ord[1:])) 
        res = max(gen_dif) 
    return res

# Ejercicio 3.
def piloto_mas_podios_por_circuito(carreras: list[CarreraFP]) -> dict[str,str]:
    dicc1 = defaultdict(list)
    for carrera in carreras:
        for elemento in carrera.podio:
            dicc1[carrera.circuito].append(elemento[0])
    dicc2 = defaultdict(list)
    for circuito, lista_nombres in dicc1.items():
        contador = Counter(lista_nombres)
        dicc2[circuito].append(max(contador.items(), key=lambda x:x[1]))
    return {circuito: lista[0][0] for circuito, lista in dicc2.items()}

# Ejercicio 4.
def escuderias_con_solo_un_piloto(carreras: list[CarreraFP]) -> list[str]: 
    dicc = defaultdict(set)
    for carrera in carreras:
        for podio in carrera.podio:
            dicc[podio[1]].add(podio[0])
    lista = []
    for escuderia, conjunto_pilotos in dicc.items():
        if len(conjunto_pilotos) == 1:
            lista.append(escuderia)
    return lista

# Ejercicio 5.
# Devuelve  el  nombre  del  piloto  que  ha  obtenido  la  racha  de  victorias  consecutivas 
# más  larga  ese  año  y  la  longitud  de  esa  racha.  Si  año  es  None  entonces  el  resultado 
# será  sin  restricción  de  año.  Una  racha  es  una  secuencia  de  resultados  iguales  y 
# seguidos,  por  ejemplo,  si  G  es  gana  y  N  no  gana,  y  los  resultados  de  un  piloto  son 
# GNNGGGNNNNGG, la racha más larga de victorias es de tres (señalada en negrita). 
# Test piloto_racha_mas_larga_victorias_consecutivas 
# Para año=2024 ('Johann Zarco', 2) 
# Para año=None ('Pedro Acosta', 3)
def piloto_racha_mas_larga_victorias_consecutivas(carreras: list[CarreraFP], 
                                                  año: int|None = None) -> tuple[str, int]:
    
    filtradas = (c for c in carreras if año == None or c.fecha_hora.year == año) 
    ordenadas = sorted(filtradas, key = lambda c:c.fecha_hora) 
    rachas = [] 

    len_racha = 0 
    for c1, c2 in zip(ordenadas, ordenadas[1:]): 
        len_racha += 1  
        if c1.podio[0].nombre != c2.podio[0].nombre:  
            rachas.append((c1.podio[0].nombre, len_racha)) 
            len_racha = 0 
    return max(rachas, key = lambda t:t[1])

# Ejercicio 6.
# Devuelve  un  diccionario  que  a  cada  circuito  le  hace  corresponder  una  lista  con  los 
# nombres de los pilotos ganadores de las últimas  n carreras disputadas en el circuito 
# con  el  estado  dado  como  parámetro.  El  estado  puede  ser  "Seco"  o  "Mojado".  Las 
# listas de los nombres de los pilotos del diccionario estarán ordenadas por la fecha de 
# la carrera que ganaron, de más reciente a más antigua.
def ultimos_ganadores_por_circuito(carreras:list[CarreraFP], 
                                   n: int, 
                                   estado: str) -> dict[str, list[str]]: 
    d = defaultdict(list) 
    for carrera in carreras: 
        if estado == "Seco" and carrera.seco or estado == "Mojado" and not carrera.seco: 
            d[carrera.circuito].append((carrera.fecha_hora, carrera.podio[0].nombre)) 
    for circuito in d: 
        lista = sorted(d[circuito], reverse = True)[:n] 
        d[circuito] = [x[1] for x in lista] 
    return d


    
    



