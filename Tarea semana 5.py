#Aqui pedimos el año actual

año = input("Introduce el año actual: ")

if año.isnumeric():  #Si es numerico
    año = int(año) #Convertimos a entero

else:
    print("Debes de introducir un numero valido")
    #Termina si no se introduce un numero valido
    exit()
    

if año <= 2024:
 print("Por favor introduce el año actual!!!")
 #Termina si no se introduce el año actual
 exit()
else:
   print("Año correcto!")
    
#Aqui pedimos el segundo 

año2 = input("Ingrese un año para calcular: ")

if año2.isnumeric():
   año2 = int(año2)
else:
   print("Debes introducir un numero valido")
   #Termina si no introduce un numero valido
   exit()

#Se calcula la diferencia

diferencia = año2 - año

if diferencia == 0:
   print("Haz introducido el mismo año actual")
elif diferencia > 0:

 print(f"Para llegar a {año2} hace falta {diferencia} año(s)") #Cadena formateada
else:
   print(f"Desde el año {año2} ha pasado {abs(diferencia)} año(s)") #abs calcula valor absoluto desde 0
#Termina el programa
exit()