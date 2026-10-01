from collections import defaultdict
import csv
from datetime import date, datetime
import statistics
import time
from typing import NamedTuple, List, Dict, Tuple, Optional, Set 
  
Artista = NamedTuple("Artista",      
                        [("nombre", str),  
                        ("hora_comienzo", time),  
                        ("cache", int)]) 
 
Festival = NamedTuple("Festival",  
                        [("nombre", str), 
                        ("fecha_comienzo", date), 
                        ("fecha_fin", date), 
                        ("estado", str),                       
                        ("precio", float), 
                        ("entradas_vendidas", int), 
                        ("artistas", List[Artista]), 
                        ("top", bool) 
                    ])

# EJERCICIO 1.

def lee_festivales (archivo:str)->List[Festival]:
    lista = []
    with open(archivo, encoding='utf-8')as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, fecha_comienzo, fecha_fin, estado, precio, entradas_vendidas, artistas, top in lector:
            fecha_comienzo = parsea_fecha(fecha_comienzo)
            fecha_fin = parsea_fecha(fecha_fin)
            precio = float(precio)
            entradas_vendidas = int(entradas_vendidas)
            artistas = parsea_artistas(artistas)
            top = parsea_top(top)
            tupla = Festival(nombre, fecha_comienzo, fecha_fin, estado, precio, entradas_vendidas, artistas, top)
            lista.append(tupla)
        return sorted(lista, key = lambda x:x[1])

def parsea_fecha(fecha: str)->date:
    return datetime.strptime(fecha, "%Y-%m-%d").date()

def parsea_artistas(artistas: str)->list[Artista]:
    lista = []
    artistas_nuevos = artistas.split("-")
    for artista in artistas_nuevos:
        lista.append(parsea_artista(artista))
    return lista

def parsea_artista(artista: str)->Artista:
    nombre, hora_comienzo, cache = artista.split('_')
    hora_comienzo = parsea_hora(hora_comienzo)
    cache = int(cache)
    return Artista(nombre, hora_comienzo, cache)

def parsea_hora(hora: str)->time:
    return datetime.strptime(hora, '%H:%M').time()

def parsea_top(top: str)->bool:
    res = False
    if (top=='sí'):
        res = True
    return res

# EJERCICIO 2.

# 2. total_facturado: esta función devuelve el importe total facturado de los festivales que se han
# celebrado entre dos fechas dadas. La función recibe una lista de tuplas de tipo Festival y dos fechas,
# cuyos valores por defecto son None. La función devuelve un número real con el total facturado por los
# festivales celebrados entre las dos fechas dadas. Si la fecha inicial es None se hace el cálculo sin limitar
# la fecha mínima de los festivales. Si la fecha final es None se hace el cálculo sin limitar la fecha máxima
# de los festivales. Para calcular el total facturado por festival hay que multiplicar el número de entradas
# por el precio de la entrada del festival. Nota: tenga en cuenta que la función debe tomar la facturación
# de los festivales con estado celebrado en el rango de fechas, es decir, solo se tendrán en cuenta
# aquellos festivales que empiezan y acaban dentro del rango de fechas. (1.25 punto)

def total_facturado(festivales:List[Festival], fecha_ini:Optional[date]=None, fecha_fin:Optional[date]=None)->float:
    return sum(festival.entradas_vendidas * festival.precio 
               for festival in festivales 
               if (festival.estado == 'CELEBRADO') and (fecha_ini is None or fecha_ini <= festival.fecha_comienzo) 
               and (fecha_fin is None or fecha_fin >= festival.fecha_fin))

# EJERCICIO 3.

# 3. artista_top: recibe una lista de tuplas de tipo Festival y devuelve una tupla compuesta por un
# número entero y una cadena de texto, que representan el número de festivales y el nombre del artista
# que haya participado en más festivales que finalmente se han celebrado, respectivamente. (1.75 puntos)

def artista_top(festivales: List[Festival]) -> Tuple[int, str]:
    dicc = defaultdict(int)
    for festival in festivales:
        for artista in festival.artistas:
            if festival.estado == 'CELEBRADO':
                dicc[artista.nombre] += 1
    maximo = max(dicc.items(), key = lambda x:x[1])
    return (maximo[1], maximo[0])

# EJERCICIO 4.

# 4. mes_mayor_beneficio_medio: recibe una lista de tuplas de tipo Festival y devuelve una cadena de
# texto que será el nombre del mes, en español, de aquel que haya obtenido un mayor beneficio medio.
# Es decir, cada festival tiene un beneficio que se calcula a partir de las entradas vendidas menos el caché
# de los artistas. Pues esta función debe calcular el beneficio medio que se ha obtenido cada mes y
# devolver aquel cuyo beneficio haya sido el mayor. Nota: Si hubiera algún festival que se celebra entre
# dos meses, se imputará al mes en el que comienza. Por ejemplo, un festival que comience el 30 de junio
# y acabe el 4 de julio será imputado al mes de junio. (2.25 puntos)

def mes_mayor_beneficio_medio(festivales: List[Festival]) -> str:
    dicc1  = defaultdict(list)
    dicc2 = defaultdict(float)
    for festival in festivales:
        dicc1[festival.fecha_comienzo.month].append(beneficio_medio(festival))
    for mes, lista_beneficio in dicc1.items():
        dicc2[mes] = sum(lista_beneficio) / len(lista_beneficio)
    return meses(max(dicc2.items(), key=lambda x:x[1])[0])

def beneficio_medio(festival: Festival)->float:
    cache_artistas = 0
    for artista in festival.artistas:
        cache_artistas += artista.cache
    return festival.entradas_vendidas * festival.precio - cache_artistas

def meses(n: int) -> str:
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", 
             "Agosto","Septiembre", "Octubre", "Noviembre", "Diciembre"]
    return meses[n - 1]

# EJERCICIO 5.

# 5. artistas_comunes: recibe una lista de tuplas de tipo Festival y dos cadenas de texto festi1 y
# festi2, y devuelve una lista con los nombres de aquellos artistas que se repitan entre festi1 y
# festi2. Nota: se considera que no hay festivales repeidos. (1.75 puntos)    

def artistas_comunes(festivales: List[Festival], festi1: str, festi2:str) -> List[str]:
    pass

# EJERCICIO 6.

# 6. festivales_top_mejor_ratio: Cada festival tiene una duración de entre 2 y 8 días. Implemente una
# función que, recibiendo una lista de tuplas de tipo Festival, y un número n cuyo valor por defecto
# será 3, devuelva un diccionario en el que las claves son las duraciones de los festivales, y los valores
# listas con los nombres de los n festivales de más calidad (ordenados de más a menos calidad). La
# calidad de un festival viene dada por el ratio entre entradas vendidas y número de artistas participantes
# en el festival. Cuanto más alto es este ratio, más calidad tiene el festival. (1.75 punto)

def festivales_top_calidad_por_duracion(festivales: List[Festival], n: int=3) -> Dict[int, List[str]]:
    pass

print(mes_mayor_beneficio_medio(lee_festivales(r"data\festivales.csv")))