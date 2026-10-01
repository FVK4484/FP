from motoFP import*

def lee_carreras_test(carreras: list[CarreraFP]) -> None:
    print('Test lee_carreras')
    print(f'Número de carreras leídas:')
    print(f'Las dos primeras son:')
    for elemento in carreras[:2]:
        print(f'{8 * ' '}{elemento}')
    print(f'Las dos últimas son:')
    for elemento in carreras[-2:]:
        print(f'{8 * ' '}{elemento}')

def maximo_dias_sin_ganar_test(carreras: list[CarreraFP], nombre_piloto: str) -> None:
    print('Test maximo_dias_sin_ganar')
    print(f'Para {nombre_piloto}: {maximo_dias_sin_ganar(carreras, nombre_piloto)}')

def piloto_mas_podios_por_circuito_test(carreras: list[CarreraFP]) -> None:
    print('Test piloto_mas_podios_por_circuito')
    for circuito, piloto in piloto_mas_podios_por_circuito(carreras).items(): 
        print(f"{circuito}: {piloto}")

def escuderias_con_solo_un_piloto_test(carreras: list[CarreraFP]) -> None:
    print('Test escuderias_con_solo_un_piloto')
    print(escuderias_con_solo_un_piloto(carreras))

def piloto_racha_mas_larga_victorias_consecutivas_test(carreras: list[CarreraFP], 
                                                  año: int|None = None) -> None:
    print('Test piloto_racha_mas_larga_victorias_consecutivas')
    print(f'Para año={año} {piloto_racha_mas_larga_victorias_consecutivas(carreras, año)}')

def ultimos_ganadores_por_circuito_test(carreras:list[CarreraFP], 
                                   n: int, 
                                   estado: str) -> None:
    print('Test ultimos_ganadores_por_circuito')
    print(f'Para n={n} y estado={estado}')
    for circuito, lista_nombres in ultimos_ganadores_por_circuito(carreras, n, estado).items():
        print(f'{circuito}: {lista_nombres}')

def main():
    carreras = lee_carreras(r'data\CSV de la sesión 1.csv')
    # lee_carreras_test(carreras)
    # maximo_dias_sin_ganar_test(carreras, 'Marc Marquez')
    # maximo_dias_sin_ganar_test(carreras, 'Jorge Martin')
    # maximo_dias_sin_ganar_test(carreras, 'Freddy Mercuri')
    # piloto_mas_podios_por_circuito_test(carreras)
    # escuderias_con_solo_un_piloto_test(carreras)
    # piloto_racha_mas_larga_victorias_consecutivas_test(carreras, 2024)
    # piloto_racha_mas_larga_victorias_consecutivas_test(carreras)
    ultimos_ganadores_por_circuito_test(carreras, 2, 'Seco')
    ultimos_ganadores_por_circuito_test(carreras, 2, 'Mojado')
    
if __name__ == '__main__':
    main()
