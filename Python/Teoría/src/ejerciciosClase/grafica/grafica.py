import matplotlib.pyplot as plt 

# Use estos datos de ventas mensuales
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
ventas = [1200,1500,1700,1300,1600,1800,2000,1900,2100,2200,2300,2500]

#Crea el gráfico con las siguientes instrucciones:
plt.figure(figsize=(10,6))
plt.plot(meses, ventas, marker='o', color='blue', label='Ventas mensuales')

#Indique el título y las etiquetas con las siguientes instrucciones:
plt.title('Ventas mensuales en 2024')
plt.xlabel('Mes')
plt.ylabel('Ventas (€)')

#Indique con cuadrícula y muestra la leyenda con las siguientes instrucciones:
plt.grid(True)
plt.legend()

#Guarde el gráfico como imagen y muéstrela con las siguientes instrucciones:
plt.savefig('grafico_ventas.png')
plt.show()

