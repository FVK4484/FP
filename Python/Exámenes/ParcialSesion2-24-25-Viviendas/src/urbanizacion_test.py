from urbanizacion import*

def lee_viviendas_test(ruta: str) -> list[Vivienda]:
    print('test_lee_viviendas')
    print(f'Número de registros leídos: {len(lee_viviendas(ruta))}')
    print(f'Las dos primeras: {lee_viviendas(ruta)[:2]}')
    print(f'Las dos últimas: {lee_viviendas(ruta)[-2:]}')

def total_mejoras_por_calle_test(viviendas: list[Vivienda], par_impar: str) -> dict[str,int]:
    print('test_total_mejoras_por_calle')
    print(f'Número de mejoras en viviendas: {par_impar}')
    for calle, veces in total_mejoras_por_calle(viviendas, par_impar).items():
        print(f'{calle} --> {veces}')

def vivienda_con_mejora_mas_rapida_test(viviendas: list[Vivienda]) -> tuple[str,str,int,int,str]:
    print('test_vivienda_con_mejora_mas_rapida')
    print(f'La vivienda que hizo una mejora en menos tiempo es {vivienda_con_mejora_mas_rapida(viviendas)}')

def calle_mayor_diferencia_precios_test(viviendas: list[Vivienda]) -> str:
    print('test_calle_mayor_diferencia_precios')
    print(f'La calle es: {calle_mayor_diferencia_precios(viviendas)}')

def n_viviendas_top_valoradas_por_calle_test(viviendas: list[Vivienda], 
                                        fecha: date|None = None, 
                                        n: int = 3) -> dict[str,list[tuple[str,int,int]]]:
    print('test_n_viviendas_top_valoradas_por_calle')
    print(f'Para n = {n} y fecha = {fecha} son:')
    for calle, lista in n_viviendas_top_valoradas_por_calle(viviendas, fecha, n).items():
        print(f'{calle} --> {lista}')

def valor_metro_cuadrado_por_calle_y_año_test(viviendas: list[Vivienda]) -> list[tuple[int,list[tuple[str,float]]]]:
    print('test_valor_metro_cuadrado_por_calle_y_año')
    for tupla in valor_metro_cuadrado_por_calle_y_año(viviendas):
        print(tupla)

def main():
    viviendas = lee_viviendas(r'data\CSV de la sesión 2.csv')
    # lee_viviendas_test(r'data\CSV de la sesión 2.csv')
    # total_mejoras_por_calle_test(viviendas, 'par')
    # total_mejoras_por_calle_test(viviendas, 'impar')
    # vivienda_con_mejora_mas_rapida_test(viviendas)
    # calle_mayor_diferencia_precios_test(viviendas)
    # n_viviendas_top_valoradas_por_calle_test(viviendas, date(2020,1,1), 4)
    valor_metro_cuadrado_por_calle_y_año_test(viviendas)

if __name__ == '__main__':
    main()