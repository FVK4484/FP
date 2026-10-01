def esbisiesto(n):
    res = False
    if n%400 == 0 and (n%4 == 0 or n%100 != 0):
        res = True
    return res

def nose_si_esbisiesto():
    año = int(input("Pon numero: "))
    while año > 0:
        esbisiesto(año)
        break
    print("Se acabo.")

