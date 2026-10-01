from datetime import*
import csv
from matplotlib import pyplot
from collections import namedtuple

# Ejercicio1
def es_bisiesto(anyo):
    res = False
    if (anyo%400 == 0) or (anyo%4 == 0 and anyo%100 != 0):
        res = True
    return res
# print(es_bisiesto(2000))
# print(es_bisiesto(2024))
# print(es_bisiesto(1900))
# print(es_bisiesto(2025))

# Ejercicio2
def extrae_numeros(texto):
    numeros = []
    for palabra in texto.split():
        if palabra.isdigit():
            numeros.append(int(palabra))
    return numeros
# print(extrae_numeros("Este año la empresa ganó 12432 euros de 8 contratos"))

# Ejercicio3
def calcula_edad(fecha_nacimiento):
    fecha_actual = date.today()
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

    cumpleaños = date(fecha_actual.year, fecha_nacimiento.month, fecha_nacimiento.day)
    if cumpleaños < fecha_actual:
        cumpleaños = date(fecha_actual.year + 1, fecha_nacimiento.month, fecha_nacimiento.day)

    dias_para_cumple = (cumpleaños - fecha_actual).days
    return print(f"Tienes {edad} años. Quedan {dias_para_cumple} días para tu cumpleaños.")
# calcula_edad('02/03/2006')

# Ejercicio4
def lee_variaciones_temperatura(fichero):
    lista = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for fecha, variacion in lector:
            fecha = parseo_fecha(fecha)
            variacion = float(variacion)
            tupla = (fecha, variacion)
            lista.append(tupla)
    return lista

def parseo_fecha(fecha):
    if fecha == None:
        fecha_nueva = 0
    else:
        fecha_nueva = datetime.strptime(fecha, '%d/%m/%Y').date()
    return fecha_nueva
# print(lee_variaciones_temperatura(r"FP_25_26/doc/ejercicios/Ejercicios del tema 2, Expresiones, tipos predefinidos y entrada salida/data/monthly_csv.csv"))

# Ejercicio5
def muestra_variaciones_temperatura(fichero):
    lista = []
    lista2 = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for fecha, variacion in lector:
            fecha = parseo_fecha(fecha)
            variacion = float(variacion)
            tupla = (fecha, variacion)
            lista.append(tupla[0])
            lista2.append(tupla[1])
            pyplot.plot(lista, lista2)
    return pyplot.show()
# print(muestra_variaciones_temperatura(r"FP_25_26/doc/ejercicios/Ejercicios del tema 2, Expresiones, tipos predefinidos y entrada salida/data/monthly_csv.csv"))

# Ejercicio6
def muestra_variaciones_temperatura2(fichero, fecha_inicial, fecha_final):
    lista = []
    lista2 = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for fecha, variacion in lector:
            fecha = parseo_fecha(fecha)
            variacion = float(variacion)
            tupla = (fecha, variacion)
            fecha_inicial = parseo_fecha(fecha_inicial)
            fecha_final = parseo_fecha(fecha_final)
            if (fecha_inicial == None and fecha_final == None):
                lista.append(tupla[0])
            elif (fecha_inicial == None):
                fecha_inicial = 0
                if (fecha > fecha_inicial and fecha_final > fecha):
                    lista.append(tupla[0])
            elif (fecha_final == None):
                fecha_final = 0
                if (fecha > fecha_inicial and fecha_final > fecha):
                    lista.append(tupla[0])
            lista2.append(tupla[1])
            pyplot.plot(lista, lista2)
    return pyplot.show()

# print(muestra_variaciones_temperatura2(r"FP_25_26/doc/ejercicios/Ejercicios del tema 2, Expresiones, tipos predefinidos y entrada salida/data/monthly_csv.csv", None, None))

# Ejercicio7
Persona = namedtuple('Persona', ['nombre', 'edad', 'tiene_licencia', 'hobbies', 'paises_visitados', 'libros_leidos'])

juan = Persona('Juan', 20, True, {'fútbol', 'cine'}, {'España', 'Chile'}, ['Don Quijote', 'El Principito'])
maria = Persona('Maria', 15, False, {'lectura', 'música', 'cine'}, {'Francia', 'Chile'}, ['El Principito', '1984'])
pedro = Persona('Pedro', 17, True, {'fútbol', 'natación'}, {'México'}, ['Cien Años de Soledad', 'Moby Dick', '1984'])


print("Juan tiene más de 18 años:",
    #TODO
)

print("Maria tiene licencia de conducir:",
    #TODO
)

print("Juan ha visitado Chile:",
    #TODO
)

print("A María le gustan el cine y la música:",
    #TODO
)

print("'El Principito' es el último libro que ha leído Maria:",
    #TODO
)

print("Ni Juan ni Pedro tienen licencia de conducir:",
    #TODO
)

print("Maria ha leído al menos 2 libros:",
    #TODO
)

print("María no ha visitado México, pero Pedro sí:",
    #TODO
)

print("Juan ha leído más libros que María pero menos que Pedro:",
    #TODO
)

print("Pedro no ha visitado Chile y tampoco le gusta el cine:",
    #TODO
)

print("El último libro que María ha leído es '1984' y Juan no lo ha leído aún:",
    #TODO
)

print("Pedro ha visitado más países que Juan o ha leído más libros que María:",
    #TODO
)

print("María tiene licencia de conducir o ha leído 'Moby Dick', pero no ambas cosas",
    #TODO
)

print("Juan ha visitado España o Francia, pero no ambos",
    #TODO
)
