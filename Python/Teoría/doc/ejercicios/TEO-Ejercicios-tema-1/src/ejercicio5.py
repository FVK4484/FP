from datetime import datetime

def calcula_dia_semana(fecha):
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return dias_semana[fecha.weekday()]

fecha = input("Introduce tu fecha de nacimiento (dd/mm/yyyy): ")
fecha_nacimiento = datetime.strptime(fecha, "%d/%m/%Y").date()
print(calcula_dia_semana(fecha_nacimiento))