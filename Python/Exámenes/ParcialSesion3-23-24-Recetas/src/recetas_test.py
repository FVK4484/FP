from recetas import*

def lee_recetas_test(filename: str) -> List[Receta]:
    print('=== TEST EJERCICIO 1 ========================================')
    print(f'FRecetas leídas: {len(lee_recetas(filename))}')
    print(f'Mostrando las 2 primeras recetas: {(lee_recetas(filename)[:2])}')
    print(f'Mostrando las 2 últimas recetas: {lee_recetas(filename)[-2:]}')

def receta_mas_barata_test(recetas: List[Receta],
                      tipos: Set[str],
                      n: Optional[int] = None) -> Receta:
    print('=== TEST EJERCICIO 2======================================== ')
    print(f'La receta más barata de las {n} con menos calorías de los tipos {tipos} es: {receta_mas_barata(recetas, tipos, n)}')

def obten_ingredientes_test(recetas: List[Receta],
                          mes1: Optional[int] = None,
                          mes2: Optional[int] = None) -> Set[str]:
    print("=== TEST EJERCICIO 3========================================")
    print(f'Hay {len(obten_ingredientes(recetas, mes1, mes2))} ingredientes de las recetas cuyos meses de creación están en el intervalo [{mes1}, {mes2}) y son {obten_ingredientes(recetas,mes1,mes2)}')

def recetas_con_precio_menor_promedio_test(recetas: List[Receta], n: int)-> List[Tuple[str, int]]:
    print("=== TEST EJERCICIO 4========================================")
    print(f"Las {n} recetas con precio menor que el promedio son: ")
    for numero, tupla in enumerate(recetas_con_precio_menor_promedio(recetas, n)):
        print(f"{numero}-{tupla}")

def main():
    recetas = lee_recetas('data\CSV de la sesión 3.csv')
    # lee_recetas_test('data\CSV de la sesión 3.csv')
    # receta_mas_barata_test(recetas, {'Postre', 'Entrante'})
    # receta_mas_barata_test(recetas, {'Plato principal'}, 5)
    # obten_ingredientes_test(recetas, None, None)
    # obten_ingredientes_test(recetas, 2, 4)
    # obten_ingredientes_test(recetas, 2, None)
    # obten_ingredientes_test(recetas, None, 3)
    recetas_con_precio_menor_promedio_test(recetas, 5)

if __name__ == '__main__':
    main()

