from ejercicioX import*

def test_calcula_imc():
    peso = float(input("Escriba un peso: "))
    altura = float(input("Escriba una altura: "))
    print(calcula_imc(peso, altura))

def test_calculo_estado_nutricional():
    peso = float(input("Escriba un peso: "))
    altura = float(input("Escriba una altura: "))
    print(calculo_estado_nutricional(peso, altura))

def test_imprime_estados_nutricionales(lista):
    print(imprime_estados_nutricionales(lista))

def test_lee_numeros():
    print(lee_numeros())

def test_calcula_dia_semana():
    fecha = input("Introduce tu fecha de nacimiento (dd/mm/yyyy): ")
    fecha_nacimiento = datetime.strptime(fecha, "%d/%m/%Y").date()
    dia_semana = calcula_dia_semana(fecha_nacimiento)
    print(f"Naciste un {dia_semana}.")

if __name__ == '__main__':
    # test_calcula_imc()
    # test_calculo_estado_nutricional()
    test_imprime_estados_nutricionales([(60.0, 1.6), (75.4, 1.75), (87.9, 1.69), (45.1, 1.65), (120.0, 1.60)])
    # test_lee_numeros()
    # test_calcula_dia_semana()