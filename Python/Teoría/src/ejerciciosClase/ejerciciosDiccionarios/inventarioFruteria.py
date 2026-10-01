inventario = {"manzanas":(2.50, 90.50), "plátanos":(2.35, 75.25), "peras":(2.60, 80.)}

# 1.
print('Productos iniciales:')
[print(f"{nombre}: Precio = {precio} €, Stock = {stock} kg.") \
                                                for nombre, (precio, stock) in inventario.items()]

# 2.
inventario["kiwis"] = (3, 90.)
print(inventario)

# 3.
mostrarPrecioyStock = inventario["manzanas"]
print(mostrarPrecioyStock)

# 4.
del(inventario["manzanas"])
print(inventario)

# 5.
print('Productos iniciales:')
[print(f"{nombre}: Precio = {precio} €, Stock = {stock} kg.") \
                                                for nombre, (precio, stock) in inventario.items()]
