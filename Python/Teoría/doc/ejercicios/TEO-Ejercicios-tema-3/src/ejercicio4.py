def imprime_pares_inverso(n):
    res = []
    while n > 0:
        if n % 2 == 0:
            res.append(n)
            n = n - 2
        elif n % 2 == 1:
            n = n - 1
    return " ".join(str(elemento)for elemento in res)
    
n = input('Inserte un número: ')
n = int(n)
print(f'Imprimiendo números pares menores o iguales a {n}: {imprime_pares_inverso(n)}')