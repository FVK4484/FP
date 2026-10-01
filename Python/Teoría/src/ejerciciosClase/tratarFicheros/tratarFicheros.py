import csv

def crearFicheroCSV(nombre, texto):
    with open(nombre , mode = 'w', newline = '') as f:
        while True:
            try:
                print(True)
                w = csv.writer(f, delimiter = '|')
                w.writerows(texto)
                break
            except ValueError:
                print("False")

crearFicheroCSV("provincias.csv", [
        [1, "Ávila"],
        [2, "Albacete"],
        [3, "Sevilla"],
        [4, "Jaén"]
    ])

