import csv
from collections import Counter, namedtuple, defaultdict

BatallaGOT = namedtuple('BatallaGOT', 'nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados')

# Ejercicio 1.
def lee_batallas(fichero: str)->list[BatallaGOT]:
    lista = []
    with open(fichero, encoding='utf-8')as f:
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados in lector:
            gana_atacante = parsea_gana_atacante(gana_atacante)
            muertes_principales = parsea_muertes_principales(muertes_principales)
            comandantes_atacantes = parsea_lista(comandantes_atacantes)
            comandantes_atacados = parsea_lista(comandantes_atacados)
            num_atacantes = parsea_num(num_atacantes)
            num_atacados = parsea_num(num_atacados)
            tupla = BatallaGOT(nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes, comandantes_atacados, region, num_atacantes, num_atacados)
            lista.append(tupla)
        return lista

def parsea_gana_atacante(atacante: str)->bool:
    res = False
    if atacante == 'win':
        res = True
    return res

def parsea_muertes_principales(muertes: str)->bool:
    res = False
    if muertes == '1':
        res = True
    return res

def parsea_lista(comandantes: str)->list[str]:
    lista = []
    if len(comandantes) > 0:
        for comandante in comandantes.strip().split(','):
            lista.append(comandante)
    return lista

def parsea_num(numero: str)->int | None:
    res = None
    if len(numero) > 0:
        res = int(numero)
    return res

# Ejercicio 2.
def reyes_mayor_menor_ejercito(batallas: list[BatallaGOT])->tuple[str, str]:
    participantes = {} 
    for batalla in batallas: 
        if batalla.num_atacantes != None: 
            if batalla.rey_atacante not in participantes: 
                participantes[batalla.rey_atacante] = 0 
            participantes[batalla.rey_atacante] += batalla.num_atacantes 
        if batalla.num_atacados != None: 
            if batalla.rey_atacado not in participantes: 
                participantes[batalla.rey_atacado] = 0 
            participantes[batalla.rey_atacado] += batalla.num_atacados   
    return max(participantes.items(), key = lambda t:t[1])[0], min(participantes.items(), key = lambda t:t[1])[0]

# Ejercicio 3.
def batallas_mas_comandantes(batallas, regiones=None, n=None):     
    res = sorted(((b.nombre, 
        len(b.comandantes_atacantes) + len(b.comandantes_atacados)) 
        for b in batallas if regiones == None or b.region in regiones),  
        key = lambda t:t[1], reverse = True) 
    if n != None: 
        return res[:n] 
    else: 
        return res

# Ejercicio 4.

def rey_mas_victorias(batallas, rol='ambos'): 
    conteos = {} 
    for b in batallas: 
        if b.rey_atacante not in conteos: 
            conteos[b.rey_atacante] = 0  
        if b.rey_atacado not in conteos: 
            conteos[b.rey_atacado] = 0  
 
        if (rol == 'ambos' or rol == 'atacante') and b.gana_atacante: 
            conteos[b.rey_atacante] += 1 
        elif (rol == 'ambos' or rol == 'atacado') and not b.gana_atacante: 
            conteos[b.rey_atacado] += 1 
     
    rey, conteo = max(conteos.items(), key = lambda t:t[1]) 
    if conteo > 0: 
        return rey 
    else: 
        return None

# Ejercicio 5.
def rey_mas_victorias_por_region(batallas: list[BatallaGOT], rol: str = 'ambos')->dict[str, list[str]]:
    dicc = {}
    for batalla in batallas:
        if batalla.region in dicc:
            dicc[batalla.region].append(batalla)
        else:
            dicc[batalla.region] = [batalla]

    for region, lista in dicc.items():
        dicc[region] = rey_mas_victorias(lista, rol)
    return dicc


