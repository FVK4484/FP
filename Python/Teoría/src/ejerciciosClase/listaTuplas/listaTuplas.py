empleados = [("Ana", 23, "TI"), ("Luis", 44, "RRHH"), ("Marta", 32, "Cobros"), ("Carlos", 30, "TI"), ("Elena", 58, "Contabilidad")]

def mostrar_empleados(empleados):
    return empleados

print(mostrar_empleados([("Ana", 23, "TI"), ("Luis", 44, "RRHH"), ("Marta", 32, "Cobros"), ("Carlos", 30, "TI"), ("Elena", 58, "Contabilidad")]))

def calcular_edad_promedio(empleados):
    suma_edad = 0
    for empleado in empleados:
        suma_edad += empleado[1]
    return suma_edad / len(empleados)

print(calcular_edad_promedio([("Ana", 23, "TI"), ("Luis", 44, "RRHH"), ("Marta", 32, "Cobros"), ("Carlos", 30, "TI"), ("Elena", 58, "Contabilidad")]))

def mostrar_empleados_TI(empleados):
    lista_empleados = []
    for empleado in empleados:
        if empleado[2] == "TI":
            lista_empleados.append(empleado)
        else:
            continue
    return lista_empleados

print(mostrar_empleados_TI([("Ana", 23, "TI"), ("Luis", 44, "RRHH"), ("Marta", 32, "Cobros"), ("Carlos", 30, "TI"), ("Elena", 58, "Contabilidad")]))