'''
A partir del archivo propinas.csv, realizar lo siguiente:
  0. Lee cada fila del CSV como un objeto Propina, usando namedtuple.
  1. Calcular el promedio de propina por género (usando dict).
  2. Calcular el promedio de propina por día de la semana (usando defaultdict).
  3. Contar la frecuencia del número de comensales por mesa (usando Counter).
  4. Obtener que día de la semana tiene mayor media de propina (usando defaultdict)
'''

import csv
from collections import namedtuple, defaultdict, Counter

Propina = namedtuple("propina", ["factura", "propina", "genero", "fumador", \
                                            "diaSemana", "horaSemana", "numComensales"])

diaSemanaDict  = {"Thur":"Jueves","Fri":"Viernes","Sat":"Sábado","Sun":"Domingo"}
generoDict     = {"Male":"Hombre", "Female":"Mujer"}
horaSemanaDict = {"Lunch":"Almuerzo", "Dinner":"Cena"}

# 0. Leer cada fila del CSV como un objeto Propina, usando namedtuple.  
#    Devolver lista de Propina 
def leerFicheroCSV(ruta) -> list:       
    res = []
    try:
        # Leer el archivo CSV para verificar su contenido
        with open(ruta, mode='r', encoding='utf-8') as archivo:
            pass # Pendiente de cumplimentar
        
    except IOError as e:
        print(f"Error al intentar leer el archivo: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    return res

# 1. Calcular el promedio de propina por género (usando dict).
#    Devolver un diccionario con clave género y valor la media de propinas
def promedio_por_genero(registros) -> dict:       
    
    pass # Pendiente de cumplimentar

# 1. Calcular el promedio de propina por género (usando dict) - POR COMPRENSIÓN -. 
#    Devolver un diccionario con clave género y como valor la media de propinas
def promedio_por_genero_Comprension(registros) -> dict:           

    pass # Pendiente de cumplimentar

# 2. Calcular el promedio de propina por día de la semana (usando defaultdict)
#    Si no se indica un día concreto, son todos los días     
#    Devolver defaultdict con clave día de la semana y como valor la media de propinas
def promedio_por_dia(registros, dia=None) -> defaultdict:
    
    pass # Pendiente de cumplimentar

# 2 bis. Calcular el promedio de propina por día de la semana (usando defaultdict) - POR COMPRENSION - 
#        Si no se indica un día concreto, son todos los días
#        Devolver defaultdict con clave día de la semana y como valor la media de propinas
def promedio_por_dia_Comprension(registros, dia=None) -> defaultdict:
    
    pass # Pendiente de cumplimentar

# 3. Contar la frecuencia del número de comensales por mesa (usando Counter).
#    Devolver un contador con clave el número de comensales y como valor el contador  
def frecuencia_numero_comensales (registros) -> Counter:
    
    pass # Pendiente de cumplimentar

# 4. Obtener que día de la semana tiene mayor media de propina (usando defaultdict)
#       Devolver tupla con:
#          - Diccionario con clave día de la semana y como valor la propina media de ese día 
#          - Tupla con el día de la semana y la media de propina mayor.     
def dia_con_mayor_media_propina (registros) -> tuple[dict, tuple[str, int]]:

    pass # Pendiente de cumplimentar 

# 4.bis Obtener que día de la semana tiene mayor media de propina (usando defaultdict) - POR COMPRENSIÓN
#       Devolver tupla con:
#          - Diccionario con clave día de la semana y como valor la propina media de ese día 
#          - Tupla con el día de la semana y la media de propina mayor.     

def dia_con_mayor_media_propina_Comprension (registros) -> tuple[dict, tuple[str,int]]:

    pass # Pendiente de cumplimentar
 
if __name__ == "__main__":

    # 0. Leer fichero de propinas 
    registros = leerFicheroCSV("data\propinas.csv")
    
    if not registros:
        print ("******* NO SE HA RECUPERADO INFORMACIÓN DEL FICHERO CSV **********")
    else:
        # Mostrar resultados
        print("\n *** 0. leer_fichero_csv  ***")
        print (registros[:3])

        # 1. Calcular el promedio de propina por género (usando dict)
        promedio1 = promedio_por_genero(registros) 
        # Mostrar resultados
        print("\n *** 1. promedio_por_genero_Comprension ***")
        print("Promedio de propina por género:")
        print(promedio1)
 
        # 1 bis. Calcular el promedio de propina por género (usando dict) - POR COMPRENSIÓN -  
        promedio2 = promedio_por_genero_Comprension(registros) 
        # Mostrar resultados
        print("\n *** 1 bis. promedio_por_genero_Comprension ***")
        print("Promedio de propina por género:")
        print(promedio2)

        # 2. Calcular el promedio de propina por día de la semana (usando defaultdict)
        promedio3 = promedio_por_dia(registros, "Jueves")
        # Mostrar resultados
        print("\n *** 2. promedio_por_dia ***")
        print("Promedio de Propinas de los Jueves:")
        for clave, valor in promedio3.items():
            print(f"Día: {clave} - Promedio: {valor}")

        promedio4 = promedio_por_dia_Comprension(registros)
        # Mostrar resultados
        print("\n *** 2. promedio_por_dia_Comprension ***")
        print("Promedio de Propinas agrupadas por día:")
        for clave, valor in promedio4.items():
            print(f"Día: {clave} - Promedio: {valor}")

        # 2 bis. Calcular el promedio de propina por día de la semana (usando defaultdict) - POR COMPRENSIÓN -
        promedio5 = promedio_por_dia_Comprension(registros, "Jueves")
        # Mostrar resultados
        print("\n *** 2. promedio_por_dia_Comprension ***")
        print("Promedio de Propinas de los Jueves:")
        for clave, valor in promedio5.items():
            print(f"Día: {clave} - Promedio: {valor}")

        promedio6 = promedio_por_dia_Comprension(registros)
        # Mostrar resultados
        print("\n *** 2. promedio_por_dia_Comprension ***")
        print("Promedio propinas agrupadas por día:")
        for clave, valor in promedio6.items():
            print(f"Día: {clave} - Promedio: {valor}")
 
        # 3. Contar la frecuencia del número de comensales por mesa (usando Counter)
        contador = frecuencia_numero_comensales (registros) 
        # Mostrar resultados
        print("\n *** 3. frecuencia_numero_comensales ***")        
        print("Frecuencia de número de comensales:")
        print(dict(contador))

        # 4. Obtener que día de la semana tiene mayor media de propina (usando defaultdict)
        tupla = dia_con_mayor_media_propina (registros)
        # Mostrar resultados
        print("\n *** 4. dia_con_mayor_media_propina ***")        
        print("Promedio propinas por día:", tupla[0])
        tupla_aux = tupla[1]
        print(f"El día con mayor media de propina es {tupla_aux[0]} con {tupla_aux[1]}")
 
        # 4 bis. Obtener que día de la semana tiene mayor media de propina (usando defaultdict) - POR COMPRENSIÓN -   
        tupla = dia_con_mayor_media_propina_Comprension (registros)
        # Mostrar resultados
        print("\n *** 4 bis. dia_con_mayor_media_propina_Comprension ***")
        print("Promedio propinas por día:", tupla[0])
        tupla_aux = tupla[1]
        print(f"El día con mayor media de propina es {tupla_aux[0]} con {tupla_aux[1]}")