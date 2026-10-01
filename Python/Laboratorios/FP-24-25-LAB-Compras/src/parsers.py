from datetime import datetime

def parsea_fecha(fecha_cadena, formato = '%d/%m/%Y %H:%M'):
    return datetime.strptime(fecha_cadena, formato)