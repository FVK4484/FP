from calificaciones import*
from calificaciones_ui import*
# a)
def test_nota_teoria(num1, num2):
    t1 = num1
    t2 = num2
    print(nota_teoria(t1, t2))

# b)
def test_nota_cuatrimestre(num1, num2, num3):
    t1 = num1
    t2 = num2
    p = num3
    print(nota_cuatrimestre(t1, t2, p))

# c)
def test_nota_continua(tuple1, tuple2):
    tupla1 = tuple1
    tupla2 = tuple2
    print(nota_continua(tupla1, tupla2))

# d)
def test_genera_mensaje(num1, num2, num3):
    cuatrimestre1 = num1  
    cuatrimestre2 = num2
    nota_continua = num3
    print(genera_mensaje(cuatrimestre1, cuatrimestre2, nota_continua))

def test_solicita_notas():
    print(solicita_notas())

def test_mostrar_notas(nombre, tupla, tupla2):
    mostrar_notas(nombre, tupla, tupla2)

if __name__ == "__main__":
    # a)
    # test_nota_teoria(9.1, 7.2)
    # test_nota_teoria(4.0, 6.0)
    # test_nota_teoria(4.0, 3.0)
    # test_nota_teoria(None, 3.0)
    # test_nota_teoria(9.0, None)
    # test_nota_teoria(None, None)

    # b)
    test_nota_cuatrimestre(9.1, 7.2, 8.1)
    test_nota_cuatrimestre(4.0, 6.0, 5.0)
    test_nota_cuatrimestre(4.0, 3.0, None)
    test_nota_cuatrimestre(None, 3.0, None)
    test_nota_cuatrimestre(9.0, None, 4.5)
    test_nota_cuatrimestre(9.0, None, None)
    test_nota_cuatrimestre(None, None, None)

    #c) 
    # test_nota_continua((9.6, 9.9, 10.0, 9.8), (9.7, 9.5))
    # test_nota_continua((4.4, 4.9, 5.1, 4.7), (4.6, 4.8))
    # test_nota_continua((4.0, 6.0, 4.0, 3.0), (5.0, None))
    # test_nota_continua((9.0, None, 4.0, 3.0), (4.5, None))
    # test_nota_continua((9.0, 5.0, 4.0, None), (4.5, None))

    # d)
    # test_genera_mensaje(6, 5, 6)
    # test_genera_mensaje(4, 6, 4)
    # test_genera_mensaje(7, 3, 4)
    # test_genera_mensaje(4, 3, 3.5)

    # e)
    # test_solicita_notas()

    test_mostrar_notas('Aitor', [4, 5, 6, 7], [6, 5])

 
