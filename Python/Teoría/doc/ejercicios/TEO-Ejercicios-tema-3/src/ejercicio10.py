from collections import namedtuple
import csv
from datetime import datetime

Libro = namedtuple("Libro", "isbn,titulo,autor,fecha_publicacion,precio,disponible")


def lee_libros(ruta_csv):
    with open(ruta_csv, encoding="utf-8") as f:
        res = []
        lector = csv.reader(f)
        next(lector)
        for isbn, titulo, autor, fecha_publicacion, precio, disponible in lector:
            fecha_publicacion = datetime.strptime(fecha_publicacion, "%d/%m/%Y").date()
            precio = float(precio)
            disponible = disponible == "Sí"
            res.append(
                Libro(isbn, titulo, autor, fecha_publicacion, precio, disponible)
            )
        return res


# TODO: Implemente las funciones solicitadas en el enunciado
def autores_disponibles(libros, inicial):
    return sorted(set(libro.autor for libro in libros if libro.autor[0] == inicial and libro.disponible == True))

def titulos_baratos_actuales(libros):
    return [libro.titulo for libro in libros if libro.precio < 20 and (libro.fecha_publicacion).year >= 2001]

def media_precios(lista_libros, palabra):
    precios_coincidentes = []
    palabra_minusculas = palabra.lower()

    for libro in lista_libros:
        if palabra_minusculas in libro.titulo.lower():
            precios_coincidentes.append(libro.precio)

    if len(precios_coincidentes) > 0:
        return sum(precios_coincidentes) / len(precios_coincidentes)
    else:
        return None

def libro_mas_reciente(libros):
    return list(libro for libro in libros if max(libro.fecha_publicacion for libro in libros) == libro.fecha_publicacion)

if __name__ == "__main__":
    libros = lee_libros(r"doc\ejercicios\TEO-Ejercicios-tema-3\data\libreria.csv")
    print(f"Se han leído {len(libros)} libros.")

    print("Autores disponibles:", autores_disponibles(libros, "M"))
    print("Titulos baratos actuales:", titulos_baratos_actuales(libros))
    print(
        "Media de precios de libros con la palabra 'El':", media_precios(libros, "El")
    )
    print("Libro más reciente:", libro_mas_reciente(libros))
