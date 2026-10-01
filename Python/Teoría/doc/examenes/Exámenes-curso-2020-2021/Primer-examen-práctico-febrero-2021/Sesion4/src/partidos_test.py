from partidos import*

def lee_resultados_test(ruta_fichero: str) -> list[Partido]:
    print("Test lee_resultados:")
    print(lee_resultados(ruta_fichero))

def selecciones_enfrentadas_israel_test(partidos: list[Partido], n: int = 3) -> list[str]:
    print("Test selecciones_enfrentadas_israel:")
    print(selecciones_enfrentadas_israel(partidos, n))

def main():
    partidos = lee_resultados(r"doc\examenes\Exámenes-curso-2020-2021\Primer-examen-práctico-febrero-2021\Sesion4\data\resultadosIsrael.csv")
    # lee_resultados_test(r"doc\examenes\Exámenes-curso-2020-2021\Primer-examen-práctico-febrero-2021\Sesion4\data\resultadosIsrael.csv")
    selecciones_enfrentadas_israel_test(partidos, 3)

if __name__ == '__main__':
    main()