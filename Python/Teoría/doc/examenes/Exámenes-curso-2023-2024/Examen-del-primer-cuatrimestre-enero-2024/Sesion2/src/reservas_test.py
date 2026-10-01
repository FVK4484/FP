from reservas import*

def test_lee_reservas(fichero):
    print("Test lee_reservas")
    print(f"Total reservas: {len(lee_reservas(fichero))}")
    print("Las tres primeras: ")
    print(lee_reservas(fichero)[:2])

def test_total_facturado(reservas, ini, fin):
    total = total_facturado(reservas, ini, fin)
    print("Test total_facturado")
    print(f"En todo el periodo de datos: {total_facturado(reservas, None, None)}")
    print(f"Desde {ini.day} de {ini.month} de {ini.year} hasta {fin.day} de {fin.month} de {fin.year}: {total}")

def test_reserva_mas_larga(reservas, n):
    print(reserva_mas_larga(reservas, n))


if __name__ == '__main__':
    test_lee_reservas(r'FP_25_26\doc\examenes\Exámenes-curso-2023-2024\Examen-del-primer-cuatrimestre-enero-2024\Sesion2\data\CSV de la sesión 2.csv')
    # test_total_facturado(test_lee_reservas(r'FP_25_26\doc\examenes\Exámenes-curso-2023-2024\Examen-del-primer-cuatrimestre-enero-2024\Sesion2\data\CSV de la sesión 2.csv'), None, None)
    # test_reserva_mas_larga([Reserva(nombre='Ana Fernández', dni='98762912S', fecha_entrada=datetime.date(2022, 1, 2), fecha_salida=datetime.date(2022, 1, 6), tipo_habitacion='Suite', num_personas=4, precio_noche=202.97, servicios_adicionales=['Parking', 'Gimnasio', 'Spa']), Reserva(nombre='María Fernández', dni='25061289Y', fecha_entrada=datetime.date(2022, 1, 1), fecha_salida=datetime.date(2022, 1, 3), tipo_habitacion='Familiar', num_personas=4, precio_noche=83.77, servicios_adicionales=[])], 2)