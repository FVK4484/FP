from collections import namedtuple
import csv
from datetime import date, datetime

PartidoBasket = namedtuple('PartidoBasket','fecha, equipo1, equipo2, competicion, puntos_eq1, puntos_eq2, faltas_eq1, faltas_eq2')

# EJERCICIO 1.

# 1. parsea_y_suma_resultados: recibe una cadena de texto con los resultados de los cuatro cuartos de 
# un partido, y devuelve una tupla con dos enteros, correspondientes a los puntos totales anotados por 
# el primer y el segundo equipo. Por ejemplo, si recibe la cadena '18-20*15-18*24-17*20-17', debe 
# devolver (77, 72). (0,5 puntos)

def parsea_y_suma_resultados(resultados: str)->tuple[int, int]:
    resultado1, resultado2 = 0, 0
    for resultado in resultados.split("*"):
        puntos1, puntos2 = resultado.split("-")
        resultado1 += int(puntos1)
        resultado2 += int(puntos2)
    return (resultado1, resultado2)

# EJERCICIO 2.

# 2. lee_partidos: recibe una cadena de texto con la ruta de un fichero csv, y devuelve una lista de tuplas 
# PartidoBasket  con  la  información  contenida  en  el  fichero.  Utilice  datetime.strptime(cadena, 
# "%d/%m/%Y").date()  para  parsear  las  fechas.  Use  la  función  parsea_y_suma_resultados  para 
# obtener los puntos totales de los equipos. (1 punto)
            
def lee_partidos(fichero: str)->list[PartidoBasket]:
    lista = []
    with open(fichero, encoding='utf-8')as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for fecha, equipo1, equipo2, competicion, cuartos, faltas_eq1, faltas_eq2 in lector:
            fecha = parsea_fecha(fecha)
            cuartos = parsea_y_suma_resultados(cuartos)
            puntos_eq1 = cuartos[0]
            puntos_eq2 = cuartos[1]
            faltas_eq1 = int(faltas_eq1)
            faltas_eq2 = int(faltas_eq2)
            tupla = PartidoBasket(fecha, equipo1, equipo2, competicion, puntos_eq1, puntos_eq2, faltas_eq1, faltas_eq2)
            lista.append(tupla)
        return lista

def parsea_fecha(fecha: str)-> date:
    return datetime.strptime(fecha, "%d/%m/%Y").date()

# EJERCICIO 3.

# 3. equipo_con_mas_faltas: recibe una lista de tuplas PartidoBasket, y un conjunto de cadenas de texto 
# equipos,  con  valor  por  defecto  None,  y  devuelve  el  nombre  del  equipo  que  acumula  más  faltas 
# personales, de entre los equipos incluidos en el parámetro equipos. Si el parámetro equipos es None, 
# se  devolverá  el  equipo  con  más  faltas  personales  de  entre  todos  los  que  aparezcan  en  la  lista  de 
# partidos recibida. (1,5 puntos)

