from autocares import*

def lee_autocares_test(ruta:str)->list[Autocar]:
    print(f'Número de registros leídos: {len(lee_autocares(ruta))}')
    print(f'Los 4 primeros registros son {lee_autocares(ruta)[:4]}')

def viaje_mas_kilometros_test(autocares:list[Autocar], marcas:set[str]|None=None)-> tuple[str, Viaje]:
    if marcas is None:
        print(f"El viaje con más kilómetros entre las marcas {marcas} es: {viaje_mas_kilometros(autocares, marcas)}")
    else:
        print(f"El viaje con más kilómetros es: {viaje_mas_kilometros(autocares, marcas)}")

def autocar_mayor_beneficio_test(autocares:list[Autocar])-> tuple[str,str,float]:
    print(f'El autocar con mayor beneficio es: {autocar_mayor_beneficio(autocares)}')


def main():
    autocares = lee_autocares(r'data\autocares.csv')
    lee_autocares_test(r'data\autocares.csv')
    # viaje_mas_kilometros_test(autocares)
    # viaje_mas_kilometros_test(autocares, {'IRIZAR', 'SETRA', 'MERCEDES-BENZ'})
    autocar_mayor_beneficio_test(autocares)


if __name__ == '__main__':
    main()