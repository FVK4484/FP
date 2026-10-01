from collections import defaultdict
import csv
from typing import Dict, List, NamedTuple, Optional, Set, Tuple 
from datetime import date, datetime 


Medallas = NamedTuple('Medallas', [('oro', int), ( 'plata', int),  ('bronce', int)]) 

Registro = NamedTuple('Registro', [ 
   ('ciudad_olimpica', str),  
   ('fecha_inicio', date),  
   ('pais', str),  
   ('deporte', str), 
   ('num_participantes', int),  
   ('genero', str),  
   ('medallas', Medallas),   
   ('sede', bool)])  

# EJERCICIO1
def lee_registros_olimpiadas(ruta_fichero: str) -> List[Registro]:
   lista = []
   with open(ruta_fichero, encoding = 'utf-8') as f:
      lector = csv.reader(f)
      next(lector)
      for ciudad_olimpica, fecha_inicio, pais, deporte, num_participantes, genero, medallas, sede in lector:
         ciudad_olimpica = str(ciudad_olimpica).strip()
         fecha_inicio = parsea_fecha(fecha_inicio)
         pais = str(pais).strip()
         deporte = str(deporte).strip()
         num_participantes = int(num_participantes.strip())
         genero = str(genero).strip()
         medallas = parsea_medallas(medallas)
         sede = parsea_sede(sede)
         tupla = Registro(ciudad_olimpica, fecha_inicio, pais, deporte, num_participantes, genero, medallas, sede)
         lista.append(tupla)
      return lista

def parsea_fecha(fecha: str) -> date:
   return datetime.strptime(fecha, "%Y-%m-%d").date()

def parsea_medallas(cadena: str) -> Medallas:
   lista = []
   cadena_nueva = cadena.split("-")
   oro = int(cadena_nueva[0])
   plata = int(cadena_nueva[1])
   bronce = int(cadena_nueva[2])
   tupla = Medallas(oro, plata, bronce)
   return tupla

def parsea_sede(sede: str) -> bool:
   return True if sede == "SI" else False

# EJERCICIO2
def deportes_ambos_generos(registros: List[Registro], anyo: int) -> Set[str]:
   conjunto1 = set(registro.deporte for registro in registros if registro.fecha_inicio.year == anyo and registro.genero == "MUJER")
   conjunto2 = set(registro.deporte for registro in registros if registro.fecha_inicio.year == anyo and registro.genero == "HOMBRE")
   conjunto_global = conjunto1.intersection(conjunto2)
   return conjunto_global

# EJERCICIO3
def deportes_mas_frecuentes(registros: List[Registro], n: int, genero: str) -> List[Tuple[str, int]]:
   dicc = defaultdict(int)
   for registro in registros:
      if registro.genero == genero:
         dicc[registro.deporte] += 1
   return sorted(dicc.items(), key = lambda x:x[1], reverse = True)[:n]

# EJERCICIO4
def deporte_con_mas_paises_distintos_con_oro(registros: List[Registro], genero: Optional[str] = None) -> str:
   dicc = defaultdict(set)
   for registro in registros:
      if registro.genero == genero:
         if registro.medallas.oro >= 1:
            dicc[registro.deporte].add(registro.pais)
      elif genero == None:
         if registro.medallas.oro >= 1:
            dicc[registro.deporte].add(registro.pais)
   return max(dicc.items(), key = lambda x:len(x[1]))[0]

# EJERCICIO5
def deportes_mas_participantes_de_genero_por_juego(registros: List[Registro], pais: str, genero: str) -> Dict[str, List[Tuple[str, int]]]:
   dicc = defaultdict(list)
   for registro in registros:
      if registro.pais == pais and registro.genero == genero:
         dicc[registro.ciudad_olimpica + str(registro.fecha_inicio.year)[-2:]].append((registro.deporte, registro.num_participantes)) 
   return {identificador: sorted(lista_deportes, key=lambda x:x[1], reverse=True)[:3] 
                 for identificador, lista_deportes in dicc.items()} 

# EJERCICIO6
def deporte_con_todos_los_paises(registros: List[Registro]) -> bool:
   conj = set()
   dicc = defaultdict(set)

   for registro in registros:
      conj.add(registro.pais)
      dicc[registro.deporte].add(registro.pais)
   return conj in dicc.values()

# EJERCICIO7
def anyo_con_mayor_incremento_participantes_de_pais(registros: List[Registro], pais: str) -> Tuple[int, int]:
   pass
   


print(deporte_con_todos_los_paises(lee_registros_olimpiadas(r"doc\examenes\Exámenes-curso-2023-2024\Examen-del-primer-cuatrimestre-enero-2024\Sesion1\data\CSV de la sesión 1.csv")))
