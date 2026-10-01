from got import*

def test_lee_batallas(fichero: str)->list[BatallaGOT]:
    print('Test 1')
    print(lee_batallas(fichero)[-1])

def test_reyes_mayor_menor_ejercito(batallas: list[BatallaGOT])->tuple[str, str]:
    print('Test 2')
    print(reyes_mayor_menor_ejercito(batallas))

def test_batallas_mas_comandantes(batallas, regiones=None, n=None):
    print('Test 3')
    print(batallas_mas_comandantes(batallas, regiones, n))

def test_rey_mas_victorias(batallas, rol='ambos'):
    print('Test 4')
    print(rey_mas_victorias(batallas, rol))

def test_rey_mas_victorias_por_region(batallas: list[BatallaGOT], rol: str = 'ambos')->dict[str, list[str]]:
    print('Test 5')
    print(rey_mas_victorias_por_region(batallas, rol))

def main():
    batallas = lee_batallas(r'data\battles.csv')
    # print(batallas)
    # test_lee_batallas(r'data\battles.csv')
    # test_reyes_mayor_menor_ejercito(batallas)
    # test_batallas_mas_comandantes(batallas, {'The North', 'The Riverlands'}, 4)
    test_rey_mas_victorias(batallas, 'atacante')
    test_rey_mas_victorias_por_region(batallas, 'atacante')

if __name__ == '__main__':
    main()