
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# a)
union_conjuntos = conjunto1 | conjunto2
print(union_conjuntos)

# union_conjuntos = conjunto1.union(conjunto2)
# print(union_conjuntos)

# b)
interseccion_conjuntos = conjunto1 & conjunto2
print(interseccion_conjuntos)

# interseccion_conjuntos = conjunto1.intersection(conjunto2)
# print(interseccion_conjuntos)

# c)
dif_conjuntos = conjunto1 - conjunto2
print(dif_conjuntos)

# dif_conjuntos = conjunto1.difference(conjunto2)
# print(dif_conjuntos)

dif2_conjuntos = conjunto2 - conjunto1
print(dif2_conjuntos)

# dif2_conjuntos = conjunto2.difference(conjunto1)
# print(dif2_conjuntos)

# d)
dif_simetrica_conjuntos = union_conjuntos - interseccion_conjuntos
print(dif_simetrica_conjuntos)

