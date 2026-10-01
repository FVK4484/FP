from partidas import*

def lee_peliculas_test(fichero: str) -> List[Partida]:
    print("1. Test de lee_peliculas:")
    print(f"Total registros leídos: {len(lee_partidas(fichero))}")
    print(f"Mostrando los tres primeros registros: {lee_partidas(fichero)[:3]}")

def victoria_mas_rapida_test(partidas: List[Partida]) -> Tuple[str, str, float]:
    print("2. Test victora_mas_rapida")
    print(f"La partida más rápida fue una entre {victoria_mas_rapida(partidas)[0]} y {victoria_mas_rapida(partidas)[1]} que duró {victoria_mas_rapida(partidas)[2]} segundos.")

def top_ratio_medio_personajes_test(partidas: List[Partida], n: int) -> List[str]:
    print("3. Test de top_ratio_medio_personajes")
    print(f"El top 3 de ratios medios es: {top_ratio_medio_personajes(partidas, n)}")



def main():
    partidas = lee_partidas(r"FP_25_26\doc\laboratorio\LAB-Street-Fighter\data\games.csv")
    # lee_peliculas_test(r"FP_25_26\doc\laboratorio\LAB-Street-Fighter\data\games.csv")
    # victoria_mas_rapida_test(partidas)
    top_ratio_medio_personajes_test(partidas, 3)

if __name__ == '__main__':
    main()
