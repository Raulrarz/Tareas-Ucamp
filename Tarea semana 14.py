#Un programa que abre una agenda de contactos y pueda modificar los datos de un contacto

#El programa mostrara en pantalla la informacion de los contactos guardados numerada
#Pregunta cual de los contactos desea modificar
#Se podra modificar el nombre, telefono y correo 
#Se debera actualizar la informacion en el archivo 
#El programa no debe interrumpirse si el usuario ingresa mal los datos  o las opciones 



personas = []
def agregar_persona():
    '''
    Agrega una nueva persona a la agenda
    '''
    contacto = []

    while True:
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        if nombre == "":
            print("No has introducido tu nombre")
        elif apellido == "":
            print("No has introduciod tu apellido") 
        else:
            contacto.append(nombre)
            contacto.append(apellido)
            break

    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            contacto.append(edad)
            break 
        except ValueError:
         print("Debes introducir un numero")


    correo = input("Ingrese su correo: ")
    contacto.append(correo)

    while True:
        try: 
            telefono = input("Ingrese su telefono: ")
            int(telefono)
            contacto.append(telefono)
            break
        except ValueError:
            print("Debes ingresar un numero")

    personas.append(contacto)


def cargar_datos():
    '''
    Carga los datos desde el archivo agenda.txt al programa
    '''
    try:
        with open('agenda.txt', 'r') as f_agenda:
            for linea in f_agenda:
                partes = linea.strip().split(' ') #separar por espacios
                nombre = partes[0] 
                apellido = partes[1]
                edad = int(partes[3])
                correo = partes[5]
                telefono = partes[7]
                personas.append([nombre, apellido, edad, correo, telefono])
    except FileNotFoundError:
        print("No se encontro el archivo agenda.txt, se creara uno nuevo al guardar los datos.")

def mostrar_contactos():
    '''
    Muestra los contactos guardados en la agenda
    '''
    if not personas:
        print("No hay contactos en la agenda.")
    else:
        print("\nContactos en la agenda: ")
        for i, persona in enumerate(personas, start = 1):
            print(f"{i}. {persona[0]} {persona[1]} Edad: {persona[2]} Correo: {persona[3]} Telefono: {persona[4]}")


def modificar_contacto():
    '''
    Modifica los datos de un contacto existente
    '''
  
    if not personas:
        print("No hay contactos para modificar.")
        return
    while True:
        try:
            indice = int(input("Ingrese el numero del contacto que desea modificar (0 para cancelar): "))
            if indice == 0:
                return
            if 1 <= indice <= len(personas):
                contacto = personas[indice - 1]
                print(f'Modificando contacto: {contacto[0]} {contacto[1]}')


                nuevo_nombre = input(f'Ingrese nuevo nombre (dejar en blanco para no cambiar) [{contacto[0]}]: ')
                if nuevo_nombre:
                    contacto[0] = nuevo_nombre


                    nuevo_apellido = (input(f'Ingrese nuevo apellido (dejar en blanco para no cambiar) [{contacto[1]}]: '))
                    if nuevo_apellido:
                        contacto[1] = nuevo_apellido


                    while True:
                        nueva_edad = input(f'Ingrese nueva edad (dejar en blanco para no cambiar) [{contacto[2]}]: ')
                        if not nueva_edad:
                            break
                        try:
                            contacto[2] = int(nueva_edad)
                            break
                            
                        except ValueError:
                            print("Debes introducir un numero")



                    nuevo_correo = input(f'Ingrese nuevo correo (dejar en blanco para no cambiar) [{contacto[3]}]: ')
                    if nuevo_correo:
                        contacto[3] = nuevo_correo


                        while True:
                            nuevo_telefono = input(f'Ingrese nuevo telefono (dejar en blanco para no cambiar) [{contacto[4]}]: ')
                            if not nuevo_telefono:
                                    break
                            if nuevo_telefono.isdigit():
                                contacto[4] = nuevo_telefono
                                break
                            else:
                                print("Debes ingresar solo numeros en el telefono")
                        print("\nContacto modificado exitosamente.\n")
                        break
                    else:
                        print("Numero fuera de rango.Intente de nuevo.")
        except ValueError:
            print(" Por favor ingrese un numero valido.")

def guardar_dato():
    '''
    Guarda los datos en el archivo agenda.txt
    '''
    with open('angenda.txt', 'w') as f_agenda:
        for persona in personas:
            f_agenda.write(f'{persona[0]} {persona[1]} Edad: {persona[2]} Correo: {persona[3]} Telefono: {persona[4]}\n')
            print("Datos guardados en el archivo agenda.txt")
      
def main():
    '''
    Funcion principal del programa
    '''
    cargar_datos()
    while True:
        mostrar_contactos()
        print('''
              1.Agreagar personas a la agenda
              2.Modificar contacto existente
              3Guardar datos en un archivo
              4.Salir
              ''')
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            agregar_persona()
        elif opcion == "2":
            modificar_contacto()
        elif opcion == "3":
            guardar_dato()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")
if __name__ == "__main__":
    main()