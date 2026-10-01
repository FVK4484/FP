def indica_primera_aparicion(lista, valor):
    for posicion in range(len(lista)):
        if lista[posicion] in valor:
            return posicion
    return -1    
    

lista_1 = ["árbol", "coche", "casa", "peatón"]
lista_2 = ["árbol", "coche", "casa", "peatón"]
print(f'Posición de "casa" en la lista {lista_1}: {indica_primera_aparicion(lista_1, 'casa')}')
print(f'Posición de "bicicleta" en la lista {lista_2}: {indica_primera_aparicion(lista_1, 'bicicleta')}')
