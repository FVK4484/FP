from collections import defaultdict, namedtuple
import csv
from datetime import date, datetime, timedelta


Reparacion = namedtuple('Reparacion', 'numero_ref,centro,fecha_entrada,fecha_reparacion,numero_serie,tipo,descripcion_problema,fecha_compra,precio_reparacion')

# Ejercicio 1.
def lee_reparaciones(fichero: str) -> list[Reparacion]:
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for numero_ref,centro,fecha_entrada,fecha_reparacion,numero_serie,tipo,descripcion_problema,fecha_compra,precio_reparacion in lector:
            fecha_entrada = parsea_fecha(fecha_entrada)
            fecha_reparacion = parsea_fecha(fecha_reparacion)
            fecha_compra = parsea_fecha(fecha_compra)
            precio_reparacion = float(precio_reparacion)
            tupla = Reparacion(numero_ref,centro,fecha_entrada,fecha_reparacion,numero_serie,tipo,descripcion_problema,fecha_compra,precio_reparacion)
            lista.append(tupla)
        return lista

def parsea_fecha(fecha: str) -> date: 
    return datetime.strptime(fecha, '%d/%m/%Y').date()

# Ejercicio 2.
def calcula_recaudacion(reparaciones: list[Reparacion], centro: str, tipo: str = None) -> float:
    return sum(reparacion.precio_reparacion 
               for reparacion in reparaciones 
                    if (reparacion.centro == centro) 
                    and (tipo is None or tipo == reparacion.tipo) 
                    and (no_esta_en_garantia(reparacion)))

def no_esta_en_garantia(reparacion: Reparacion) -> bool:
    res = False
    if (reparacion.fecha_compra >= date(2022, 1, 1)) and ((reparacion.fecha_entrada - reparacion.fecha_compra).days > (365*3)):
        res = True
    elif (reparacion.fecha_compra < date(2022, 1, 1)) and ((reparacion.fecha_entrada - reparacion.fecha_compra).days > (365*2)):
        res = True
    else:
        res = False
    return res

# Ejercicio 3.
def reparaciones_mas_largas(reparaciones: list[Reparacion], anyo: int, n: int, centro: str = None) -> list[Reparacion]:
    return sorted((((reparacion.numero_ref, (reparacion.fecha_reparacion - reparacion.fecha_entrada).days)) 
                   for reparacion in reparaciones 
                        if (reparacion.fecha_reparacion.year == anyo) 
                            and (centro is None or reparacion.centro == centro)), 
                            key = lambda x:x[1], 
                            reverse = True)[:n]
    # lista = []
    # for reparacion in reparaciones:
    #     if (reparacion.fecha_reparacion.year == anyo) and (centro is None or reparacion.centro == centro):
    #         dias = (reparacion.fecha_reparacion - reparacion.fecha_entrada).days
    #         lista.append((reparacion.numero_ref, dias))

    # return sorted(lista, key = lambda x:x[1], reverse=True)[:n]

# Ejercicio 4.
def centro_mas_rapido(reparaciones: list[Reparacion], centros: set[str]) -> str:
    dicc = defaultdict(list)
    for reparacion in reparaciones:
        if reparacion.centro in centros:
            dicc[reparacion.centro].append((reparacion.fecha_reparacion - reparacion.fecha_entrada).days)
    dicc_nuevo = defaultdict(int)
    for centro, lista_dias in dicc.items():
        dicc_nuevo[centro] = sum(lista_dias) / len(lista_dias)
    return min(dicc_nuevo.items(), key = lambda x:x[1])[0]

# Ejercicio 5.
def centros_experimentados_en(reparaciones: list[Reparacion], palabras_clave: set[str]) ->  dict[str, list[str]]:
    dicc = defaultdict(set)
    dicc2 = defaultdict(list)
    for reparacion in reparaciones:
        for palabra in palabras_clave:
            if reparaciones_relacionadas(reparacion, palabra):
                dicc[palabra].add(reparacion.centro)
    for palabra, conjunto_centros in dicc.items():
        for centro in conjunto_centros:
            dicc2[palabra].append(centro)
    return dict(dicc2)

def reparaciones_relacionadas(reparacion: Reparacion, palabra: str) -> bool:
    res = False
    lista = []
    for palabra_new in (reparacion.descripcion_problema.split(' ')):
        lista.append(palabra_new.lower())
    if palabra.lower() in lista:
        res = True
    return res
 





