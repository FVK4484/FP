from urbanizacion import*

def test_lee_viviendas(fichero):
    print('test_lee_viviendas')
    print(f'Número de registros leídos: {len(lee_viviendas(fichero))}')
    print(f'Las dos primeras: {lee_viviendas(fichero)[:2]}')
    print(f'Las dos últimas: {lee_viviendas(fichero)[-2:]}')

def total_mejoras_por_calle_test(viviendas: list[Vivienda], par_impar: str) -> dict[str,int]:
    print("test_total_mejoras_por_calle")
    print(f"Número de mejoras en viviendas: {par_impar}")
    for calle, numero_total in total_mejoras_por_calle(viviendas, par_impar).items():
        print(f"{calle} --> {numero_total}")

def main():
    viviendas = lee_viviendas('doc/examenes/Exámenes-curso-2024-2025/Examen-del-primer-cuatrimestre-enero-2025/Sesion2/data/urbanizacion.csv')
    test_lee_viviendas('doc/examenes/Exámenes-curso-2024-2025/Examen-del-primer-cuatrimestre-enero-2025/Sesion2/data/urbanizacion.csv')
    # total_mejoras_por_calle_test(viviendas, "par")
    # total_mejoras_por_calle_test(viviendas, "impar")

if __name__ == '__main__':
    main()