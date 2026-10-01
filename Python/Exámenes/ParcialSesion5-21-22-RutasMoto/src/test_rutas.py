from rutas import*

def lee_rutas_test(fichero: str) -> list[Ruta]:
    print('Test 1')
    print(lee_rutas(fichero))

def acumular_kms_por_meses_test(rutas: list[Ruta]) -> dict[int, list[float]]:
    print('Test 2')
    print(acumular_kms_por_meses(rutas))

def acumular_kms_por_meses_test(rutas: list[Ruta]) -> dict[int, list[float]]:
    print('Test 2')
    print(acumular_kms_por_meses(rutas))

def diferencias_kms_meses_anyo_test(rutas: list[Ruta]):
    print('Test 3')
    print(diferencias_kms_meses_anyo(rutas))

def top_rutas_lejanas_test(rutas: list[Ruta], n: int, c: Coordenada, km_min: int = None) -> list[Ruta]:
    print('Test 4')
    print(top_rutas_lejanas(rutas, n, c, km_min))

def ciudades_top_tiempo_dificultad_test(rutas: list[Ruta], n: int = 3) -> dict[str, list[str]]:
    print('Test 5')
    print(ciudades_top_tiempo_dificultad(rutas, n))

def main():
    rutas = lee_rutas(r'data\rutas_motos.csv')
    # lee_rutas_test(r'data\rutas_motos.csv')
    # acumular_kms_por_meses_test(rutas)
    diferencias_kms_meses_anyo_test(rutas)
    # top_rutas_lejanas_test(rutas, 2, Coordenada(35.15, -8.76))
    # top_rutas_lejanas_test(rutas, 2, Coordenada(37.3826, -5.99629))
    # ciudades_top_tiempo_dificultad_test(rutas)

if __name__ == '__main__':
    main()