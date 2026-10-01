from poblacion import*

def test_lee_poblaciones(fichero):
    datos = lee_poblaciones(fichero)
    return datos

def test_calcula_paises(poblaciones):
    print(calcula_paises(poblaciones))

def test_filtra_por_pais(poblaciones, nombre_o_codigo):
    print(filtra_por_pais(poblaciones, nombre_o_codigo))

def test_filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    print(filtra_por_paises_y_anyo(poblaciones, anyo, paises))

def test_muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    print(muestra_evolucion_poblacion(poblaciones, nombre_o_codigo))

def test_muestra_comparativa_paises_anyo(poblaciones, anyo, paises): 
    print(muestra_comparativa_paises_anyo(poblaciones, anyo, paises))

if __name__ == '__main__':
    datos = test_lee_poblaciones(r'doc\laboratorio\LAB-Poblacion\data\population.csv')
    # print(datos)
    # test_calcula_paises(datos)
    # test_filtra_por_pais(datos, 'ARB')
    test_filtra_por_paises_y_anyo(datos, 1959, {'Arab World', 'Central Europe and the Baltics', 'East Asia & Pacific'})
    # test_muestra_evolucion_poblacion(datos, 'ESP')
    # test_muestra_comparativa_paises_anyo(datos, 1981, {'China', 'France', 'Mexico', 'Portugal', 'Spain'})