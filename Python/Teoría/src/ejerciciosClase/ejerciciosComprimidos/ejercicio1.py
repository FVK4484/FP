examen1 = [('Alicia', 85), ('José', 78), ('Carlos', 92), ('David', 88)]
examen2 = [('Alicia', 90), ('Eva', 88), ('José', 75), ('Francisco', 84)]

# 1.
examen1_conj = set(examen1)
examen2_conj = set(examen2)

# 2.
estudiantes_ambos = {e1[0] for e1 in examen1_conj}.intersection(e2[0] for e2 in examen2_conj)
print(estudiantes_ambos)

# 3.
solo_examen1 = {e1[0] for e1 in examen1_conj}.difference(e2[0] for e2 in examen2_conj)
print(solo_examen1)

# 4. 
solo_examen2 = {e2[0] for e2 in examen2_conj}.difference(e1[0] for e1 in examen1_conj)
print(solo_examen2)

# 5.
media_ambos = [(e1[1], e2[1]) for e1 in examen1_conj for e2 in examen2_conj if e1[0] == e2[0]]
calificaciones = [(p1 + p2) / 2 for p1, p2 in media_ambos]
print(calificaciones)
