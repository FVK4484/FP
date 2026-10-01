from extranjeria import*

def lee_datos_extranjeria_test(ruta_fichero: str) -> list[RegistroExtranjeria]:
    print("TEST DE LA FUNCIÓN lee_datos_extranjeria:")
    print(f"Leídos {len(lee_datos_extranjeria(ruta_fichero))} registros.")
    print("Mostrando los 3 primeros:")
    print(lee_datos_extranjeria(ruta_fichero)[:3])
    print("Mostrando los 3 últimos:")
    print(lee_datos_extranjeria(ruta_fichero)[-3:])
    print("##############################################################")

def numero_nacionalidades_distintas_test(registros: list[RegistroExtranjeria]) -> int:
    print("TEST DE LA FUNCIÓN numero_nacionalidades_distintas:")
    print(f"Hay {numero_nacionalidades_distintas(registros)} nacionalidades distintas en los datos.")
    print("##############################################################")

def secciones_distritos_con_extranjeros_nacionalidades_test(registros: list[RegistroExtranjeria], paises: Set) -> list[tuple[str, str]]:
    print("TEST DE LA FUNCIÓN secciones_distritos_con_extranjeros_nacionalidades:")
    print(f"Hay {len(secciones_distritos_con_extranjeros_nacionalidades(registros, paises))} secciones de distritos con residentes cuya procedencia es {paises}")
    print(f"Mostrando 3 secciones: {secciones_distritos_con_extranjeros_nacionalidades(registros, paises)[:3]}")
    print("##############################################################")

def total_extranjeros_por_pais_test(registros: list[RegistroExtranjeria]) -> dict[str:int]:
    print("TEST DE LA FUNCIÓN total_extranjeros_por_pais:")
    print("Mostrando el número de residentes para algunos países de procedencia:")
    for pais, extranjeros in total_extranjeros_por_pais(registros).items():
        print(f"{pais} : {extranjeros}")
    print("##############################################################")
          
def top_n_extranjeria_test(registros: list[RegistroExtranjeria], n: int | int = 3) -> list[tuple[str, int]]:
    print("TEST DE LA FUNCIÓN top_n_extranjeria:")
    print(f"Mostrando los {n} países de los que proceden más residentes:")
    print(top_n_extranjeria(registros, n))
    print("##############################################################")

def barrio_mas_multicultural_test(registros: list[RegistroExtranjeria]) -> str:
    print("TEST DE LA FUNCIÓN barrio_mas_multicultural:")
    print(f"El barrio más multicultural de sevilla es {barrio_mas_multicultural(registros)}")
    print("##############################################################")

def barrio_con_mas_extranjeros_test(registros: list[RegistroExtranjeria], tipo = None) -> str:
    print("TEST DE LA FUNCIÓN barrio_con_mas_extranjeros:")
    print(f"El barrio con más residentes extranjeros es {barrio_con_mas_extranjeros(registros, None)}")
    print(f"El barrio con más hombres residentes extranjeros es {barrio_con_mas_extranjeros(registros, "Hombres")}")
    print(f"El barrio con más mujeres residentes extranjeras es {barrio_con_mas_extranjeros(registros, "Mujeres")}")
    print("##############################################################")

def pais_mas_representado_por_distrito_test(registros: list[RegistroExtranjeria]) -> dict[str : str]:
    print("TEST DE LA FUNCIÓN pais_mas_representado_por_distrito:")
    print("Los países con más residentes en cada distrito son los siguientes:")   
    for distrito, pais in pais_mas_representado_por_distrito(registros):
        print(f"Distrito: {distrito} => {pais}")
    print("##############################################################")

def main():
    registros = lee_datos_extranjeria(r"doc\laboratorio\LAB-Extranjeria\data\extranjeriaSevilla.csv")
    # lee_datos_extranjeria_test(r"doc\laboratorio\LAB-Extranjeria\data\extranjeriaSevilla.csv")
    # numero_nacionalidades_distintas_test(registros)
    # secciones_distritos_con_extranjeros_nacionalidades_test(registros, {'ITALIA', 'ALEMANIA'})
    total_extranjeros_por_pais_test(registros)
    # top_n_extranjeria_test(registros, 5)
    # barrio_mas_multicultural_test(registros)
    # barrio_con_mas_extranjeros_test(registros)
    # pais_mas_representado_por_distrito_test(registros)

if __name__ == "__main__":
    main()