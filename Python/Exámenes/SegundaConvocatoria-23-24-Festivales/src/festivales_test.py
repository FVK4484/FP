from festivales import*

def lee_festivales_test(archivo:str)->List[Festival]:
    print("Test Ej1: lee_festivales")
    print("Test lee_festivales")
    print(f"Total festivales: {len(lee_festivales(archivo))}")
    print(f"Los tres primeros: {lee_festivales(archivo)[:3]}")

def total_facturado_test(festivales:List[Festival], fecha_ini:Optional[date]=None, fecha_fin:Optional[date]=None)->float:
    print("Test Ej2: total_facturado")
    print(f"Entre {fecha_ini} y {fecha_fin} el total es: {total_facturado(festivales, fecha_ini, fecha_fin)}")

def artista_top_test(festivales: List[Festival]) -> Tuple[int, str]:
    print('Test Ej3: artista_top')
    print(f'El artista que ha actuado en más festivales es {artista_top(festivales)[1]}, con {artista_top(festivales)[0]} festivales.')

def mes_mayor_beneficio_medio_test(festivales: List[Festival]) -> str:
    print('Test Ej4: mes_beneficio_medio')
    print(f'El mes con más beneficio es {mes_mayor_beneficio_medio(festivales)}.')

def main():
    festivales = lee_festivales(r"data\festivales.csv")
    # lee_festivales_test(r"data\festivales.csv")
    # total_facturado_test(festivales)
    # total_facturado_test(festivales, None, date(2024, 6, 15))
    # total_facturado_test(festivales, date(2024, 6, 15), None)
    # total_facturado_test(festivales, date(2024, 6, 1), date(2024, 6, 15))
    # artista_top_test(festivales)
    mes_mayor_beneficio_medio_test(festivales)

if __name__ == '__main__':
    main()