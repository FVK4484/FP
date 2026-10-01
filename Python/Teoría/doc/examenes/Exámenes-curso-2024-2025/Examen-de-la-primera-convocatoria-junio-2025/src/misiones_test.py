from misiones import*

def test_lee_misiones(ruta_fichero):
    print(f'Total de misiones leídas: {len(lee_misiones(ruta_fichero))}')
    print(f'Primeras 3 misiones: {lee_misiones(ruta_fichero)[:3]}')

def test_comandante_ocioso(misiones):
    print(f'Comandante más ocioso: {comandante_ocioso(misiones)}')

def test_comandante_mas_activo_por_mes(misiones):
    print('Comandantes más activos por mes: ')
    for año_mes, comandantes in comandante_mas_activo_por_mes(misiones).items():
        print(f'{año_mes} : {comandantes[:1]}')

def main():
    misiones = lee_misiones(r'FP_25_26\doc\examenes\Exámenes-curso-2024-2025\Examen-de-la-primera-convocatoria-junio-2025\data\misiones.csv')
    # test_lee_misiones(r'FP_25_26\doc\examenes\Exámenes-curso-2024-2025\Examen-de-la-primera-convocatoria-junio-2025\data\misiones.csv')
    # test_comandante_ocioso(misiones)
    test_comandante_mas_activo_por_mes(misiones)

if __name__ == '__main__':
    main()