from compras import*

def test_lee_compras(compras):
    print("Prueba de la función lee_compras")
    print(f"Hay {len(compras)} compras.")
    print(f"Las tres primeras son : {compras[:3]}.")

'''def test_compra_maxima_minima_provincia(compra_máxima, compra_mínima):
    print("Prueba de la función compra_maxima_minima_provincia")
    print(f"Importe máximo de la provincia de Huelva : {compra_máxima}. Importe mínimo : {compra_mínima}")
    print(f"Importe máximo de la provincia None : {compra_máxima}. Importe mínimo : {compra_mínima}")'''

'''def test_hora_menos_afluencia ():
    pass'''

if __name__ == '__main__':
    compras = lee_compras("data/compras.csv")
    test_lee_compras(compras)
    # test_compra_maxima_minima_provincia(compras)
    # test_hora_menos_afluencia(compras)
