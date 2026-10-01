import csv
from datetime import datetime
from typing import NamedTuple 
 
Piloto=NamedTuple("Piloto", [("nombre", str),("escuderia", str)]) 
 
CarreraFP=NamedTuple("CarreraFP",[ 
        ("fecha_hora",datetime),  
        ("circuito",str),                     
        ("pais",str),  
        ("seco",bool), # True si el asfalto estuvo seco, False si estuvo mojado 
        ("tiempo",float),  
        ("podio", list[Piloto])])

# EJERCICIO1
def lee_carreras(filename: str) -> list[CarreraFP]:
    lista = []
    with open(filename, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for fecha_hora, circuito, pais, asfalto, tiempo, nombre_ganador, marca_ganador, nombre_segundo_clasificado, marca_segundo_clasificado, nombre_tercer_clasificado, marca_tercer_clasificado in lector:
            fecha_hora = parsea_fecha(fecha_hora)
            seco = parsea_asfalto(asfalto) 
            tiempo = float(tiempo)
            podio = [parsea_podio(nombre_ganador, marca_ganador),
                     parsea_podio(nombre_segundo_clasificado, marca_segundo_clasificado),
                     parsea_podio(nombre_tercer_clasificado, marca_tercer_clasificado)]
            tupla = CarreraFP(fecha_hora, circuito, pais, seco, tiempo, podio)
            lista.append(tupla)
        return lista
            
def parsea_fecha(fecha: str) -> datetime:
    return datetime.strptime(fecha, "%Y-%m-%d %H:%M")

def parsea_asfalto(asfalto: str) -> bool:
    res = False
    if asfalto == "Seco":
        res = True
    return res

def parsea_podio(nombre: str, escuderia: str) -> Piloto:
    tupla = Piloto(nombre, escuderia)
    return tupla

# print(lee_carreras(r"FP_25_26\doc\examenes\Exámenes-curso-2024-2025\Examen-del-primer-cuatrimestre-enero-2025\Sesion1\data\mundial_motofp.csv"))