from typing import  NamedTuple, Set
from collections import defaultdict
import csv

RegistroExtranjeria = NamedTuple(
    "RegistroExtranjeria", 
            [("distrito",str),
             ("seccion", str),
             ("barrio", str),
             ("pais",str),
             ("hombres", int),
             ("mujeres", int)
            ]
)

# EJERCICIO 1
def lee_datos_extranjeria(ruta_fichero: str) -> list[RegistroExtranjeria]:
    lista = []
    with open(ruta_fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for distrito, seccion, barrio, pais, hombres, mujeres in lector:
            barrio = str(barrio).strip().upper()
            pais = str(pais).strip().upper()
            hombres = int(hombres)
            mujeres = int(mujeres)
            tupla = RegistroExtranjeria(distrito, seccion, barrio, pais, hombres, mujeres)
            lista.append(tupla)
        return lista
    
# EJERCICIO 2
def numero_nacionalidades_distintas(registros: list[RegistroExtranjeria]) -> int:
    lista = []
    for registro in registros:
        if registro.pais not in lista:
            lista.append(registro.pais)
    return len(lista)
    ###########################################
    # dicc = defaultdict(int)
    # for registro in registros:
    #     dicc[registro.pais] += 1
    # return len(dicc.keys())
    ###########################################

# EJERCICIO 3
def secciones_distritos_con_extranjeros_nacionalidades(registros: list[RegistroExtranjeria], paises: Set) -> list[tuple[str, str]]:
    return sorted(set((registro.distrito, registro.seccion) for registro in registros if registro.pais in paises), key = lambda x:x[0])
    # lista = []
    # for registro in registros:
    #     if registro.pais in paises:
    #         lista.append((registro.distrito, registro.seccion))
    # return set(lista)

# EJERCICIO 4
def total_extranjeros_por_pais(registros: list[RegistroExtranjeria]) -> dict[str : int]:
    dicc = defaultdict(int)
    for registro in registros:
        dicc[registro.pais] += registro.hombres + registro.mujeres
    return dicc


# EJERCICIO 5
def top_n_extranjeria(registros: list[RegistroExtranjeria], n: int | int = 3) -> list[tuple[str, int]]:
    dicc = defaultdict(int)
    for registro in registros:
        dicc[registro.pais] += registro.hombres + registro.mujeres
    return sorted((dicc.items()), key = lambda x:x[1], reverse = True)[:5]

# EJERCICIO 6
def barrio_mas_multicultural(registros: list[RegistroExtranjeria]) -> str:
    dicc = defaultdict(list)
    dicc2 = defaultdict(int)
    for registro in registros:
        dicc[registro.barrio].append(registro.pais)
    for barrio, paises in dicc.items():
        dicc2[barrio] = len(paises)
    return max(dicc2.items(), key = lambda x:x[1])[0]

# EJERCICIO 7
def barrio_con_mas_extranjeros(registros: list[RegistroExtranjeria], tipo = None) -> str:
    dicc = defaultdict(int)
    for registro in registros:
        if tipo == None:
            dicc[registro.barrio] += registro.hombres + registro.mujeres
        elif tipo == 'Mujeres':
            dicc[registro.barrio] += registro.mujeres
        else:
            dicc[registro.barrio] += registro.hombres 
    return max(dicc.items(), key = lambda x:x[1])[0]

# EJERCICIO 8
def pais_mas_representado_por_distrito(registros: list[RegistroExtranjeria]) -> dict[str : str]:

# Agregación 
    dicc = defaultdict(list)
    result = defaultdict(str)
    for registro in registros:
        dicc[registro.distrito].append(registro)

# Transformación
    for distrito, lista_registros in dicc.items():
        result[distrito] = pais_mas_representado(lista_registros)
    return result

def calcula_suma_extranjeros(lista_registros):
    result=0 
    for r in lista_registros:
        result += r.hombres + r.mujeres
    return result

def pais_mas_representado(registros):
    dicc = defaultdict(list)
    result = defaultdict()
    for registro in registros:
        dicc[registro.distrito].append(registro)
    
    for pais, lista_registros in dicc.items():
        result[pais] = calcula_suma_extranjeros(lista_registros)
    return max(result.keys(), key = lambda pais:result[pais])
    