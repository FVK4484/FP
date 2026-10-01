from repositorios import*

def test_recomendar_lenguajes (repos_list: List[Repositorio], repositorio: Repositorio) -> None: 
    print("test_recomendar_lenguajes", "="*80) 
    print(f"Para el repositorio {repositorio.nombre} que usa los lenguajes {repositorio.lenguajes} se recomiendan") 
    print(recomendar_lenguajes(repos_list, repositorio)) 
 
if __name__== "__main__": 
    repos_list = lee_repositorios(r"FP_25_26\doc\examenes\Exámenes-curso-2024-2025\Examen-de-la-tercera-convocatoria-diciembre-2024\data\repositorios.csv") 
    test_recomendar_lenguajes(repos_list, repos_list[0]) 
    test_recomendar_lenguajes(repos_list, repos_list[-1]) 
    test_recomendar_lenguajes(repos_list, repos_list[4])