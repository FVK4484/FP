#Ej1
#a)
def nota_teoría(t1, t2):
    t1 = a_cero(t1)
    t2 = a_cero(t2)
    nota_media = (t1 + t2) / 2
    return nota_media

def a_cero(x):
    if x == None:
        x = 0
    return x

#b)
def nota_cuatrimestre (notas_teoría, p):
    # Convertir valores None a 0
    t1 = a_cero(notas_teoría[0])
    t2 = a_cero(notas_teoría[1])
    p = a_cero(p)

    #Obtener nota del cuatrimestre
    #nota = notas_teoría * 0.2 + p * 0.8
    teoria = notas_teoría(t1,t2)
    if teoria(t1,t2) >=4:
         nota = teoria(t1, t2) * 0.2 + p * 0.8
    else:
        nota = 0

    #Devolver nota del cuatrimestre
    return nota

def nota_continua(notas_teoría, nota_práctica):
    #Calcular notas de los dos cuatrimestres
    nota_c1 = nota_cuatrimestre((notas_teoría[0], nota_teoría[1]), nota_práctica[0])
    nota_c2 = nota_cuatrimestre((notas_teoría[2], nota_teoría[3]), nota_práctica[1])
    #Calcular nota de la evaluación continua
    media = (nota_c1 + nota_c2) / 2
    if nota_c1 >= 4 and nota_c2 >=4:
        nota = media
    else:
        nota = min(4.0, media)
    return nota
