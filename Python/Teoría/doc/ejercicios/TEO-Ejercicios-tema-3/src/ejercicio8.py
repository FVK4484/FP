nombres = ["Juan", "Ana", "Manuel", "Irene", "Jaime", "María"]
apellidos = ["Ruiz", "López", "Martínez", "Fernández", "Jiménez", "Castro"]
# La salida debe ser ['Juan Ruiz', 'Ana López', 'Manuel Martínez', 'Irene Fernández', 'Jaime Jiménez', 'María Castro']

nombres_completos = []
# TODO

for nombre, apellido in zip(nombres, apellidos):
  nombres_completos.append(f"{nombre} {apellido}")

print(nombres_completos)