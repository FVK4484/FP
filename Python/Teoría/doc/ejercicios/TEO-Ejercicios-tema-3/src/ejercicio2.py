

def imprime_diccionario(diccionario, ancho = 30):
    for elemento in diccionario:
        print(f'{elemento} ===> {diccionario[elemento]}')

precios_productos = {
    "manzana": 0.5,
    "plátano": 0.3,
    "naranja": 0.6,
    "uva": 1.2,
    "fresa": 2.5
}

imprime_diccionario(precios_productos)
