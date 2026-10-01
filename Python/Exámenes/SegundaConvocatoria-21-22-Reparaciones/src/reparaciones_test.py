from reparaciones import*

def lee_reparaciones_test(fichero: str) -> list[Reparacion]:
    print('Test 1')
    print(lee_reparaciones(fichero))

def calcula_recaudacion_test(reparaciones: list[Reparacion], centro: str, tipo: str = None) -> float:
    print('Test 2')
    print(calcula_recaudacion(reparaciones, centro, tipo))

def reparaciones_mas_largas_test(reparaciones: list[Reparacion], anyo: int, n: int, centro: str = None) -> list[Reparacion]:
    print('Test 3')
    print(reparaciones_mas_largas(reparaciones, anyo, n, centro))

def centro_mas_rapido_test(reparaciones: list[Reparacion], centros: set[str]) -> str:
    print('Test 4')
    print(centro_mas_rapido(reparaciones, centros))

def centros_experimentados_en_test(reparaciones: list[Reparacion], palabras_clave: set[str]) ->  dict[str, list[str]]:
    print('Test 5')
    print(centros_experimentados_en(reparaciones, palabras_clave))

def main():
    reparaciones = lee_reparaciones(r'data\reparaciones.csv')
    # lee_reparaciones_test(r'data\reparaciones.csv')
    # calcula_recaudacion_test(reparaciones, 'Cádiz', 'móvil')
    # reparaciones_mas_largas_test(reparaciones, 2020, 2, 'Sevilla')
    # centro_mas_rapido_test(reparaciones, {'Sevilla', 'Cádiz'})
    centros_experimentados_en_test(reparaciones, {'PANTALLA', 'BATERÍA'})

if __name__ == '__main__':
    main()

