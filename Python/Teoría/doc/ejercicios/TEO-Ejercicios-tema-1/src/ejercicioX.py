from datetime import datetime, date

# Ejericio1
def calcula_imc(peso, altura):
    imc = peso / altura**2
    return imc

# Ejercicio2
def calculo_estado_nutricional(peso, altura):
    imc = calcula_imc(peso, altura)
    res = ''
    if imc < 18.5:
        res = 'Tienes Bajo peso'
    elif 18.5 <= imc < 25:
        res = 'Tienes peso Normal'
    elif 25 <= imc < 30:
        res = 'Tienes Sobrepeso'
    else:
        res = 'Tienes Obesidad'
    return res

# Ejercicio3
def imprime_estados_nutricionales(lista):
    cont = 0
    for n in lista:
        peso = n[0]
        altura = n[1]

        imc = calcula_imc(peso, altura)
        estado_nutricional = calculo_estado_nutricional(peso, altura)

        cont += 1            
        
        print(f"El IMC de la persona {cont} es {imc}, y su estado nutricional es {estado_nutricional}.") 

# Ejercicio4
def lee_numeros():
    numeros = []
    cantidad = int(input("¿Cuantos números quiere añadir a la lista? "))
    for i in range(cantidad):
        numero = int(input(f"Introduce el número entero {i + 1}: "))
        numeros.append(numero)
    return numeros

# Ejercicio5
def calcula_dia_semana(fecha):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return dias_semana[fecha.weekday()]