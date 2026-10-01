from consumo_electrico import*

def test_lee_facturas(fichero):
    print('Test lee_facturas')
    print(f'Total facturas: {len(lee_facturas(fichero))}')
    print(f'Mostrando las dos primeras y las dos últimas:\n{lee_facturas(fichero)[:2]}\n...\n{lee_facturas(fichero)[-2:]}')

# def test_busca_vivienda_mayor_consumo_acumulado(facturas):
#     print('Test busca_vivienda_mayor_consumo_acumulado(facturas)')
#     print(f'La vivienda con mayor consumo acumulado es la {busca_vivienda_mayor_consumo_acumulado(facturas)[0]} con un consumo total de {busca_vivienda_mayor_consumo_acumulado(facturas)[1]} kWh.')


if __name__ == '__main__':
    datos = lee_facturas(r'FP_25_26\doc\examenes\Exámenes-curso-2023-2024\Examen-de-la-primera-convocatoria-(junio2024)\data\consumos_sevilla_2023.csv')
    test_lee_facturas(r'FP_25_26\doc\examenes\Exámenes-curso-2023-2024\Examen-de-la-primera-convocatoria-(junio2024)\data\consumos_sevilla_2023.csv')
    # test_busca_vivienda_mayor_consumo_acumulado(datos)
