from partidas import*

def lee_partidas_test(fichero: str) -> list[Partida]:
    print(lee_partidas(fichero))

def main():
    lee_partidas_test('data\games.csv')

if __name__ == '__main__':
    main()