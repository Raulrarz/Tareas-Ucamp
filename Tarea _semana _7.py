import sys
def validar_nombre(nombre):
    return nombre.isalpha() and len(nombre) > 0

lista = [] 

alumnos = 0 
while alumnos <= 5:
    opcion = input("Agregar alumo (1) o terminar (2): ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del alumno:").capitalize() # .capitalize() pone la primer letra en mayuscula
        if not validar_nombre(nombre):
            print("Nombre invalido. Intente de nuevo")
            sys.exit()
        calificacion1 = int(input(f"Ingrese la primera calificacion de {nombre}: "))
        calificacion2 = int(input(f"Ingrese la segunda calificacion de {nombre}: "))
        calificacion3 = int(input(f"Ingrese la tercera calificacion de {nombre}: "))
        alumno = [nombre, calificacion1, calificacion2, calificacion3]
        lista.append(alumno) 
        alumnos += 1
    elif opcion == "2":
        print("El programa ha terminado con {alumnos} alumnos.") 
        break
    else :
        print("Se ha ingresado una ocpion no valida")
        continue
print("La lista de alumnos es:")
print(lista) 


