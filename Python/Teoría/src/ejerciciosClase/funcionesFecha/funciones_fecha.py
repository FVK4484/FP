from datetime import*

def restaFechas(fecha1, fecha2):
    formato = "%d/%m/%Y"
    fecha1 = datetime.strptime(fecha1, formato)
    fecha2 = datetime.strptime(fecha2, formato)
    resta = (fecha1 - fecha2).days
    if fecha2 > fecha1:
        resta = (fecha2 - fecha1).days
    return resta

def sumaDias(fecha):
    pass