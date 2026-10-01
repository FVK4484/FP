from typing import NamedTuple 
from datetime import date, datetime
from collections import defaultdict
import csv
from statistics import mean

 
Mision = NamedTuple("Mision", [ 
    ("comandante", str), 
    ("sistema", str), 
    ("controlado", bool), 
    ("fecha_inicio", date), 
    ("fecha_fin", date | None), 
    ("tipo_mision", str), 
    ("num_unidades", int), 
    ("coste_mensual", float), 
    ("recursos", list[str]) 
])

# EJERCICIO 1

def lee_misiones(ruta_fichero: str) -> list[Mision]:
    lista = []
    with open(ruta_fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for comandante, sistema, controlado, fecha_inicio, fecha_fin, tipo_mision, num_unidades, coste_mensual, recursos in lector:
            controlado = parsea_controlado(controlado)
            fecha_inicio = parsea_fecha(fecha_inicio)
            fecha_fin = parsea_fecha(fecha_fin)
            num_unidades = int(num_unidades)
            coste_mensual = float(coste_mensual)
            recursos = parsea_recursos(recursos)
            tupla = Mision(comandante, sistema, controlado, fecha_inicio, fecha_fin, tipo_mision, num_unidades, coste_mensual, recursos)
            lista.append(tupla)
    return lista

def parsea_controlado(controlado: str) -> bool:
    res = False
    if controlado == 'Sí':
        res = True
    return res

def parsea_fecha(fecha: str | None) -> date:
    res = None
    if len(fecha) > 0:
        res = datetime.strptime(fecha, "%Y-%m-%d").date()
    return res

def parsea_recursos(recursos: str) -> list[str]:
    recurso = []
    if len(recursos) > 0:
        recurso = recursos.split('#')
    return recurso

# EJERCICIO 2

def comandante_ocioso(misiones: list[Mision]) -> str:
    dicc_misiones = misiones_por_comandante(misiones)
    comandante_mas_vago = None
    maximo_tiempo_libre = -1
    for comandante, lista_de_sus_misiones in dicc_misiones.items():  
        descanso_comandante = calcular_maximo_descanso(lista_de_sus_misiones)
        if descanso_comandante > maximo_tiempo_libre:
            maximo_tiempo_libre = descanso_comandante
            comandante_mas_vago = comandante          
    return comandante_mas_vago

def misiones_por_comandante(misiones: list[Mision]) -> dict[str, list[int]]:
    dicc = defaultdict(list)
    for mision in misiones:
            dicc[mision.comandante].append(mision)
    return dicc

def calcular_maximo_descanso(misiones: list[Mision]) -> int:
    misiones_ordenadas = sorted(misiones, key=lambda x: x.fecha_inicio)
    max_dias = 0
    for i in range(1, len(misiones_ordenadas)):
        mision_actual = misiones_ordenadas[i]
        mision_anterior = misiones_ordenadas[i-1]
        if mision_anterior.fecha_fin is not None:
            delta = mision_actual.fecha_inicio - mision_anterior.fecha_fin
            dias_libres = delta.days
            if dias_libres > max_dias:
                max_dias = dias_libres            
    return max_dias

# EJERCICIO 3

def comandante_mas_activo_por_mes(misiones: list[Mision]) -> dict[tuple[int, int], str]: 
    dicc = defaultdict(list)
    for mision in misiones:
        dicc[mision.fecha_inicio.year, mision.fecha_inicio.month].append(mision.comandante)
    return dict(sorted(dicc.items(), key = lambda x:x[0]))

# EJERCICIO 4

def coste_de_recursos(misiones: list[Mision], n: int = 3) -> list[tuple[str, float]]:
    dicc = defaultdict(list)
    for mision in misiones:
        for recurso in mision.recursos:
            dicc[recurso].append(mision.coste_mensual)
    return sorted(((recurso, mean(lista_coste_mensual)) for recurso, lista_coste_mensual in dicc.items()), key = lambda x:x[1], reverse = True)[:n]

print(coste_de_recursos(lee_misiones(r'FP_25_26\doc\examenes\Exámenes-curso-2024-2025\Examen-de-la-primera-convocatoria-junio-2025\data\misiones.csv')))