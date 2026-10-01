# a)
def nota_teoria(t1, t2):
    nota = 0
    if t1 == None and t2 == None:
        nota = 0
    elif t1 == None:
        t1 = 0
        nota = (t1 + t2) /2
    elif t2 == None:
        t2 = 0 
        nota = (t1 + t2) /2
    else:
        nota = (t1 + t2) /2
    return nota

# b)
def nota_cuatrimestre(t1, t2, p):
    teoria = nota_teoria(t1, t2)
    nota = 0
    if p == None and t1 == None and t2 == None:
        nota = 0
    elif p == None and t2 == None:
        p = 0
        t2 = 0
        if teoria < 4:
            nota = 0
        else:
            nota = 0.15 * t1 + 0.15 * t2 + 0.7 * p
    elif p == None and t1 == None:
        p = 0
        t1 = 0
        if teoria < 4:
            nota = 0
        else:
            nota = 0.15 * t1 + 0.15 * t2 + 0.7 * p
    elif p == None:
        p = 0
        if teoria < 4:
            nota = 0
        else:
            nota = 0.15 * t1 + 0.15 * t2 + 0.7 * p
    elif t1 == None:
        t1 = 0
        if teoria < 4:
            nota = 0
        else:
            nota = 0.15 * t1 + 0.15 * t2 + 0.7 * p
    elif t2 == None:
        t2 = 0
        if teoria < 4:
            nota = 0
        else:
            nota = 0.15 * t1 + 0.15 * t2 + 0.7 * p
    else:
        nota = 0.15 * t1 + 0.15 * t2 + 0.7 * p
    return nota

# c)
def nota_continua(tupla1, tupla2):
    cuatrimestre1 = nota_cuatrimestre(tupla1[0], tupla1[1], tupla2[0])
    cuatrimestre2 = nota_cuatrimestre(tupla1[2], tupla1[3], tupla2[1])
    nota = 0
    if cuatrimestre1 == None or cuatrimestre2 == None:
        nota = 0
    elif cuatrimestre1 and cuatrimestre2 >= 5:
        nota = (cuatrimestre1 + cuatrimestre2) / 2
    else:
        nota = (cuatrimestre1 + cuatrimestre2) / 2
        if nota >= 5:
            nota = nota
    return nota

# d)
def genera_mensaje(cuatrimestre1, cuatrimestre2, nota_continua):
    frase = ""
    if nota_continua >= 5:
        frase = "¡Enhorabuena! Has aprobado la asignatura."
    elif cuatrimestre1 < 5 and cuatrimestre2 >= 5:
        frase = "Debes recuperar el primer cuatrimestre."
    elif cuatrimestre2 < 5 and cuatrimestre1 >= 5:
        frase = "Debes recuperar el segundo cuatrimestre."
    else:
        frase = "Debes recuperar toda la asignatura."
    return frase
