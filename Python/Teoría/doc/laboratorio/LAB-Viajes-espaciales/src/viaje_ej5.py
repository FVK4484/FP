while True:
    distancia_km = int(input("Escriba una distancia (km): "))
    velocidad_kmh = int(input("Escriba una velocidad (km/h): "))
    tiempo_horas = distancia_km / velocidad_kmh
    tiempo_dias = tiempo_horas / 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    pregunta = input("¿Quieres hacer otra simulación? (s/n): ")
    if pregunta != "s":
        break
    else:
        continue

    

