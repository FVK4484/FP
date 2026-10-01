from collections import defaultdict
from datetime import date, datetime
from typing import NamedTuple 
import csv
 
Suscripcion = NamedTuple("Suscripcion", 
                         [("nombre", str), 
                          ("dni", str), 
                          ("fecha_inicio", date), 
                          ("fecha_fin", date | None), # Será None si la suscripción sigue activa 
                          ("tipo_plan", str), 
                          ("num_perfiles", int), 
                          ("precio_mensual", float), 
                          ("addons", list[str]) 
                         ])

# EJERCICIO 1.

def lee_suscripciones(ruta_fichero: str) -> list[Suscripcion]:
    lista = []
    with open(ruta_fichero, encoding='utf-8') as f:
        lector  = csv.reader(f)
        next(lector)
        for nombre, dni, fecha_inicio, fecha_fin, tipo_plan, num_perfiles, precio_mensual, addons in lector:
            fecha_inicio = parsea_fecha(fecha_inicio)
            fecha_fin = parsea_fecha(fecha_fin)
            num_perfiles = int(num_perfiles)
            precio_mensual = float(precio_mensual)
            addons = parsea_addons(addons)
            tupla = Suscripcion(nombre, dni, fecha_inicio, fecha_fin, tipo_plan, num_perfiles, precio_mensual, addons)
            lista.append(tupla)
        return lista

def parsea_fecha(fecha: str) -> date:
    res = None
    if len(fecha) > 0:
        res = datetime.strptime(fecha, "%Y-%m-%d").date()
    return res

def parsea_addons(addons: str) -> list[str]:
    lista = []
    addons_nuevos = addons.replace('"', "")
    for addon in addons_nuevos.split(","):
        if len(addons_nuevos) > 0:
            lista.append(addon)
    return lista

# EJERCICIO 2.

def suscripciones_mas_rentables(suscripciones: list[Suscripcion],
                                n: int = 3,
                                tipos_plan: set[str]|None = None) -> list[tuple[str, float]]:
    return sorted(((suscripcion.dni, importe_suscripcion(suscripcion)) for suscripcion in suscripciones if tipos_plan == None or suscripcion.tipo_plan in tipos_plan), key = lambda x:x[1], reverse = True)[:n]

def duracion_dias(suscripcion: Suscripcion)-> int:
    fecha_fin = suscripcion.fecha_fin
    if suscripcion.fecha_fin is None:
        fecha_fin = date.today()
    return (fecha_fin - suscripcion.fecha_inicio).days

def importe_suscripcion(suscripcion: Suscripcion)->float:
    duracion = duracion_dias(suscripcion)
    precio_diario = suscripcion.precio_mensual / 30
    importe_total = precio_diario * duracion
    return importe_total

# EJERCCICIO 3.

# 3. Devuelve una tupla con el tipo de plan y el total de perfiles correspondiente al plan que suma 
# mayor número total de perfiles entre todas las suscripciones cuya  fecha_inicio esté dentro 
# del  rango  indicado  por  los  parámetros  fecha_ini y  fecha_fin.  Ambas  fechas  fecha_ini y 
# fecha_fin están incluidas en el rango. Si fecha_ini es None no se establece un límite inferior; 
# si fecha_fin es None no se establece un límite superior.

def plan_mas_perfiles(suscripciones: list[Suscripcion], 
                           fecha_ini: date|None = None, 
                           fecha_fin: date|None = None) -> tuple[str, int]: 
    # Contamos cuántos perfiles hay en total para cada tipo_plan 
    dicc = defaultdict(int) 
    for suscripcion in suscripciones: 
        # Filtramos por fecha_inicio 
        if (fecha_ini is None or suscripcion.fecha_inicio >= fecha_ini) and (fecha_fin is None or suscripcion.fecha_inicio <= fecha_fin):
            dicc[suscripcion.tipo_plan] += suscripcion.num_perfiles 
    return max(dicc.items(), key=lambda x: x[1])
    