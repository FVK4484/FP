from typing import NamedTuple 
from datetime import*
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

# Ejercicio 1
def lee_suscripciones(ruta_fichero: str) -> list[Suscripcion]: 
    suscripciones = [] 
    with open(ruta_fichero, "r", encoding="utf-8") as f: 
        lector = csv.reader(f) 
        next(lector) 
        for nombre, dni, fecha_inicio, fecha_fin, tipo_plan, num_perfiles, precio_mensual, addons in lector: 
            fecha_inicio = parsea_fecha(fecha_inicio) 
            fecha_fin = parsea_fecha(fecha_fin) 
            num_perfiles = int(num_perfiles) 
            precio_mensual = float(precio_mensual) 
            addons = parsea_addons(addons) 
            sus = Suscripcion(nombre, dni, fecha_inicio, fecha_fin, tipo_plan,  
                       num_perfiles, precio_mensual, addons) 
            suscripciones.append(sus) 
    return suscripciones 
 
def parsea_fecha(fecha_str: str) -> date: 
    res = None 
    if len(fecha_str) > 0: 
        res = datetime.strptime(fecha_str, "%Y-%m-%d").date() 
    return res 
 
def parsea_addons(addons_str: str) -> list[str]: 
    res = [] 
    if len(addons_str) > 0: 
        res = addons_str.split(",") 
    return res

# Ejercicio 2
def suscripciones_mas_rentables(suscripciones: list[Suscripcion], 
                         n: int = 3, 
                         tipos_plan: set[str]|None = None) -> list[tuple[str, float]]: 
    return sorted( 
        ((s.dni, importe_suscripcion(s)) 
                for s in suscripciones 
                    if tipos_plan == None or s.tipo_plan in tipos_plan), 
         key = lambda t: t[1], reverse = True)[:n] 

def duracion_dias(sus: Suscripcion) -> int: 
    fecha_fin = sus.fecha_fin 
    if sus.fecha_fin is None: 
        # fecha_fin = date(2025, 1, 15) # Para obtener el test del día del examen 
        fecha_fin = date.today() 
    return (fecha_fin - sus.fecha_inicio).days 
 
def importe_suscripcion(sus: Suscripcion) -> float: 
    duracion = duracion_dias(sus) 
 
    precio_diario = sus.precio_mensual / 30.0 
    return duracion * precio_diario 

# def suscripcion_importe_total_por_tipos_plan(suscripciones, tipos_plan):
#     return sum(suscripcion.precio_mensual for suscripcion in suscripciones if tipos_plan == [] or suscripcion.tipo_plan in tipos_plan)
# def suscripciones_mas_rentables(suscripciones, n, tipos_plan):
#     return sorted((suscripcion_importe_total_por_tipos_plan(suscripciones, tipos_plan), suscripcion.dni) for suscripcion in suscripciones if suscripcion.tipo_plan in tipos_plan)[:n]