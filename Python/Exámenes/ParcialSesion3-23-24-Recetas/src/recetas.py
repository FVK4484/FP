from collections import Counter, defaultdict
from typing import Dict, NamedTuple, Optional, List, Set, Tuple 
from datetime import date, datetime 
import csv
Receta = NamedTuple("Receta",  
                    [("nombre", str), 
                     ("tipo", str), 
                     ("dificultad", str), 
                     ("ingredientes", Optional[List[str]]), 
                     ("tiempo_preparacion", int), 
                     ("calorias", int), 
                     ("fecha_creacion", date), 
                     ("precio_estimado", float) 
                    ])

# EJERCICIO 1.

def lee_recetas(filename: str) -> List[Receta]:
    lista = []
    with open(filename, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, tipo, dificultad, ingredientes, tiempo_preparacion, calorias, fecha_creacion, precio_estimado in lector:
            ingredientes = parsea_ingredientes(ingredientes)
            tiempo_preparacion = int(tiempo_preparacion)
            calorias = int(calorias)
            fecha_creacion = parsea_fecha(fecha_creacion)
            precio_estimado = float(precio_estimado)
            tupla = Receta(nombre, tipo, dificultad, ingredientes, tiempo_preparacion, calorias, fecha_creacion, precio_estimado)
            lista.append(tupla)
        return lista


def parsea_ingredientes(ingredientes: str)-> List[str]:
    lista = []
    ingredientes_nuevos = ingredientes.replace('"', "")
    for ingrediente in ingredientes_nuevos.split(","):
        if len(ingredientes_nuevos) > 0:
            lista.append(ingrediente.strip())
        else:
            lista = None
    return lista

def parsea_fecha(fecha: str)->date:
    return datetime.strptime(fecha, "%Y-%m-%d").date()

# EJERCICIO 2.

def receta_mas_barata(recetas: List[Receta],
                      tipos: Set[str],
                      n: Optional[int] = None) -> Receta:
    oreden_calorias = sorted((receta for receta in recetas if receta.tipo in tipos), key=lambda x:x.calorias)[:n]
    return min(oreden_calorias, key=lambda x:x.precio_estimado)

# EJERCICIO 3.

# 3. obten_ingredientes: devuelve el conjunto de ingredientes necesarios para cocinar todas las recetas con 
# ingredientes creadas en el intervalo de meses [mes1, mes2). Si mes1 no se especifica, se consideran todas 
# las recetas creadas en un mes anterior a mes2. Si mes2 no se especifica, se consideran todas las recetas 
# creadas  en  un  mes  posterior  a  mes1 o  del  mismo  mes1.  Si  no  se  proporciona ninguno,  no  se  tiene  en 
# cuenta el mes. (1 punto) 

def obten_ingredientes(recetas: List[Receta],  
                          mes1: Optional[int] = None, 
                          mes2: Optional[int] = None) -> Set[str]:
    res = set() 
    for receta in recetas: 
        mes_receta = receta.fecha_creacion.month 
        if receta.ingredientes != None and (mes1 is None or mes_receta >= mes1) and (mes2 is None or mes_receta < mes2):
            res = res.union(receta.ingredientes)   
    return res  

# EJERCICIO 4.

# 4. recetas_con_precio_menor_promedio: devuelve una lista con n las tuplas (nombre, calorías) con menos 
# calorías de las recetas cuyo precio sea menor que la media general (el promedio de todos los precios), 
# ordenadas de menor a mayor número de calorías.  (1,5 puntos)

def recetas_con_precio_menor_promedio(recetas: List[Receta], n: int)-> List[Tuple[str, int]]:
    cont = 0
    suma_precio = 0
    for receta in recetas:
        suma_precio += receta.precio_estimado
        cont += 1
    precio_promedio = suma_precio / cont

    return sorted(((receta.nombre, receta.calorias) for receta in recetas if receta.precio_estimado < precio_promedio), key=lambda x:x[1])[:n]

# EJERCICIO 5.

# 5. receta_mas_ingredientes: devuelve una tupla con el nombre y los ingredientes de la receta con mayor 
# cantidad de ingredientes considerando solo recetas que contengan alguno de los ingredientes 
# especificados  en  el  parámetro.  Si  ingredientes  no  se  especifica,  se  consideran  todas  las  recetas.  (1,5 
# puntos)

def receta_mas_ingredientes(recetas: List[Receta],  
                           ingredientes: Optional[Set[str]] = None)-> Tuple[str, List[str]]:
    recetas = [receta for receta in recetas 
               if receta.ingredientes != None 
               and (ingredientes == None or tiene_algun_ingrediente(receta, ingredientes))] 
 
    receta = max(recetas, key=lambda x: len(x.ingredientes) ) 
    return (receta.nombre, receta.ingredientes) 
 
def tiene_algun_ingrediente(receta:Receta, ingredientes: Set[str]) -> bool: 
    res = False 
    for ingrediente in receta.ingredientes: 
        if ingrediente in ingredientes: 
            res = True 
            break 
    return res

# EJERCICIO 6.

# 6. ingredientes_mas_comunes_por_tipo:   devuelve  un  diccionario  con  los  3  ingredientes  más  comunes 
# para cada tipo de receta. (2 puntos)

def ingredientes_mas_comunes_por_tipo(recetas: List[Receta])-> Dict[str, List[str]]: 
    d = agrupar_ingredientes_por_tipo(recetas) 
    res = {} 
    for tipo, ingredientes in d.items(): 
        contador_ingredientes = Counter(ingredientes) 
        res[tipo] = ingredientes_mas_comunes(contador_ingredientes) 
    return res

def agrupar_ingredientes_por_tipo(recetas: List[Receta])-> Dict[str, List[str]]:
    dicc = defaultdict(list)
    for receta in recetas:
        if receta.ingredientes:
            dicc[receta.tipo] += list(receta.ingredientes)
    return dicc

def ingredientes_mas_comunes(cont_ingredientes: Dict[str, int]) -> List[str]: 
    return [ingrediente for ingrediente, _ in cont_ingredientes.most_common(3)]
    
print(ingredientes_mas_comunes_por_tipo(lee_recetas('data\CSV de la sesión 3.csv')))