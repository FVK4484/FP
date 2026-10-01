import csv
from datetime import datetime, date
from typing import NamedTuple

Pelicula = NamedTuple(
    "Pelicula",
    [("fecha_estreno", date), 
    ("titulo", str), 
    ("director", str), 
    ("generos",list[str]),
    ("duracion", int),
    ("presupuesto", int), 
    ("recaudacion", int), 
    ("reparto", list[str])
    ]
)

def lee_peliculiculas(fichero: str) -> list[Pelicula]:
    with open(fichero, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        peliculas = []
        for fecha_estreno, titulo, director, generos, duracion, \
        presupuesto, recaudacion, reparto in lector:
            
            fecha_estreno = parsea_fecha(fecha_estreno)
            titulo = titulo.strip()
            director = director.strip()
            generos = parsea_lista(generos)
            duracion = int(duracion)
            presupuesto = int(presupuesto)
            recaudacion = int(recaudacion)
            reparto = parsea_lista(reparto)

            tupla = Pelicula(fecha_estreno, titulo, director, 
                             generos, duracion, presupuesto, 
                             recaudacion, reparto)
            peliculas.append(tupla)   

    return peliculas

def parsea_fecha(cadena: str) -> date:
    return datetime.strptime(cadena, "%d/%m/%Y").date()

def parsea_lista(cadena: str, delimiter: str = ",") -> list[str]:
    lista = cadena.split(delimiter)
    res = []
    for c in lista:
        res.append(c.strip())
    return res

def pelicula_mas_ganancias (peliculas: list[Pelicula],
    genero: str | None = None) -> tuple[str, int]:
    # Filtrar por genero
    peliculas_genero = []
    for p in peliculas:
        if genero in p.generos:
            peliculas_genero.append((p.titulo, p.recaudacion - p.presupuesto))
    # Obtener el máximo
    return max(peliculas_genero, key=lambda t: t[1])

def media_presupuesto_por_genero (peliculas: list[Pelicula]) \
     -> dict[str, float]:
    # Crear diccionario de presupuestos por genero
    dic = media_presupuesto_por_genero(peliculas)

    # Crear diccionario de medias de presupuestos por genero
    res = dict()
    for genero, lista_presupuesto in dic.items():
        res[genero] = sum(lista_presupuesto) / len(lista_presupuesto)
    return res

def presupuesto_por_genero (peliculas: list[Pelicula]) \
     -> dict[str, list[int]]:
    res = dict()
    for p in peliculas:
        generos = p.generos
        for g in generos:
            if g not in res:
                res[g] = (p.presupuesto)
            else:
                res[g].append[p.presupuesto]
    return res

def peliculas_por_actor (peliculas: list[Pelicula], año_inicial: int | None = None, 
                         año_final: int | None = None) -> dict[str, list[int]]:
    res = dict()
    for p in peliculas:
        if año_inicial is not None and p.fecha_estreno.year < año_inicial:
            continue
        if año_final is not None and p.fecha_estreno.year > año_final:
            continue
        for g in p.generos:
            if g not in res:
                res[g] = [p.recaudacion - p.presupuesto]
            else:
                res[g].append(p.recaudacion - p.presupuesto)
    return res
