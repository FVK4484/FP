import csv
from collections import defaultdict, namedtuple
from datetime import date, datetime


Ruta = namedtuple('Ruta', 'ciudad_inicio, coordenada, fecha_ruta, km, gasolineras, dificultad, zona_descanso, vel_max, vel_min')
Coordenada = namedtuple('Coordenada', 'latitud, longitud')

# Ejercicio 1.
def lee_rutas(fichero: str) -> list[Ruta]:
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for ciudad_inicio, coordenadas, fecha_ruta, km, gasolineras, dificultad, zona_descanso, vel_max, vel_min in lector:
            ciudad_inicio = ciudad_inicio.strip()
            coordenadas = parsea_coordenadas(coordenadas)
            fecha_ruta = parsea_fecha_ruta(fecha_ruta)
            km = float(km)
            gasolineras = int(gasolineras)
            zona_descanso = parsea_zona_descanso(zona_descanso)
            vel_max = int(vel_max)
            vel_min = int(vel_min)
            tupla = Ruta(ciudad_inicio, coordenadas, fecha_ruta, km, gasolineras, dificultad, zona_descanso, vel_max, vel_min)
            lista.append(tupla)
        return lista
  
def parsea_coordenadas(coordenadas: str) -> Coordenada:
    latitud, longitud = coordenadas.split('/')
    return Coordenada(float(latitud), float(longitud))

def parsea_fecha_ruta(fecha: str) -> date:
    res = 0
    if len(fecha) > 0:
        res = datetime.strptime(fecha, '%m/%d/%Y').date() 
    else:
        res = datetime.today().date()
    return res

def parsea_zona_descanso(zona_descanso: str) -> bool:
    res = False
    if zona_descanso == 'True':
        res = True
    return res

# Ejercicio 2.
def acumular_kms_por_meses(rutas: list[Ruta]) -> dict[int, list[float]]:
    d = agrupar_por_anyos(rutas) 
    res = dict() 
    for anyo, rutas_anyo in d.items(): 
        d_total_meses = acumular_por_meses(rutas_anyo) 
        total_meses_anyo = [d_total_meses.get(mes, 0) for mes in range(1, 13)] 
        res[anyo] = total_meses_anyo 
    lista = sorted(res.items(), key = lambda x:x[1])
    n = dict()
    for elemento in lista:
        n[elemento[0]] = elemento[1]
    return n

def agrupar_por_anyos(rutas: list[Ruta]):
    dicc = defaultdict(list)
    for ruta in rutas:
        dicc[ruta.fecha_ruta.year].append(ruta)
    return dicc

def acumular_por_meses(rutas: list[Ruta]):
    dicc = defaultdict(int)
    for ruta in rutas:
        dicc[ruta.fecha_ruta.month] += ruta.km
    return dicc

# Ejercicio 3.
def diferencias_kms_meses_anyo(rutas): 
    d = acumular_kms_por_meses(rutas) 
    return {anyo: incrementos_kms(kms_meses) for anyo, kms_meses in d.items()} 
 
def incrementos_kms(total_meses): 
    res = [] 
    for i in range(len(total_meses) - 1):         
        res.append(total_meses[i+1] - total_meses[i]) 
    return res

# Ejercicio 4.
def top_rutas_lejanas(rutas: list[Ruta], n: int, c: Coordenada, km_min: int = None) -> list[Ruta]:
    lista_ordenada = sorted(((ruta, distancia_manhattan(c, ruta.coordenada)) for ruta in rutas if km_min is None or km_min < ruta.km), key = lambda x:x[1], reverse = True)[:n]
    return [elemento[0] for elemento in lista_ordenada]

def distancia_manhattan(coordenada1: Coordenada, coordenada2: Coordenada) -> float:
    return abs(coordenada1.latitud - coordenada2.latitud) + abs(coordenada1.longitud - coordenada2.longitud)

# Ejercicio 5.
def agrupa_por_dificultad(rutas): 
    dicc = defaultdict(list)
    for ruta in rutas:
        dicc[ruta.dificultad].append(ruta)
    return dicc
 
def ciudades_top_tiempo_dificultad(rutas, n = 3): 
    rutas = [r for r in rutas if r.zona_descanso] 
    res = agrupa_por_dificultad(rutas) 
    for dificultad, tuplas in res.items(): 
        lista = sorted(tuplas, key = lambda p: p.km/p.vel_min)[:n] 
        res[dificultad] = [l.ciudad_inicio for l in lista] 
    return res