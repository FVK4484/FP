import csv
from datetime import datetime
from collections import namedtuple
from statistics import mean


Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(fichero):
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            fechahora = datetime.strptime(fechahora, '%d/%m/%Y %H:%M')
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            # if compartido == 'S':
            #     compartido = True
            # else: 
            #     compartido = False
            compartido = (compartido == 'S')
            tupla = Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            lista.append(tupla)
    return lista

# Ejercicio1
def tipos_entreno(entrenos):
    return sorted(set(entreno.tipo 
                      for entreno in entrenos))

# Ejercicio2
def entrenos_duracion_superior(entrenos, d):
    return sorted(entreno 
                  for entreno in entrenos 
                  if entreno.duracion > d)

# Ejercicio3
def suma_calorias(entrenos, f_inicio, f_fin):
    f_inicio = datetime.strptime(f_inicio, '%d/%m/%Y %H:%M')
    f_fin = datetime.strptime(f_fin, '%d/%m/%Y %H:%M')
    return sum(entreno.calorias 
               for entreno in entrenos 
               if f_inicio <= entreno.fechahora 
               and entreno.fechahora <= f_fin)

# Extra:
# Ejercicio4
def entrenamiento_mas_kms(entrenos: list[Entreno])->Entreno:
    # result = None
    # for entreno in entrenos:
    #     if result == None or result.distancia < entreno.distancia:
    #         result = entreno
    # return result
    return max([entreno for entreno in entrenos], key = lambda x:x[5])

# Ejercicio5
def duracion_media_entrenos(entrenos, anyo, mes):
    return [mean(entreno.duracion 
                for entreno in entrenos 
                if entreno.fechahora.year == anyo 
                and entreno.fechahora.month == mes) or None]

'''6.entrenamiento_mas_calorico: recibe una lista de entrenos y devuelve el entrenamiento con mayor gasto calorico'''
def enfrentamiento_mas_calorico(entrenos):
    return [entreno for entreno in entrenos if entreno.calorias == max(entreno.calorias for entreno in entrenos)]

'''7.num_entrenamientos_efectivos: recibe una lista de entrenos y un valor calorico y devuelve el numero de entrenamientos que quemaron calorias por 
encima del valor'''
def num_entrenamientos_efectivos(entrenos, calorias):
    return len([entreno for entreno in entrenos if entreno.calorias > calorias])

'''8.existe_tipo_entrenamiento: recibe una lista de entrenos y un tipo de entrenamiento y devuelve cierto si existe ese tipo dentro del listado. La consulta 
debe ser insensible a mayusculas y/o minisculas.'''
def existe_tipo_entrenamiento(entrenos, tipo):
    return any(entreno.tipo.lower() == tipo.lower() for entreno in entrenos)
