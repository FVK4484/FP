from olimpiadas import*

def lee_registros_olimpiadas_test(filename: str) -> None:
    print('TEST EJERCICIO 1 ########################################')
    print(f'Se han leído {len(lee_registros_olimpiadas(filename))} registros')
    n = 0
    print('Los dos primeros son:')
    for elemento in lee_registros_olimpiadas(filename)[:2]:
        print(f'{7 * ' '}{n}-{elemento}')
        n += 1
    n = 0
    print('Los dos últimos son:')
    for elemento in lee_registros_olimpiadas(filename)[-2:]:
        print(f'{7 * ' '}{n}-{elemento}')
        n += 1

def deportes_ambos_generos_test(registros: List[Registro], anyo: int) -> None:
    print('TEST EJERCICIO 2 ########################################')
    print(f'Los deportes que han tenido competición masculina y femenina en el año {anyo} son: {deportes_ambos_generos(registros, anyo)}')
    
def deportes_mas_frecuentes_test(registros: List[Registro], 
                            n: int, 
                            genero: str) ->  None:
    print('TEST EJERCICIO 3 ########################################')
    print(f'Los {n} deportes más frecuentes para el género {genero} son: {deportes_mas_frecuentes(registros, n, genero)}')

def deporte_con_mas_paises_distintos_con_oro_test(registros: List[Registro], 
                                             genero: Optional[str] = None) -> None:
    print('TEST EJERCICIO 4 ########################################')
    print(f'El deporte para el género {genero} en el que hay más países distintos con medallas de oro es: {deporte_con_mas_paises_distintos_con_oro(registros, genero)}')

def main():
    registros = lee_registros_olimpiadas(r'data\CSV de la sesión 1.csv')
    # lee_registros_olimpiadas_test(r'data\CSV de la sesión 1.csv')
    # deportes_ambos_generos_test(registros, 1984)
    # deportes_mas_frecuentes_test(registros, 4,'HOMBRE')
    # deportes_mas_frecuentes_test(registros, 5,'MUJER')
    deporte_con_mas_paises_distintos_con_oro_test(registros)
    deporte_con_mas_paises_distintos_con_oro_test(registros, 'HOMBRE')
    deporte_con_mas_paises_distintos_con_oro_test(registros, 'MUJER')


if __name__ == '__main__':
    main()