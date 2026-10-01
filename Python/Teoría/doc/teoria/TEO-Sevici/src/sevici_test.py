from sevici import*

def test_lee_estaciones(fichero):
    print(f'Las tres primeras son : \n{lee_estaciones(fichero)[:3]}')

def test_estaciones_bicis_libres(estaciones, k):
    print(f'Hay {len(estaciones_bicis_libres(estaciones, k))} estaciones con {k} o más bicis libres y las 5 primeras son: \n{estaciones_bicis_libres(estaciones, k)[:5]}')

def test_estaciones_cercanas(estaciones, coordenadas, k):
    print(f'Las {k} estaciones más cercanas al punto {coordenadas} son: \n{estaciones_cercanas(estaciones, coordenadas, k)}')

if __name__=='__main__':
    datos = lee_estaciones(r'doc\teoria\TEO-Sevici\data\estaciones.csv')
    # test_lee_estaciones(r'doc\teoria\TEO-Sevici\data\estaciones.csv')
    test_estaciones_bicis_libres(datos, 5)
    test_estaciones_bicis_libres(datos, 10)
    test_estaciones_bicis_libres(datos, 1)
    # test_estaciones_cercanas(datos, (37.357659, -5.9863), 5)
    # print(media_coordenadas(datos))

    