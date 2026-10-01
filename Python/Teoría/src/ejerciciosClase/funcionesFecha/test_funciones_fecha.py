from funciones_fecha import*

def test_restaFechas():
    print(restaFechas("12/11/2017", "19/09/2025"))

if __name__ == "__main__":
    test_restaFechas()   

# fecha3 = sumaDias("18/10/2024", 15):
#     if fecha3 is not None:
#         print("Nueva fecha " + fecha3.strftime("%d/%m/%Y"))
#     else:
#         print("Parámetros de simaDias() erróneos")