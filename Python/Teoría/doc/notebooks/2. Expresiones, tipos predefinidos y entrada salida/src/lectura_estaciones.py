import csv
from collections import namedtuple

Estaciones = namedtuple("Estaciones", "name, slots, empty_slots, free_bikes, latitude, longitude")

def lee_estaciones(fichero):
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for name, slots, empty_slots, free_bikes, latitude, longitude in lector:
            slots = int(slots)
            empty_slots = int(empty_slots)
            free_bikes = int(free_bikes)
            latitude = float(latitude)
            longitude = float(longitude)
            # tupla = Estaciones(name, slots, empty_slots, free_bikes, latitude, longitude)
            # lista.appen(tupla)
            lista.append(Estaciones(name, slots, empty_slots, free_bikes, latitude, longitude))
        return lista

