from centros import *

def test_lee_centros(datos):
    print("Prueba de la funcion lee_centros")
    print(f"Se han leido {len(datos)} centros")
    print(f"Los 3 primeros son: {datos[:3]}")
    print(f"Los 3 últimos son: {datos[-3:]}")

def test_lee_calcular_total_camas_centros_accesibles(datos):

    camas = calcular_total_camas_centros_accesibles(datos)
    print("Prueba de la funcion lee_calcular_total_camas_centros_acesible")
    print(f"Número de camas en centros acesibles:{camas}")

if __name__ == '__main__':
    datos = lee_centros("data/centrosSanitarios.csv")
    test_lee_centros(datos)
    test_lee_calcular_total_camas_centros_accesibles(datos)
