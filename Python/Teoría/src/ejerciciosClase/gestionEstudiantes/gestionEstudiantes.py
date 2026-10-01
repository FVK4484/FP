from typing import List, Dict

estudiantes : List[Dict[int, str]] = []
cursos: List[Dict[str, str]] = []
inscripciones: Dict[int, List[str]] = {}

def agregar_estudiante(id: int, nombre: str) -> None:
    for estudiante in estudiantes:
        if estudiante["id"] == id:
            print(f"El estudiante con ID {id} ya existe.")
            return
    estudiantes.append({"id": id, "nombre": nombre})
    print(f"Estudiante agregado: {nombre} (ID: {id})")

def agregar_curso(cod: str, nombre: str) -> None:
    for curso in cursos:
        if curso["código"] == cod:
            print(f"El curso con el código {cod} ya existe.")
            return
    cursos.append({"cod": cod, "nombre": nombre})
    print(f"Curso agregado: {nombre} (Código: {cod})")

def inscribir_estudiante(id: int, cod: List[str]) -> None:
    for inscripcion in inscripciones:
        if inscripcion["id"] == id:
            print(f"La inscripcion con ID {id} ya existe.")
            return
    inscripciones.append({"id": id, "codigo": cod})
    print(f"Inscripcion agregada: {id} (Código: {cod})")

def mostrar_estudiante() -> None:
    print(estudiantes)

def mostrar_cursos() -> None:
    print(cursos)

def mostrar_inscripciones() -> None:
    print(inscripciones)
