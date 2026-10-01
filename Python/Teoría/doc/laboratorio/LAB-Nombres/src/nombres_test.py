from nombres import*

datos = lee_frecuencias_nombres(r'FP_25_26\doc\laboratorio\LAB-Nombres\data\frecuencias_nombres.csv')

def leer_frecuencias_nombres_test():
    print(datos)

def filtrar_por_genero_test():
    print(f'Número de Hombres: {len(filtrar_por_genero(datos, 'Hombre'))}')
    print(f'Número de Mujeres: {len(filtrar_por_genero(datos, 'Mujer'))}')

def calcular_nombres_test():
    print(calcular_nombres(datos, 'Hombre'))

def calcular_top_nombres_de_año_test():
    print(calcular_top_nombres_de_año(datos, 2002))

def calcular_nombres_ambos_generos_test():
    print(calcular_nombres_ambos_generos(datos))

def calcular_nombres_compuestos_test():
    print(len(calcular_nombres_compuestos(datos)))

def calcular_frecuencia_media_nombres_año_test():
    print(calcular_frecuencia_media_nombres_año(datos, 'DIEGO', 2002, 2017))

def calcular_nombre_mas_frecuente_año_genero_test():
    print(calcular_nombre_mas_frecuente_año_genero(datos, 2002, 'Hombre'))

def calcular_año_mas_frecuencia_nombre_test():
    print(calcular_año_mas_frecuencia_nombre(datos, 'DIEGO'))

def calcular_nombres_mas_frecuentes_test():
    print(calcular_nombres_mas_frecuentes(datos, 'Hombre', 10))

def calcular_año_frecuencia_por_nombre_test():
    print(calcular_año_frecuencia_por_nombre(datos, 'Hombre'))

def calcular_nombre_mas_frecuente_por_año_test():
    print(calcular_nombre_mas_frecuente_por_año(datos, 'Hombre'))

def main():
    # leer_frecuencias_nombres_test()
    # filtrar_por_genero_test()
    # calcular_nombres_test()
    # calcular_top_nombres_de_año_test()
    # calcular_nombres_ambos_generos_test()
    calcular_nombres_compuestos_test()
    # calcular_frecuencia_media_nombres_año_test()
    # calcular_nombre_mas_frecuente_año_genero_test()
    # calcular_año_mas_frecuencia_nombre_test()
    # calcular_nombres_mas_frecuentes_test()
    # calcular_año_frecuencia_por_nombre_test()
    # calcular_nombre_mas_frecuente_por_año_test()

if __name__ == '__main__':
    main()
