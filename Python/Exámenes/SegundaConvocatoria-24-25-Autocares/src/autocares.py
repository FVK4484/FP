from collections import defaultdict
from statistics import mean
from typing import NamedTuple 
from datetime import date, datetime 
import csv

Viaje = NamedTuple("Viaje",      
       [("inicio", datetime),   #fecha y hora de inicio del viaje. 
        ("fin", datetime),      #fecha y hora de fin del viaje. 
        ("kms", float),         #kilometros recorridos. 
        ("num_viajeros", int)]) #número de viajeros. 
 
Autocar = NamedTuple("Autocar",      
      [("matricula", str),        #matrícula del autocar.  
       ("marca", str),            #marca del autocar. 
       ("plazas", int),           #número de plazas para viajeros. 
       ("tipo", str),             #tipo del autocar. 
       ("precio",int),            #precio que cuesta alquilarlo diariamente. 
       ("viajes", list[Viaje])])  #Lista con los viajes realizados.

# EJERCICIO 1.

def lee_autocares(ruta:str)->list[Autocar]:
  lista = []
  with open(ruta, encoding='utf-8') as f:
    lector = csv.reader(f)
    next(lector)
    for matricula, marca, plazas, tipo, precio, viajes in lector:
      plazas = int(plazas)
      precio = int(precio)
      viajes = parsea_viajes(viajes)
      tupla = Autocar(matricula, marca, plazas, tipo, precio, viajes)
      lista.append(tupla)
    return lista

def parsea_viajes(viajes_str: str) -> list[Viaje]: 
  res = list() 
  viajes_str = viajes_str.replace("[","").replace("]","") 
  if len(viajes_str) > 0: 
    for viaje in viajes_str.split("*"): 
      res.append(parsea_viaje(viaje)) 
  return res

def parsea_viaje(viaje_str: str) -> Viaje: 
  inicio, fin, kms, num_viajeros = viaje_str.split(";") 
  inicio = datetime.strptime(inicio, "%d/%m/%Y %H:%M") 
  fin = datetime.strptime(fin, "%d/%m/%Y %H:%M") 
  kms = float(kms) 
  num_viajeros = int(num_viajeros) 
  return Viaje(inicio, fin, kms, num_viajeros)

# EJERCICIO 2.

# 2. viaje_mas_kilometros:  dada  una  lista  de  tuplas  autocares  de  tipo Autocar  y  un  conjunto  de  marcas  de 
# autocares,  devuelve  una  tupla  formada  por  la  matrícula  y  el  viaje  con  más  kilómetros  recorrido  entre  los 
# autocares  cuya  marca  sea  del  conjunto  de  marcas  dado.  El  conjunto  de  marcas  tomará  el  valor  por  defecto 
# None, en cuyo caso se analizarán los viajes de todos los autocares de fichero.

def viaje_mas_kilometros(autocares:list[Autocar], marcas:set[str]|None=None)-> tuple[str, Viaje]:
  return max(((autocar.matricula, viaje) 
              for autocar in autocares 
              if marcas is None or autocar.marca in marcas 
              for viaje in autocar.viajes), key = lambda x:x[1].kms)

# EJERCICIO 3.

# 3. autocar_mayor_beneficio: dada una lista de tuplas  autocares de tipo Autocar, devuelve  la matrícula, la 
# marca y el beneficio del autocar con mayor beneficio. 
# El  beneficio  es el  resultado  de  multiplicar el  precio  diario  por  el  número  de  días  que  ha estado  alquilado  un 
# autocar  dividido  entre  los  kilómetros  recorridos.  A  estos  efectos,  la  propiedad  days  devuelve  los  días  de 
# diferencia entre dos fechas f1 y f2: (f1-f2).days.  En nuestro caso,  tenga en cuenta que, si un autocar inicia el 
# viaje  en  la  fecha  20/10/2024  y  lo  finaliza  el  22/10/2024,  la  diferencia  devolverá  22-20=2,  cuando  se  deben 
# considerar tres días (20, 21 y 22).

def autocar_mayor_beneficio(autocares:list[Autocar])-> tuple[str,str,float]:
  lista = []
  for autocar in autocares:
    beneficio = 0
    for viaje in autocar.viajes:
      dias_totales = ((viaje.fin - viaje.inicio).days + 1)
      beneficio += (dias_totales * autocar.precio) / viaje.kms
    lista.append((autocar.matricula, autocar.marca, beneficio))
  return max(lista, key = lambda x:x[2])

# EJERCICIO 4.

# 4. promedio_viajeros_por_tipo:  dada  una  lista  de  tuplas  de  tipo  Autocar  y  una  fecha,  que  por  defecto 
# tomará el valor None, debe devolver un diccionario que a cada tipo de autocar le asocie el promedio de viajeros 
# que estaban de viaje en la fecha dada. Si la fecha toma el valor None, se tendrán en cuenta todos los viajes. 
# Nota: observe que en los resultados esperados se visualizan todos los tipos de autobús y en el caso de que no 
# haya habido viajeros en la fecha indicada para algún tipo (en el test se usa 10 de febrero de 2024), el resultado 
# es None para el tipo de que se trate.

def promedio_viajeros_por_tipo(autocares: list[Autocar], fecha:date|None=None)->dict[str,float|None]:
  dicc = defaultdict(list) 
  dicc2 = defaultdict()
  for autocar in autocares:
    for viaje in autocar.viajes:
      if fecha is None or viaje.inicio.date() < fecha and fecha > viaje.fin.date():
        dicc[autocar.tipo].append(viaje.num_viajeros)
  for tipo, viajeros in dicc.items():
    dicc2[tipo] = mean(viajeros)
  return dicc2


print(promedio_viajeros_por_tipo(lee_autocares(r'data\autocares.csv'), date(2024, 2, 10)))



   
        
