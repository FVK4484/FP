from centros import*

def leer_centros_test(fichero):
    print(leer_centros(fichero))

def calcular_total_camas_centros_accesibles_test(fichero):
    print("Este es número total de camas de los centros sanitarios accesibles para discapacitados: ", calcular_total_camas_centros_accesibles(leer_centros(fichero)))

def obtener_centros_con_uci_cercanos_a_test(tupla):
    print("Este es el nombre, la localidad y la ubicacion de los centros con uci situados a una distancia de las coordenadas dadas como parámetro menor o igual que el umbral dado: ", 
          obtener_centros_con_uci_cercanos_a(tupla[0], tupla[1], tupla[2]))
    
if __name__ == '__main__':
    datos = leer_centros(r'FP_25_26\doc\laboratorio\LAB-Centros-sanitarios\data\centrosSanitarios.csv')
    calcular_total_camas_centros_accesibles_test(datos)
    obtener_centros_con_uci_cercanos_a_test(datos, (36.72460010332263, -5.698749084070459), 10)
    