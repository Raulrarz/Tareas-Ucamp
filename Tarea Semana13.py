#Programa para capturar las calificaciones de un grupo de alumnos 

#Que al iniciar el programa se muestre un menu con las siguientes opciones:
#Agregar alumno (1)
#Ver los alumnos y las calificaciones (2)
#Salir (s)

#Si decide agregar un nuevo alumno, corroborar que el nombre no este en blanco 

#Preguntar cuantas calificaciones se quiere agregar 

#Si ingresa una calificacion que no sea de tipo numerico, se pedira volver a intentar 
#Despues de agregar al alumno , volvera al menu principal 

#Si se selecciona la opcion 2, mostrar en pantalla la informacion de cada alumno y el promedio de sus calificaciones

#Si selecciona la opcion "s" , indica que se cerrara el pregrograma y preguntar si esta seguro de cerrar el programa o no 

alumnos = {} #Se utiliza un diccionario para guardar los alumnos y sus calificaciones , por eso se inicializa vacio


def seleccionar_opcion():
    '''
    Muestra el menu principla y permite seleccionar una opcion
    '''
    while True:
        print("Menu Principal")
        print("1. Agregar alumno")
        print("2. Ver alumnos y calificaciones")
        print("s. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            agregar_alumno()
        elif opcion == "2":
            ver_alumnos_y_calificaciones()
        elif opcion.lower() == "s": #Los metodos lower y upper convierten a minusculas o mayusculas respectivamente
            salir() 
        else:
            print("Opcion no valida, Intente de nuevo.")
            
def agregar_alumno():
    '''
    Agrega un nuevo alumno y sus calificaciones
    '''
    while True:
        nombre = input("Ingrese el nombre del alumno: ").capitalize()
        if nombre.strip() == "": #.strip() elimina espacios en blanco al inicio y al final de la cadena
            print("Debe ingresar un nombre")
        elif not nombre.isalpha(): #.isalpha() verifica que todos los caracteres sean letras
            print("El nombre no debe contener numeros o caracteres especiales")
        elif nombre in alumnos: 
            print("El alumno ya fue registrado.")
        else:
            break

        
    while True:
        try:
            num_calificaciones = int(input(f"¿Cuantas calificaciones desea agregar para '{nombre}'?: "))
            if num_calificaciones <= 0: #Corrobora que se ingrese al menos una calificacion
                print("Debe agregar al menos una calificacion.")
            else:
                break
        except ValueError:
            print("Por favor ingrese un numero entero para la catidad de calificaciones.")

#Lista de calificaciones

    calificaciones = [] #Se utiliza una lista para guardar las calificaciones de cada alumno
    for i in range(num_calificaciones):
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificacion {i+1} para {nombre}: ")) #i+1 para que inicie en 1 y no en 0
                calificaciones.append(calificacion)
                break
            except ValueError:
                print("Por favor ingrese un numero para la calificacion")
                
    alumnos[nombre] = calificaciones
    print(f"Alumno {nombre} agregado con sus calificaciones correspondientes.")

    
def ver_alumnos_y_calificaciones():
    '''
    Muestra la lista de alumnos con sus calificaciones y el promedio
    '''
    
    if not alumnos: #Verifica si el diccionario esta vacio
        print("No hay alumnos registrados.")
    else:
        for nombre, calificaciones in alumnos.items():
            promedio = sum(calificaciones) / len(calificaciones)
            print(f"Alumnos: {nombre}")
            print(f"Calificaciones: {calificaciones}")
            print(f"Promedio: {promedio:.2f}") #.2f limita el numero de decimales a 2
            print("-" * 20) #Imprime una linea de separacion

def salir():
    while True:
        confirmacion = input("¿Esta seguro que desea salir? (s/n):  ").lower()
        if confirmacion == "s":
         print("Saliendo del programa.")
         exit()

        elif confirmacion == "n":
            seleccionar_opcion()
        else:
            print("Opcion no valida, intente de nuevo.")
seleccionar_opcion()

