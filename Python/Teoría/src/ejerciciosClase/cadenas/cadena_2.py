nombres = ["Ana", "Luis", "María", "Carlos", "Elena"]
edades = [28, 34, 25, 40, 30]
ciudades = ["Sevilla", "Almería", "Granada", "Cádiz", "Málaga"]

print("{:<5} {:<10} {:<5} {:<10}".format("ID", "Nombre", "Edad", "Ciudad"))
print("-" * 35)
combi = list(zip(nombres, edades, ciudades))
combi_sorted = sorted(combi, key = lambda x:x[1], reverse = True)
for i, (n, e, c) in enumerate(combi_sorted, start = 1):
    if len(nombres) == len(edades) and len(edades) == len(ciudades) and len(ciudades) == len(nombres):
        print("{:<5} {:<10} {:<5} {:<10}".format(i, n, e, c))
    else:
        print("Error la lista no tiene la misma longitud.")