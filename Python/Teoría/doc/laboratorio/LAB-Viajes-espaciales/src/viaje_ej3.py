edad = int(input("Inserte su edad: "))
nivel_fisico = int(input("Inserte su nivel físico: "))

if nivel_fisico in range(1,10):
    if edad < 18:
        print("Debes ser mayor de edad.")
    elif nivel_fisico < 5:
        print("Debes estar en mejor forma.")
    else:
        print("¡Listo para despegar!")
else:
    print("El nivel físico debe estar comprendido entre 1 y 10." )