from mayday import*

def lee_desastres_test(ruta):
    print(f"Número de desastres leídos: {len(lee_desastres(ruta))}")
    print(f"Los dos primeros son: {lee_desastres(ruta)[:2]}")
    print(f"Los dos últimos son: {lee_desastres(ruta)[-2:]}")

def desastres_con_fallecidos_en_tierra_test(desastres, numero):
    print(f"Los {numero} desastres con más fallecidos en tierra son: {desastres_con_fallecidos_en_tierra(desastres, numero)}")

def decada_mas_colisiones_test(desastres):
    print(f"La década de {decada_mas_colisiones(desastres)[0]} fue la peor, con {decada_mas_colisiones(desastres)[1]} desastres con colisiones de aeronaves.")

def main():
    desastres = lee_desastres(r'FP_25_26\doc\examenes\Exámenes-curso-2025-2026\Examen-de-la-tercera-convocatoria-(octubre-2025)\data\Mayday.csv')
    # lee_desastres_test(r'FP_25_26\doc\examenes\Exámenes-curso-2025-2026\Examen-de-la-tercera-convocatoria-(octubre-2025)\data\Mayday.csv')
    # desastres_con_fallecidos_en_tierra_test(desastres, 5)
    decada_mas_colisiones_test(desastres)
if __name__ == '__main__':
    main()