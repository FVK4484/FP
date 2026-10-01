from nombres import*

def test_lee_frecuencias_nombre(datos):
    print(f"Se han leído {len(datos)} frecuencias")
    print(f"Las tres primeras son: {datos[:3]}")
    print(f"Las tres últimas son: {datos[-3:]}")

if __name__ == '__main__':
    datos = lee_frecuencias_nombres(
        'data/frecuencias_nombres.csv')
    test_lee_frecuencias_nombre(datos)

