from entrenos import*

def test_lee_entrenos(fichero):
    print(f'Los 3 primeros registros son: {lee_entrenos(fichero)[:3]}')
    print(f'Los 3 últimos registros son: {lee_entrenos(fichero)[-3:]}')

def test_tipo_entreno(entrenos):
    print(tipos_entreno(entrenos))

def test_entrenos_duracion_superior(entrenos, d):
    print(entrenos_duracion_superior(entrenos, d))

def test_suma_calorias(entrenos, f_inicio, f_fin):
    print(suma_calorias(entrenos, f_inicio, f_fin))

def test_entrenamiento_mas_kms(entrenos):
    print(entrenamiento_mas_kms(entrenos))

def test_duracion_media_entrenos(entrenos, anyo, mes):
    print(duracion_media_entrenos(entrenos, anyo, mes))

def test_enfrentamiento_mas_calorico(entrenos):
    print(enfrentamiento_mas_calorico(entrenos))

def test_num_entrenamientos_efectivos(entrenos, calorias):
    print(f'Hay {num_entrenamientos_efectivos(entrenos, calorias)} entrenos con mas de {calorias} calorias.')

def test_existe_tipo_entrenamiento(entrenos, tipo):
    print(existe_tipo_entrenamiento(entrenos, tipo))

if __name__ == "__main__":
    datos = lee_entrenos(r'doc\laboratorio\LAB-Entrenos\data\entrenos.csv')
    test_lee_entrenos(r'doc\laboratorio\LAB-Entrenos\data\entrenos.csv')
    # test_tipo_entreno(datos)
    # test_entrenos_duracion_superior(datos, 126)
    # test_suma_calorias(datos, '2/5/2021 22:20', '11/6/2021 17:38')
    # test_entrenamiento_mas_kms(datos)
    # test_duracion_media_entrenos(datos, 2019, 4)
    # test_enfrentamiento_mas_calorico(datos)
    # test_num_entrenamientos_efectivos(datos, 357)
    test_existe_tipo_entrenamiento(datos, 'Andar')
