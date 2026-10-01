import csv
from collections import namedtuple
from statistics import mean
from collections import defaultdict

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')

def lee_frecuencias_nombres(fichero):
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for año,nombre,frecuencia,genero in lector:
            año = int(año)
            nombre = nombre.strip()
            frecuencia = int(frecuencia)
            genero = genero.strip()
            tupla = FrecuenciaNombre(año, nombre, frecuencia, genero)
            lista.append(tupla)
    return lista

def filtrar_por_genero(nombres: list[FrecuenciaNombre], genero: str) -> list[FrecuenciaNombre]:
    # lista = []
    # for nombre in nombres:
    #     if genero.strip().lower() == nombre.genero.lower():
    #         lista.append(nombre)
    # return lista     
    return [nombre for nombre in nombres if genero.strip().lower() == nombre.genero.lower()]

def calcular_nombres(nombres, genero = None):
    # conjunto = set()
    # for nombre in nombres:
    #     if genero == None or nombre.genero.lower() == genero.strip().lower():
    #         conjunto.add(nombre.nombre)
    # return conjunto
    return set(nombre.nombre for nombre in nombres 
               if genero is None or nombre.genero == genero)

def calcular_top_nombres_de_año(nombres, año, genero = None, limite = 10):
    # lista = []
    # for nombre in nombres:
    #     if nombre.año == año and (genero is None or nombre.genero == genero):
    #         lista.append((nombre.nombre, nombre.frecuencia))
    # return sorted(lista, key = lambda x: x[1], reverse = True)[:limite]
    return sorted([(nombre.nombre, nombre.frecuencia) for nombre in nombres 
         if nombre.año == año and (genero is None or nombre.genero == genero)], 
         key = lambda x: x[1], reverse = True)[:limite]

def calcular_nombres_ambos_generos(nombres):
    # conjunto1 = set()
    # conjunto2 = set()
    # for nombre in nombres:
    #     if nombre.genero == 'Hombre':
    #         conjunto1.add(nombre.nombre)
    #     else:
    #         conjunto2.add(nombre.nombre)
    # return conjunto1.intersection(conjunto2)
    return {nombre.nombre for nombre in nombres if nombre.genero == 'Hombre'}.intersection({nombre.nombre for nombre in nombres if nombre.genero == 'Mujer'})

def calcular_nombres_compuestos(nombres, genero = None):
    # conjunto = set()
    # for nombre in nombres:
    #     if (' ' in nombre.nombre)  and (genero is None or nombre.genero.strip().lower() == genero):
    #         conjunto.add(nombre.nombre)
    # return conjunto
    return {nombre.nombre for nombre in nombres if (' ' in nombre.nombre) and (genero is None or nombre.genero == genero)}

def calcular_frecuencia_media_nombres_año(nombres, nombre_param, año_ini, año_fin):
    frecuencias = [nombre.frecuencia for nombre in nombres if nombre_param == nombre.nombre and año_ini <= nombre.año < año_fin]
    return mean(frecuencias or [0])

def calcular_nombre_mas_frecuente_año_genero(nombres, año, genero):
    return [nombre.nombre for nombre in nombres 
            if nombre.frecuencia == max(nombre.frecuencia for nombre in nombres if nombre.año == año and genero == nombre.genero)]

def calcular_año_mas_frecuencia_nombre(nombres, nombre_param):
    return [nombre.año for nombre in nombres 
            if nombre.frecuencia == max(nombre.frecuencia for nombre in nombres if nombre.nombre == nombre_param)]

def calcular_nombres_mas_frecuentes(nombres, genero, decada, n = 5):
    # lista = []
    # for nombre in nombres:
    #     if nombre.genero == genero and nombre.año % 100 == decada:
    #         lista.append(nombre)
    # lista_ordenada = sorted(lista, key = lambda x: x[2], reverse = True)
    # return lista_ordenada[:n]
    return sorted((nombre for nombre in nombres if nombre.genero == genero and nombre.año % 100 == decada), key = lambda x: x[2], reverse = True)[:n]

def calcular_año_frecuencia_por_nombre(nombres, genero):
    # dicc = {}
    # for nombre in nombres:
    #     if nombre.genero == genero:
    #         if nombre.nombre not in dicc:
    #             dicc[nombre.nombre] = []
    #         dicc[nombre.nombre].append((nombre.año, nombre.frecuencia))
    # return dicc
    dicc = defaultdict(list)
    [dicc[nombre.nombre].append((nombre.año, nombre.frecuencia)) for nombre in nombres if nombre.genero == genero]
    return dict(dicc)

def calcular_nombre_mas_frecuente_por_año(nombres, genero):
    # resultado = [] 
    # años_unicos = sorted(set(n.año for n in nombres if n.genero == genero))
    # for año in años_unicos:
    #     nombres_en_año = [n for n in nombres if n.año == año and n.genero == genero]
    #     mayor = max(nombres_en_año, key=lambda x: x.frecuencia)
    #     resultado.append((año, mayor.nombre, mayor.frecuencia)) 
    # return sorted(resultado)
    return sorted([(año, 
                    max([n for n in nombres if n.genero == genero and n.año == año], key=lambda x: x.frecuencia).nombre, 
                    max([n for n in nombres if n.genero == genero and n.año == año], key=lambda x: x.frecuencia).frecuencia) 
                    for año in sorted({n.año for n in nombres if n.genero == genero})], key=lambda x: x[0])
