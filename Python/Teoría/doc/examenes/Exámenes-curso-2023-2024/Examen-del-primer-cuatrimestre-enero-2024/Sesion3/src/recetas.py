from typing import NamedTuple, Optional, List, Set, Tuple 
from datetime import date 
from statistics import mean
import csv
from datetime import*
Receta = NamedTuple("Receta",  
                    [("nombre", str), 
                     ("tipo", str), 
                     ("dificultad", str), 
                     ("ingredientes", Optional[List[str]]), 
                     ("tiempo_preparacion", int), 
                     ("calorias", int), 
                     ("fecha_creacion", date), 
                     ("precio_estimado", float) 
                    ]) 

def lee_recetas(fichero):
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, tipo, dificultad, ingredientes, tiempo_preparacion, calorias, fecha_creacion, precio_estimado in lector:
            ingredientes = parsea_ingredientes(ingredientes)
            tiempo_preparacion = int(tiempo_preparacion)
            calorias = int(calorias)
            fecha_creacion = parsea_fecha(fecha_creacion)
            precio_estimado = float(precio_estimado)
            tupla = Receta(nombre, tipo, dificultad, ingredientes, tiempo_preparacion, calorias, fecha_creacion, precio_estimado)
            lista.append(tupla)
    return lista

def parsea_ingredientes(ingredientes):
    return ingredientes.split(',') if ingredientes else []

def parsea_fecha(fecha):
    return datetime.strptime(fecha, '%Y-%m-%d').date()

def receta_mas_barata(recetas, tipos, n):
    recetas = sorted((receta for receta in recetas if receta.tipo in tipos),
                     key = lambda receta:receta.calorias)[:n]
    return min(recetas, key = lambda receta: receta.precio_estimado)

def obten_ingredientes(recetas, mes1, mes2):
    res = set()
    return (res.union(receta.ingredientes)
            for receta in recetas
            if (mes1 is None or receta.fecha_creacion.month >= mes1) and
               (mes2 is None or mes2 > receta.fecha_creacion.month)
            )

def recetas_con_precio_menor_promedio(recetas: List[Receta], n: int) -> List[Tuple[str, int]]:
    precio_total = 0
    cont = 0
    for receta in recetas:
        precio_total += receta.precio_estimado
        cont += 1
        media = precio_total / cont
    return sorted(((receta.nombre, receta.calorias) for receta in recetas if receta.precio_estimado < media), key = lambda x:x[1])[:n]