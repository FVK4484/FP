from collections import Counter, defaultdict, namedtuple
import csv
from datetime import date, datetime

Partido = namedtuple('Partido', 'fecha, equipoloc, equipovis, ganador, golesloc, golesvis, competicion, espectadores') 


# EJERCICIO 1
def lee_resultados(ruta_fichero: str) -> list[Partido]:
    lista = []
    with open(ruta_fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ";")
        next(lector)
        for fecha, partido, resultado, marcador, competicion, espectadores in lector:
            fecha = parsea_fecha(fecha)
            equipoloc = parsea_partido(partido)[0].strip()
            equipovis = parsea_partido(partido)[1].strip()
            ganador = resultado.strip()
            golesloc = int(parsea_marcador(marcador)[0])
            golesvis = int(parsea_marcador(marcador)[1])
            competicion = str(competicion).strip()
            espectadores = int(espectadores)
            tupla = Partido(fecha, equipoloc, equipovis, ganador, golesloc, golesvis, competicion, espectadores)
            lista.append(tupla)
        return lista


def parsea_fecha(fecha: str) -> date:
    return datetime.strptime(fecha, "%d/%m/%Y").date()

def parsea_partido(cadena: str) -> list[str]:
    return cadena.strip().split(" v ")

def parsea_marcador(cadena: str) -> list[str]:
    return cadena.split("-")

# EJERCICIO 2
def selecciones_enfrentadas_israel(partidos: list[Partido], n: int = 3) -> list[str]:
    dicc = defaultdict(list)
    for partido in partidos:
        if partido.equipoloc != "Israel":
            dicc[partido.competicion].append(partido.equipoloc)
        else:
            dicc[partido.competicion].append(partido.equipovis)
    lista = sorted(dicc.items(), key = lambda x:len(x[1]), reverse = True)[:n]
    lista2 = []
    for elemento1, elemento2 in lista:
        lista2.extend(elemento2)
    return sorted(set(lista2))

# EJERCICIO 3
def lista_diferencias_goles(partidos: list[Partido], fecha1: date, fecha2: date) -> list[int]:
    pass

# EJERCICIO 4
def partidos_por_mes(partidos: list[Partido]) -> list[tuple[int, int]]:
    dicc = defaultdict(int)
    for partido in partidos:
        dicc[partido.fecha.month] += 1
    return sorted(dicc.items())

# EJERCICIO 5
def partidos_mensuales_por_anyo(partidos: list[Partido]) -> dict[int, list[int, int]]:
    dicc1 = defaultdict(list)
    dicc2 = defaultdict(list)
    for partido in partidos:
        dicc1[partido.fecha.year].append(partido)
    for año, lista_partidos in dicc1.items():
        dicc2[año] += (partidos_por_mes(lista_partidos))
    return dicc2
        
print(partidos_mensuales_por_anyo(lee_resultados(r"doc\examenes\Exámenes-curso-2020-2021\Primer-examen-práctico-febrero-2021\Sesion4\data\resultadosIsrael.csv")))

