from datetime import*

def agregarEvento():
    evento1 = []
    evento2 = []
    evento = []
    print("Añada un evento.")
    fecha_hora = input("Indique la fecha y hora del evento: ")
    fecha_hora1 = datetime.strptime(fecha_hora, '%d/%m/%Y-%H:%M')
    descripcion = input("Realize una breve descripción: ")
    evento1.append(fecha_hora1)
    evento2.append(descripcion)
    for e1, e2 in zip(evento1, evento2):
        while len(evento) <= 5:
            evento.append(f'Fecha evento: {e1}, descripcion: {e2}')
    return evento

print(agregarEvento())

# def borrarEventos():
#     fecha_borrar = input('Inserte la fecha de un evento para borrarlo: ')
#     if fecha_borrar in agregarEvento():
#         return fecha_borrar.remove() 

