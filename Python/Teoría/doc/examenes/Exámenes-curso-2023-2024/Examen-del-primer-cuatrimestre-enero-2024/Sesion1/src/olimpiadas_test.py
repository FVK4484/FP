from olimpiadas import*

def lee_registros_olimpiadas_test(ruta_fichero: str) -> list[Registro]:
    print("TEST EJERCICIO 1 ######################################## ")
    print(f"Se han leído {len(lee_registros_olimpiadas(ruta_fichero))} registros")
    print(f"Los dos primeros son: {enumerate, lee_registros_olimpiadas(ruta_fichero)[:2]} ")
    print(f"Los dos últimos son: {enumerate, lee_registros_olimpiadas(ruta_fichero)[-2:]} ")

def deportes_ambos_generos_test(registros: list[Registro], anyo: int) -> set:
    print("TEST EJERCICIO 2 ########################################")
    print(f"Los deportes que han tenido competición masculina y femenina en el año {anyo} son: {deportes_ambos_generos(registros, anyo)}")

def deportes_mas_frecuentes_test(registros: List[Registro], n: int, genero: str) -> List[Tuple[str, int]]:
    print(f"Los {n} deportes más frecuentes para el género {genero} son: {deportes_mas_frecuentes(registros, n, genero)}")

def deporte_con_mas_paises_distintos_con_oro_test(registros: List[Registro], genero: Optional[str] = None) -> str:
    print("TEST EJERCICIO 4 ########################################")
    print(f"El deporte para el género {genero} en el que hay más países distintos con medallas de oro es: {deporte_con_mas_paises_distintos_con_oro(registros, genero)}")

def main():
    registros = lee_registros_olimpiadas(r"doc\examenes\Exámenes-curso-2023-2024\Examen-del-primer-cuatrimestre-enero-2024\Sesion1\data\CSV de la sesión 1.csv")
    # lee_registros_olimpiadas_test(r"doc\examenes\Exámenes-curso-2023-2024\Examen-del-primer-cuatrimestre-enero-2024\Sesion1\data\CSV de la sesión 1.csv")
    # deportes_ambos_generos_test(registros, 1984)
    # deportes_ambos_generos_test(registros, 1992)
    # # deportes_ambos_generos_test(registros, 2000)
    # deportes_mas_frecuentes_test(registros, 4, "HOMBRE")
    # deportes_mas_frecuentes_test(registros, 5, "MUJER")
    deporte_con_mas_paises_distintos_con_oro_test(registros, None)
    deporte_con_mas_paises_distintos_con_oro_test(registros, "HOMBRE")
    deporte_con_mas_paises_distintos_con_oro_test(registros, "MUJER")

if __name__ == '__main__':
    main()