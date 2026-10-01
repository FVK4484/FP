from suscripciones import*
from collections.abc import Iterable

def mostrar_iterable (it: Iterable) -> None: 
    for elem in it: 
        print(f"\t{elem}") 
 
def test_lee_suscripciones(suscripciones: list[Suscripcion]) -> None: 
    print(f"Total suscripciones: {len(suscripciones)}") 
    print("Las tres primeras") 
    mostrar_iterable(suscripciones[:3]) 

def test_suscripciones_mas_rentables(suscripciones: list[Suscripcion], 
         n: int = 3, 
         tipos_plan: set[str] |None = None) -> None: 
    print (f"Las {n} suscripciones más rentables con tipos_plan {tipos_plan} son") 
    res = suscripciones_mas_rentables(suscripciones, n, tipos_plan) 
    mostrar_iterable(res)
 
if __name__ == "__main__": 
    suscripciones = lee_suscripciones(r"doc\examenes\Exámenes-curso-2024-2025\Examen-del-primer-cuatrimestre-enero-2025\Sesion3\data\Suscripciones.csv") 
    test_lee_suscripciones(suscripciones)
    test_suscripciones_mas_rentables(suscripciones) 
    test_suscripciones_mas_rentables(suscripciones, tipos_plan = {'Básico'})