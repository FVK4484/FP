from triangulo import*

l1 = float(input("Ingresa la longitud del lado 1: "))
l2 = float(input("Ingresa la longitud del lado 2: "))  
l3 = float(input("Ingresa la longitud del lado 3: "))

area = area_por_heron(l1, l2, l3)
print("El área del triángulo es: ", area)