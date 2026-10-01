from statistics import mean

def lee_numeros():
    lista = []
    cont = 0
    n = int(input('Introduce cuantos números quiere añadir: '))
    print(f'Inserte {n} numeros')
    while  n > cont:
        cont += 1
        numero = int(input(f'{cont}. Introduce un número: '))
        lista.append(numero)
    return lista
    
# print(lee_numeros())

# print(max(lee_numeros()))

# media = mean(lee_numeros())

# if media == 0:
#     print('No es posible calcular la media.')
# else:
#     print(media)

# numeros = lee_numeros()
# cont = 0
# for numero in numeros:
#     if numero % 2 == 0:
#         cont += 1
# print(cont)

lista = lee_numeros()
lista_nueva = []
for numero in lista:
    if numero > 10:
        lista_nueva.append(numero)
print(lista_nueva)

