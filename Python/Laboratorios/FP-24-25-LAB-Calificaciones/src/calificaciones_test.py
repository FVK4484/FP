from calificaciones import *
def test_nota_teoría(t1, t2):
    print("Prueba de la función nota_teoría")
    media = nota_teoría(t1, t2)
    print(f"la media de {t1} y {t2} es la {media}")

def test_nota_cuatrimestre(notas_teoría, p):
    print ("Prueba de la función nota_cuatrimestre")
    nota = nota_cuatrimestre(notas_teoría, p)
    print(f"{notas_teoría[0]}, {notas_teoría[1]}, ==> {nota}")

if __name__=='__main__':
    test_nota_teoría(9.1, 7.2)
    test_nota_teoría(4.0, 6.0)
    test_nota_teoría(4.0, 3.0) 
    test_nota_teoría(None, 3.0) 
    test_nota_teoría(9.0, None) 
    test_nota_teoría(None, None) 
    test_nota_cuatrimestre((9.1, 7.2), 8.1) 
    test_nota_cuatrimestre((4.0, 6.0), 5.0)
    test_nota_cuatrimestre((4.0, 3.0), None)
    test_nota_cuatrimestre((None, 3.0), None)  
    test_nota_cuatrimestre((9.0, None), 4.5)
