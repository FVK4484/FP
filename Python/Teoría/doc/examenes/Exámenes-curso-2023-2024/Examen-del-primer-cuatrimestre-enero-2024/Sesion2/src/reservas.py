from typing import NamedTuple, List 
from datetime import*
from datetime import date 
import csv

Reserva = NamedTuple("Reserva",  
                     [("nombre", str), 
                      ("dni", str), 
                      ("fecha_entrada", date), 
                      ("fecha_salida", date), 
                      ("tipo_habitacion", str), 
                      ("num_personas", int), 
                      ("precio_noche", float), 
                      ("servicios_adicionales", List[str]) 
                    ])

def lee_reservas(fichero):
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, dni, fecha_entrada, fecha_salida, tipo_habitacion, num_personas, precio_noche, servicios_adicionales in lector:
            fecha_entrada = parsea_fecha(fecha_entrada)
            fecha_salida = parsea_fecha(fecha_salida)
            num_personas = int(num_personas)
            precio_noche = float(precio_noche)
            servicios_adicionales = parsea_lista(servicios_adicionales)
            tupla = Reserva(nombre, dni, fecha_entrada, fecha_salida, tipo_habitacion, num_personas, precio_noche, servicios_adicionales)
            lista.append(tupla)
    return lista

def parsea_fecha(fecha):
    return datetime.strptime(fecha, "%Y-%m-%d").date()

def parsea_lista(lista):
    return lista.split(',') if lista else []

def total_facturado(reservas, ini, fin):
    total = 0
    for reserva in reservas:
        if (ini == None or ini <= reserva.fecha_entrada) and (fin == None or reserva.fecha_entrada <= fin):
            total += reserva.precio_noche * dias(reserva)
    return total

#     return sum(reserva.precio_noche * dias(reserva) 
#                 for reserva in reservas
#                 if (ini == None or ini <= reserva.fecha_entrada) and 
#                    (fin == None or reserva.fecha_entrada <= fin)
#                )
    
def dias(reserva):
    return (reserva.fecha_salida - reserva.fecha_entrada).days

def reserva_mas_larga(reservas, n):
    lista = []
    reservas_ordenadas = sorted(reservas, key = lambda r:(r.fecha_salida - r.fecha_entrada).days, reverse=True)  
    for reserva in reservas_ordenadas[:n]:
        tupla = (reserva.nombre, reserva.fecha_entrada)
        lista.append(tupla)
    return lista
    
