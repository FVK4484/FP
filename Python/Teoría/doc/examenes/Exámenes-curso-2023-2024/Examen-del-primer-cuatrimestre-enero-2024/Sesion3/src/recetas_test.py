from recetas import*

def test_lee_recetas(fichero):
    recetas = lee_recetas(fichero)
    print(f"Recetas leídas: {len(recetas)}")
    print(f"Mostrando las 2 primeras recetas: {recetas[:2]}")
    print(f"Mostrando las 2 ultimas recetas: {recetas[-2:]}")

if __name__ == '__main__':
    test_lee_recetas(r'FP_25_26\doc\examenes\Exámenes-curso-2023-2024\Examen-del-primer-cuatrimestre-enero-2024\Sesion3\data\CSV de la sesión 3.csv')