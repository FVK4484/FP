import csv
from collections import namedtuple
import matplotlib.pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(fichero):
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        for pais, codigo, año, censo in lector:
            año = int(año)
            censo = int(censo)
            tupla = RegistroPoblacion(pais, codigo, año, censo)
            lista.append(tupla)
    return lista

def calcula_paises(poblaciones):
    return sorted(set(poblacion.pais 
                      for poblacion in poblaciones 
                      if poblacion.censo != None 
                      and poblacion.año != None))

def filtra_por_pais(poblaciones, nombre_o_codigo):
    return sorted((poblacion.año, poblacion.censo) 
                  for poblacion in poblaciones 
                  if poblacion.pais == nombre_o_codigo 
                  or poblacion.codigo == nombre_o_codigo)

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    return sorted((poblacion.pais, poblacion.censo)
                  for poblacion in poblaciones
                  if poblacion.año == anyo - 1
                  and poblacion.pais in paises) or None

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    titulo = 'Población'
    lista_años = []
    lista_habitantes = []
    for poblacion in poblaciones:
        if poblacion.pais == nombre_o_codigo or poblacion.codigo == nombre_o_codigo:
            lista_años.append(poblacion.año)
            lista_habitantes.append(poblacion.censo)
    plt.title(titulo) 
    plt.plot(lista_años, lista_habitantes)
    plt.show()

def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    titulo = 'Población'
    lista_paises = []
    lista_habitantes = []
    for poblacion in poblaciones:
        if poblacion.año == anyo and poblacion.pais in paises:
            lista_paises.append(poblacion.pais)
            lista_habitantes.append(poblacion.censo)
    plt.title(titulo)
    plt.bar(lista_paises, lista_habitantes)
    plt.show()      