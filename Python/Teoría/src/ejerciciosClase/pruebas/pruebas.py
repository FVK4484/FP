for i in range(0, 10):
    print(i)

alumnos = [("Juan", 25), ("Ana", 17), ("Zaida", 19)]

for a in alumnos:
   print(a)


numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12]

suma = 0
for numero in numeros:
     if numero % 3 == 0:
        suma += numero
print(suma)

# A = (1,2,3)

# for i, x in enumerate(A):
#       print(i, 2 * x, end = ' ')
 
# def lectura_datos():
#     peso = float(input("Introduzca su peso en kgs:"))
#     estatura = float(input("Introduzca su estatura en metros:"))
#     return peso, estatura
# print("==== Cálculo del índice de masa corporal =====")
# peso, estatura = lectura_datos()
# print("Su IMC es:", peso / estatura ** 2)

c1, c2 = [1,2,3,4,5,6], [1,2,3]
res = []
for i, (e1, e2) in enumerate(zip(c1, c2)):
    res.append((i, (e1 + e2)))
print(res)

nombres = ["Aitor", "Laura"]

print(nombres[1] , nombres[0])
