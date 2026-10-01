palabras = ['satélite', 'sol', 'luna', 'estrella', 'marte', 'júpiter']

# 1.
palabras_menos5 = list(filter(lambda x: len(x) < 5 , palabras))
print(palabras_menos5)

# 2.
palabras_mayus = list(map(lambda x: x.upper(), palabras_menos5))
# palabras_mayus = [palabra.upper() for palabra in palabras_menos5]
print(palabras_mayus)

# 3.
# palabra_empiezaS = any(palabra.startswith('S') for palabra in palabras_mayus)
palabra_empiezaS = any(map(lambda x: x.startswith('S'), palabras_mayus))
print(palabra_empiezaS)

# 4.
# lista_longitudes = [len(palabra) for palabra in palabras_menos5]
lista_longitudes = list(map(lambda x: len(x), palabras_menos5))
print(lista_longitudes)
