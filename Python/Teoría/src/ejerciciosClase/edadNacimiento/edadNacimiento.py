from datetime import*

def calcular_edad():
    fecha_actual = datetime.now()
    while True:
        fecha_nacimiento_str = input("Inserte una fecha de nacimiento: ")
        try: # Bloque de código a controlar excepciones
            fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%d/%m/%Y').date()
            if fecha_nacimiento  > fecha_actual:
                print(f"La fecha introducida ({fecha_nacimiento_str}) debe ser menor que la actual\n") 
            else:
                break
        except ValueError:
            print("Error, formato incorrecto")
        
print(calcular_edad())