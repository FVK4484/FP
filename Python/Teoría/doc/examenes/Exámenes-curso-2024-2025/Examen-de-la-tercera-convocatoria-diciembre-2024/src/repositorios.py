from collections import defaultdict
from typing import NamedTuple,List,Set,Tuple,Dict,Optional 
from datetime import datetime,date 
import csv
 
Commit = NamedTuple("Commit",      
       [("id", str), # Identificador alfanumérico del commit 
        ("mensaje", str), # Mensaje asociado al commit 
        ("fecha_hora", datetime) # Fecha y hora en la que se registró el commit 
       ]) 
Repositorio = NamedTuple("Repositorio",      
      [("nombre", str),  # Nombre del repositorio 
       ("propietario", str), # Nombre del usuario propietario 
       ("lenguajes", Set[str]),  # Conjunto de lenguajes usados 
       ("privado", bool),  # Indica si es privado o público 
       ("commits", List[Commit])  # Lista de commits realizados 
       ])

# EJERCICIO 1

def lee_repositorios(csv_filename: str) -> List[Repositorio]: 
    repositorios = []  
    with open(csv_filename,  encoding='utf-8') as csvfile: 
        reader = csv.reader(csvfile) 
        next(reader) 
        for nombre, propietario, lenguajes, privado, commits in reader:            
            commits = parse_commits(commits) 
            lenguajes = parse_lenguajes(lenguajes) 
            privado = parse_bool(privado) 
            repositorio = Repositorio( 
                nombre, propietario, lenguajes, privado, commits) 
            repositorios.append(repositorio) 
    return repositorios 
 
def parse_lenguajes(lenguajes_str: str) -> Set[str]: 
    return set(lenguajes_str.split(',')) 
 
def parse_bool(privado_str: str) -> bool: 
    res = None 
    privado = privado_str.lower() 
    if privado == "true": 
        res = True 
    elif privado == "false": 
        res = False 
    return res 
 
def parse_commits(commits_str: str) -> List[Commit]: 
    commits_str= commits_str.replace("[","").replace("]","").strip() 
    res = []                         
    if len(commits_str) > 0: 
        commits_list = commits_str.split(";") 
        res = [parse_commit(commit) for commit in commits_list] 
    return res 
     
def parse_commit(commit_str: str) -> Commit: 
    id, mensaje, fecha_hora_str = commit_str.split('#') 
    return Commit( 
        id = id.strip(), 
        mensaje = mensaje.strip(), 
        fecha_hora = parse_fecha_hora(fecha_hora_str) 
    ) 
 
def parse_fecha_hora(fecha_hora_str: str) -> datetime: 
    return datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S")


# EJERCICIO 2

def total_commits_por_anyo(repositorios:List[Repositorio])->Dict[int, int]:
    dicc = defaultdict(int)
    for repositorio in repositorios:
        if repositorio.privado == False:
            for commit in repositorio.commits:
                dicc[commit.fecha_hora.year] += 1
    return dicc

# EJERCICIO 3

def n_mejores_repos_por_tasa_crecimiento(repositorios: List[Repositorio], n: int=3) -> List[Tuple[str, float]]:
    return sorted(((repo.nombre, calcular_tasa_crecimiento (repo)) 
                   for repo in repositorios), 
                   key=lambda t:t[1], reverse=True) [:n] 
 
def calcular_tasa_crecimiento(repositorio: Repositorio) -> float: 
    dias = calcular_dias_entre_commits(repositorio.commits) 
    tasa = 0 
    if dias > 0: 
        tasa = len(repositorio.commits) / dias 
    return tasa 
 
def calcular_dias_entre_commits(commits: List[Commit]) -> int: 
    res = 0 
    if (len(commits) > 1): 
        res = (commits[-1].fecha_hora - commits[0].fecha_hora).days 
    return res

# EJERCICIO 4

def recomendar_lenguajes(repositorios: List[Repositorio], repositorio:Repositorio) -> Set[str]: 
    res = set() 
    for repo in repositorios: 
        if repo.nombre != repositorio.nombre: 
            if (son_similares(repositorio, repo)): 
                res = res.union(repo.lenguajes - repositorio.lenguajes) 
    return res 
 
def son_similares(repositorio1: Repositorio, repositorio2: Repositorio) -> bool: 
    lenguajes_comunes = repositorio1.lenguajes.intersection(repositorio2.lenguajes) 
    return len(lenguajes_comunes) > 0