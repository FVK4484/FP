from nombres import*

def test_lee_frecuencias_nombre(datos):
    print(f"Se han leído {len(datos)} frecuencias")
    print(f"Las tres primeras son: {datos[:3]}")
    print(f"Las tres últimas son: {datos[-3:]}")

def test_filtar_por_genero(datos, genero):
    datos_filtrados = filtrar_por_genero(datos, genero)
    print(f"Hay {len(datos_filtrados)} frecuencias de género {genero}")
    print(f"Las tres primeras son: {datos_filtrados[:3]}")

def test_calcular_nombres(datos, genero):
    nombres = calcular_nombres(datos, genero)
    print(f"Hay {len(nombres)} nombres de género {genero}")
    print(f"Los diez primeros son: {nombres[:10]}")

def test_calcular_top_nombres_de_año(datos, año, n, genero):
    top = calcular_top_nombres_de_año(datos, año, n, genero)
    print(f"Los {n} nombres nombres top {genero} de {año} son: {top}")

if __name__ == '__main__':
    datos = lee_frecuencias_nombres(
        'data/frecuencias_nombres.csv')
    # test_lee_frecuencias_nombre(datos)
    # test_filtar_por_genero(datos, "Mujer")
    # test_filtar_por_genero(datos, "Hombre")
    # test_calcular_nombres(datos, "Mujer")
    # test_calcular_nombres(datos, "Hombre")
    # test_calcular_nombres(datos, None)
    test_calcular_top_nombres_de_año(datos, 2007, 5,"Mujer")
    test_calcular_top_nombres_de_año(datos, 2007, 5,"Hombre")


