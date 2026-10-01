from baloncesto import*

def victoria_por_equipo_test(partidos):
    print(victorias_por_equipo(partidos))

def equipos_minimo_victorias_test(partidos, n):
    print(equipos_minimo_victorias(partidos, n))

def equipos_mas_victorias_por_año_test(partidos, n):
    print(equipos_mas_victorias_por_año(partidos, n))

def main():
    datos = lee_partidos(r'FP_25_26\doc\examenes\Exámenes-curso-2022-2023\Examen-del-primer-cuatrimestre-enero-2023\Sesion3\data\CSV de la sesión 3.csv')
    victoria_por_equipo_test(datos)
    equipos_minimo_victorias_test(datos, 8)
    equipos_mas_victorias_por_año_test(datos, 8)

if __name__ == '__main__':
    main()





