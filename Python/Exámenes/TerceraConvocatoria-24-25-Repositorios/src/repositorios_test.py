from repositorios import*

def lee_repositorios_test(repositorios: List[Commit]) -> None:
    print(f"Se han leido {len(repositorios)} repositorios")
    print(f"Los dos primeros son {repositorios[:2]}")
    print(f"Los dos últimos son {repositorios[-2:]}")

def total_commits_por_anyo_test(repositorios:List[Repositorio])->Dict[int, int]:
    print(f"El total de commits por año para los repositorios públicos es {total_commits_por_anyo(repositorios)}")

def n_mejores_repos_por_tasa_crecimiento_test(repositorios: List[Repositorio], 
                n:Optional[int]=3)->List[Tuple[str,float]]:
    print(f"Los 3 mejores repositorios según su tasa de crecimiento son {n_mejores_repos_por_tasa_crecimiento(repositorios, n)}")

def main():
    repositorios = lee_repositorios(r"data\repositorios.csv")
    # lee_repositorios_test(repositorios)
    # total_commits_por_anyo_test(repositorios)
    n_mejores_repos_por_tasa_crecimiento_test(repositorios, 3)

if __name__ == '__main__':
    main()

