from motoFP import*

def lee_carreras_test(filename: str) -> list[CarreraFP]:
    carreras = lee_carreras(filename)
    print('Test lee_carreras')
    print(f'Número de carreras leídas: {len(carreras)}') 
    print(f'Las dos primeras son: {carreras[:2]}')
    print(f'Las dos ultimas son: {carreras[-2:]}')

def main():
    # carreras = lee_carreras(r'FP_25_26\doc\examenes\Exámenes-curso-2024-2025\Examen-del-primer-cuatrimestre-enero-2025\Sesion1\data\mundial_motofp.csv')
    lee_carreras_test(r'FP_25_26\doc\examenes\Exámenes-curso-2024-2025\Examen-del-primer-cuatrimestre-enero-2025\Sesion1\data\mundial_motofp.csv')

if __name__ == '__main__':
    main()