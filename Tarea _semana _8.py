#Aqui creamos el diccionario

colores = {"rojo": "red",
           "naranja": "orange",
           "amarillo": "yellow",
           "verde": "green",
           "azul": "blue",
           "violeta": "purple"

}

#Pedimos el color al usuario

color = input("Ingresa un color (español o ingles): ").lower() #Convertimos a minusculas para evitar errores  

opcion = input("¿Quieres traducir a ingles (en) o a espalo (es)? ").lower()

if opcion == "en":
    if color in colores: #Español a Ingles
        print(f"El color {color} en ingles es {colores[color]}")
    elif color in colores.values(): 
       print(f"El color {color} ya esta en ingles")

    else:
        print("Ese color no esta en el diccionario")
        
elif opcion == "es":
    if color in colores:
        print(f"El color {color} ya esta en español ")

    else: 

     for esp, ing in colores.items(): #Ingles a Español 
        if color == ing:
            print(f"El {color}  en Españols es {esp}")
    
        break
     else:
        print("Ese color no esta en el diccionario")

else:
 print("Opcion no valida")

