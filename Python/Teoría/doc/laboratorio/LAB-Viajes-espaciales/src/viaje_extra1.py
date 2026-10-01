km = 150000
distancia = int(input("Introduce la distancia total en km: "))
paradas = 0
km_actual = km

while km_actual < distancia:
    print(f"Parada en el km {km_actual}")
    paradas += 1
    km_actual += km

# Mostrar total de paradas
print(f"Total de paradas para repostar: {paradas}")




