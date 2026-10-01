nombres = ['Leopoldo', 'Luisa', 'Lorenzo', 'Leonor']
edad = [35, 91, 77, 45]

for i, (nom, ano) in enumerate(zip(nombres, edad), start = 1):
    print(f'{i}. {nom} - Edad: {ano}')