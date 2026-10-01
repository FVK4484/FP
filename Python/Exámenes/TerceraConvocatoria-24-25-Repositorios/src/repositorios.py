from collections import defaultdict
import csv
from typing import NamedTuple,List,Set,Tuple,Dict,Optional 
from datetime import datetime,date 
 
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

# EJERCICIO 1. (1,75 puntos)

def lee_repositorios(csv_filename: str) -> List[Repositorio]:
    lista = []
    with open(csv_filename, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for nombre, propietario, lenguajes, privado, commits in lector:
            lenguajes = parsea_lenguajes(lenguajes)
            privado = parsea_privado(privado)
            commits = parsea_commits(commits)
            tupla = Repositorio(nombre, propietario, lenguajes, privado, commits)
            lista.append(tupla)
        return lista

def parsea_lenguajes(lenguajes: str)->Set[str]:
    conjunto = set()
    lenguajes = lenguajes.replace('"', "").replace('"', "")
    for lenguaje in lenguajes.split(","):
        conjunto.add(lenguaje)
    return(conjunto)

def parsea_privado(privado: str)->bool:
    res = False
    if (privado == 'True'):
        res = True
    return res

def parsea_commits(commits: str)->List[Commit]:
    lista = []
    commits = commits.replace("[", "").replace("]", "")
    if len(commits) > 0:
        for commit in commits.split(";"):
            lista.append(parsea_commit(commit))
    return lista

def parsea_commit(commit: str)->Commit:
    if len(commit) > 0:
        id, mensaje, fecha_hora = commit.split("#")
        fecha_hora = parsea_fecha_hora(fecha_hora)
    return Commit(id, mensaje, fecha_hora)

def parsea_fecha_hora(fecha_hora: str)->datetime:
    return datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M:%S")

# EJERCICIO 2.

# 2. total_commits_por_anyo: dada una lista de tuplas de tipo Repositorio, devuelve un diccionario en el que 
# las claves son los años, y los valores el número total de commits registrados en el año dado como clave para 
# los repositorios públicos. (1,25 puntos)

def total_commits_por_anyo(repositorios:List[Repositorio])->Dict[int, int]:
    dicc = defaultdict(int)
    for repositorio in repositorios:
        for commit in repositorio.commits:
            if (repositorio.privado == False):
                dicc[commit.fecha_hora.year] += 1
    return dicc

# EJERCICIO 3.

# 3. n_mejores_repos_por_tasa_crecimiento:  dada  una  lista  de  tuplas  de  tipo  Repositorio  y  un  número 
# entero n (con valor por defecto igual a 3), devuelve una lista con los n nombres de los repositorios y sus tasas 
# de crecimiento más altas. (1,75 puntos)

def n_mejores_repos_por_tasa_crecimiento(repositorios: List[Repositorio], 
                n:Optional[int]=3)->List[Tuple[str,float]]:
    return sorted(((repositorio.nombre, calcular_tasa_crecimiento(repositorio))for repositorio in repositorios), key = lambda x:x[1], reverse=True)[:n]
    
# Antes de implementar la función anterior, implemente la función auxiliar que se describe a continuación: 
# • calcular_tasa_crecimiento: dado un Repositorio, devuelve su tasa de crecimiento. La tasa de 
# crecimiento de  un repositorio  se  define  como la  ratio entre  el número de  commits y el número de 
# días transcurridos entre el primer y el último commit (los commits están ordenados en el archivo). Si 
# el repositorio tiene menos de 2 commits, o si tiene 2 o más commits pero no ha pasado al menos un 
# día entre el primero y el último, la tasa se considera cero.

def calcular_tasa_crecimiento(repositorio: Repositorio) -> float:
    if len(repositorio.commits) > 1:
        dias_entre_repo = dias_entre_commit(repositorio.commits[0].fecha_hora, repositorio.commits[-1].fecha_hora)
        if (dias_entre_repo == 0):
            tasa_crecimiento = 0
        else:
            num_commits = len(repositorio.commits)
            tasa_crecimiento = num_commits / dias_entre_repo
    else: 
        tasa_crecimiento = 0
    return tasa_crecimiento

def dias_entre_commit(f1: datetime, f2: datetime)->int:
    return (f2 - f1).days

print(calcular_tasa_crecimiento(Repositorio(nombre='LAB-Calificaciones', propietario='student1', lenguajes={'Java', 'Python'}, privado=True, commits=[Commit(id='a123456', mensaje='Initial setup', fecha_hora=datetime(2020, 10, 6, 8, 0)), Commit(id='a123457', mensaje='Added features', fecha_hora=datetime(2022, 10, 6, 9, 0))])))


# Ayuda: Los días transcurridos entre dos variables dt1 y dt2, de tipo datetime, se pueden calcular 
# como (dt2-dt1).days.

# EJERCICIO 4.

# 4. recomendar_lenguajes: dada una lista de tuplas de tipo Repositorio y un repositorio específico, devuelve 
# un  conjunto  con  los  lenguajes  de  programación  recomendados  para  dicho  repositorio.  Los  lenguajes 
# recomendados  son  aquellos  que  se  usan  en  repositorios  similares  al  repositorio  dado. Se  considera  que  un 
# repositorio es similar al dado si comparte al menos uno de los lenguajes de programación con el repositorio 
# dado. Por ejemplo, si queremos hacer una recomendación para el repositorio "LAB-FP", cuyo lenguaje es Java, 
# podemos  considerar  similar  el  repositorio  "LAB-Calificaciones",  que  utiliza  Java  y  Python,  ya  que  ambos
# comparten el lenguaje Java. En este caso, se recomendaría Python como nuevo lenguaje para el repositorio 
# "LAB-FP". (2,5 puntos)

def recomendar_lenguajes (repositorios:List[Repositorio],  
                          repositorio:Repositorio)->Set[str]:
    pass
