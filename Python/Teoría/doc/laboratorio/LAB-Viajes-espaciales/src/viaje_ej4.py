# Muestra cuánto se tarda en llegar a Marte (225 millones de km) con velocidades de 10.000 a 50.000 km/h (en saltos de 10.000 km/h), usando for y range():
distancia = 225000000
for velocidad in range(10000, 50000, 10000):
    horas = distancia / velocidad
    dias = horas / 24
    años = dias / 365.25
    print(años, "años")
