from baloncesto import*

def lee_partidos_test(fichero: str)->list[PartidoBasket]:
    print("Test de lee_datos_baloncesto:")
    print(f"Total registros leídos: {len(lee_partidos(fichero))}")
    print("Mostrando los tres primeros registros: ")
    for elemento in lee_partidos(fichero)[:3]:
        print(f"         {elemento}")

def main():
    partidos = lee_partidos(r"data\resultados_baloncesto.csv")
    lee_partidos_test(r"data\resultados_baloncesto.csv")

if __name__ == '__main__':
    main()