from typing import List
from mayday import *

def lee_desastres_test(fichero: str)->List[Vuelo]:
    print('Test leer_desastres ==================================================')
    print(f'Número de desastres leídos: {len(lee_desastres(fichero))}')
    print(f'Los dos primeros son: {lee_desastres(fichero)[:2]}')
    print(f'Los dos últimos son: {lee_desastres(fichero)[-2:]}')

def desastres_con_fallecidos_en_tierra_test(desastres:list[Desastre],n:int|None=None)->list[tuple[str,date,time,int]]:
    print('Test desastres_con_fallecidos_en_tierra ==================================================') 
    print(f'Los {n} desastres con más fallecidos en tierra son: {desastres_con_fallecidos_en_tierra(desastres, n)}')

def decada_mas_colisiones_test(desastres:list[Desastre]) -> tuple[int,int]:
    print("Test decada_mas_colisiones ==================================================")
    print(f"La década de {decada_mas_colisiones(desastres)[0]} fue la peor, con {decada_mas_colisiones(desastres)[1]} desastres con colisiones de aeronaves.")

def mayor_periodo_sin_desastres_test(desastres: list[Desastre],operacion: str|None = None) -> tuple[date, date, int]: 
    print("Test mayor_periodo_sin_desastres ==================================================")
    print(f"El mayor periodo sin desastres comienza el {mayor_periodo_sin_desastres(desastres, operacion)[0]}, termina el {mayor_periodo_sin_desastres(desastres, operacion)[1]} y dura {mayor_periodo_sin_desastres(desastres, operacion)[2]} dias.")

def estadisticas_por_operacion_test(desastres: list[Desastre], 
                               limite_tasa_supervivencia: float|None = None)->dict[str, tuple[int, float, float]]:
    print('Test estadisticas_por_operacion ==================================================')
    if limite_tasa_supervivencia == None:
        print(f'Las estadísticas por operación son: {estadisticas_por_operacion(desastres, limite_tasa_supervivencia)}')
    else:
        print(f'Las estadísticas por operación con tasa de supervivencia menor a {limite_tasa_supervivencia} son: {estadisticas_por_operacion(desastres, limite_tasa_supervivencia)}')

def main():
    desastres = lee_desastres('data\mayday.csv')
    # lee_desastres_test("data\mayday.csv")
    # desastres_con_fallecidos_en_tierra_test(desastres)
    # decada_mas_colisiones_test(desastres)
    # mayor_periodo_sin_desastres_test(desastres)
    # mayor_periodo_sin_desastres_test(desastres, 'Taking-off')
    # mayor_periodo_sin_desastres_test(desastres, 'Landing')
    estadisticas_por_operacion_test(desastres)
    estadisticas_por_operacion_test(desastres, 0.15)

if __name__ == '__main__':
    main()