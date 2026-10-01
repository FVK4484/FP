from collections import defaultdict
import csv
from typing import Dict, List, NamedTuple, Optional, Set, Tuple 
from datetime import date, datetime 
Medallas = NamedTuple('Medallas', [('oro', int), ( 'plata', int),  ('bronce', int)]) 
Registro = NamedTuple('Registro', [ 
   ('ciudad_olimpica', str),  
   ('fecha_inicio', date),  
   ('pais', str),  
   ('deporte', str), 
   ('num_participantes', int),  
   ('genero', str),  
   ('medallas', Medallas),   
   ('sede', bool)])

# Ejercicio 1.
def lee_registros_olimpiadas(filename: str) -> List[Registro]:
    lista = []
    with open(filename, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for ciudad_olimpica, fecha_inicio, pais, deporte, num_participantes, genero, medallas, sede in lector:
            fecha_inicio = parsea_fecha(fecha_inicio)
            num_participantes = int(num_participantes)
            medallas = parsea_medallas(medallas)
            sede = parsea_sede(sede)
            tupla = Registro(ciudad_olimpica, fecha_inicio, pais, deporte, num_participantes, genero, medallas, sede)
            lista.append(tupla)
        return lista

def parsea_fecha(fecha: str) -> date:
    return datetime.strptime(fecha, '%Y-%m-%d').date()

def parsea_medallas(medallas: str) -> Medallas:
    oro, plata, bronce = medallas.split('-')
    return Medallas(int(oro), int(plata), int(bronce))

def parsea_sede(sede: str) -> bool:
    res = False
    if (sede == 'SI'):
        res = True
    return res

# Ejercicio 2.
def deportes_ambos_generos(registros: List[Registro], anyo: int) -> Set[str]:
    filtrado = [registro for registro in registros if registro.fecha_inicio.year == anyo]
    conjunto_hombres = set(registro.deporte for registro in filtrado if registro.genero == 'HOMBRE')
    conjunto_mujeres = set(registro.deporte for registro in filtrado if registro.genero == 'MUJER')
    return conjunto_hombres.intersection(conjunto_mujeres)

# Ejercicio 3.
def deportes_mas_frecuentes(registros: List[Registro], 
                            n: int, 
                            genero: str) ->  Dict[str, List[Tuple[str, int]]]:
    dicc = defaultdict(int)
    for registro in registros:
        if registro.genero == genero:
            dicc[registro.deporte] += 1
    return sorted(dicc.items(), key = lambda x:x[1], reverse = True)[:n]

# Ejercicio 4.
def deporte_con_mas_paises_distintos_con_oro(registros: List[Registro], 
                                             genero: Optional[str] = None) -> str:
    filtrado = [registro for registro in registros if genero is None or genero == registro.genero]
    dicc = defaultdict(set)
    for registro in filtrado:
        if (registro.medallas.oro > 0):
            dicc[registro.deporte].add(registro.pais)
    return max(dicc.items(), key = lambda x:len(x[1]))[0] 

# Ejercicio 5.
def deportes_mas_participantes_de_genero_por_juego(registros: List[Registro], pais: str, genero: str) -> Dict[str, List[Tuple[str, int]]]:
    pass


    




    