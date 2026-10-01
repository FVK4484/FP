def es_palindromo(cadena):
    res = False
    reversa = "".join(reversed(cadena)) # cadena[::-1]
    if cadena == reversa:
        res = True
    return res

# def es_palindromo(cadena):
#     cadena = cadena.lower().replace(" ", " ")

#     longitud = len(cadena)

#     for i in range(longitud // 2):
#         if cadena[i] != cadena[longitud - i - 1]:
#             return False