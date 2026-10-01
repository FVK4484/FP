from jugadores import*

def lee_jugadores_test(fichero: str) -> list[Jugador]:
    print(f'Registros leídos: {len(lee_jugadores(fichero))}')
    print(f'Los dos primeros: {lee_jugadores(fichero)[:2]}')
    print(f'Los dos últimos: {lee_jugadores(fichero)[-2:]}')

def mejores_jugadores_test(jugadores: list[Jugador], anyo: int, n: int) -> list[tuple[str, str, float]]:
    print(f'Los {n} mejores jugadores nacidos en el {anyo} son: {mejores_jugadores(jugadores, anyo, n)}')

def jugadores_por_golpes_test(jugadores: list[Jugador]) -> list[tuple[int, set[str]]]:
    print('Jugadores por golpes')
    for elemento in jugadores_por_golpes(jugadores):
        print(elemento)

def promedio_ultimos_resultados_test(jugadores: list[Jugador], f1: date = None, f2: date = None) -> list[tuple[str, float]]:
    print(f'El promedio de cada jugador senior con fecha de actualización entre {f1} y {f2} son:')
    print(promedio_ultimos_resultados(jugadores, f1, f2))

def jugador_menor_handicap_por_federacion_test(jugadores: list[Jugador]) -> dict[str, tuple[str, float]]:
    print('Los mejores jugadores de cada federación son:')
    for federacion, mejor_jugador in jugador_menor_handicap_por_federacion(jugadores).items():
        print(f"        {(federacion, mejor_jugador)}")

def comparativa_de_mejores_resultados_segun_handicap_test(jugadores: list[Jugador]) -> list[tuple[str, float]]:
    print(comparativa_de_mejores_resultados_segun_handicap(jugadores))

def main():
    jugadores = lee_jugadores(r'data\Datos para el ejercicio de Python.csv')
    # lee_jugadores_test('data\Datos para el ejercicio de Python.csv')
    # mejores_jugadores_test(jugadores, 1969, 4)
    jugadores_por_golpes_test(jugadores)
    # promedio_ultimos_resultados_test(jugadores, date(2020, 3, 1), date(2020, 5, 31))
    # promedio_ultimos_resultados_test(jugadores)
    # jugador_menor_handicap_por_federacion_test(jugadores)
    # comparativa_de_mejores_resultados_segun_handicap_test(jugadores)

if __name__ == '__main__':
    main()
