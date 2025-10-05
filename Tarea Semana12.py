#Que pida al usuario las ventas de un rango de determinados años
#Que le pida las ventas de cada año dentro del rango
#Que muestre mediante una grafica de lineas las ventas de cada año 

import matplotlib.pyplot as plt


def grafica_ventas(años, color, ventas):
   '''
   Dibuja la grafica de lineas con las ventas del año
   '''
   plt.plot(años, ventas, color = color, marker = 'o') #marker 'o' pone una bolita conforme vayan las ventas
   plt.title("Ventas en los años")
   plt.xlabel('Año')
   plt.ylabel('Ventas')

#Generamos la lista de los años 2010 al 2025 
años = list(range(2020, 2026))

#Pedimos las ventas de cada año 


ventas = []
for anio in años:
   v = float(input(f"Ingrese las ventas en el año {anio}: "))
   ventas.append(v)

#Graficamos

grafica_ventas(años, 'red', ventas)
plt.show()