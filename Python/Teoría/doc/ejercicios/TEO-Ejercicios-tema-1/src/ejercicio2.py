from ejercicio1 import*

def calcula_estado_nutricional(peso, estatura):
    imc = calcula_imc(peso, estatura)
    res = ''
    if imc < 18.5:
        res = 'Bajo Peso'
    elif 18.5 <= imc < 30:
        res = 'Normal'
    elif 25 <= imc < 30:
        res = 'Sobrepeso'
    else:
        res = 'Obesidad' 
    return res

print(calcula_estado_nutricional(18, 1.7))
