from suscripciones import*

def lee_suscripciones_test(ruta_fichero: str) -> list[Suscripcion]:
    print('Test lee_suscripciones')
    print(f'Total suscripciones: {len(lee_suscripciones(ruta_fichero))}')
    print(f'Las tres primeras: {lee_suscripciones(ruta_fichero)}')

def suscripciones_mas_rentables_test(suscripciones: list[Suscripcion],
                                n: int = 3,
                                tipos_plan: set[str]|None = None) -> list[tuple[str, float]]:
    print("Test suscripciones_mas_rentables")
    if tipos_plan != None:
        print(f"Filtrando por tipo de plan ({tipos_plan}): {suscripciones_mas_rentables(suscripciones, n, tipos_plan)}")
    else:
        print(f"Las {n} suscripciones más rentables (sin filtrar): {suscripciones_mas_rentables(suscripciones, n, tipos_plan)}")

def plan_mas_perfiles_test(suscripciones: list[Suscripcion], 
                           fecha_ini: date|None = None, 
                           fecha_fin: date|None = None) -> tuple[str, int]:
    print('Test plan_mas_perfiles ')
    print(f'Sin filtrar fechas, el plan con más perfiles acumulados es: {plan_mas_perfiles(suscripciones, fecha_ini, fecha_fin)[0]} con {plan_mas_perfiles(suscripciones, fecha_ini, fecha_fin)[1]}')

def main():
    suscripciones = lee_suscripciones("data\CSV de la sesión 3.csv")
    # lee_suscripciones_test('data\CSV de la sesión 3.csv')
    # suscripciones_mas_rentables_test(suscripciones, 3, None)
    # suscripciones_mas_rentables_test(suscripciones, 3, {'Básico'})
    plan_mas_perfiles_test(suscripciones, None, None)

if __name__ == '__main__':
    main()