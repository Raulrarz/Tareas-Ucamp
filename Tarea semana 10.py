#Que permita crear dos listas de distintas longitudes.
#Que la longitud y los elementos de cada lista sean especificados por el usuario.
#Que imprima las listas indicando que son las listas originales.
#Que elimine de la primera lista los nombres de la segunda.
#Que imprima la primera lista indicando que se han eliminado los elementos que estaban también en la segunda

#Creamos la primera lista

def crear_listas():
    '''
    Crea dos listas con longitudes y elementos especificados por el usuario.
    '''
    lista1 = []
    lista2 = []

#Primer lista
    longitud1 = int(input('Ingrese la longitud de la primera lista:'))
    for i in range(longitud1):
        elemento1 = input(f'Ingrese el elemento {i+1} para la primera lista:')
        lista1.append(elemento1)

#Segunda lista
    longitud2 = int(input('Ingrese la longitud de la segunda lista:'))
    for i in range(longitud2):
        elemento2 = input(f'Ingrese el elemento {i+1} para la segunda lista:')
        lista2.append(elemento2)

#Imprimir las listas originales
    print("\nLas listas originales son:")
    print(f'Primera lista: {lista1}')
    print(f'Segunda lista: {lista2}\n')

    return lista1, lista2

def eliminar_elementos():
    '''
    Elimina de la primera lista los elementos que estan en la segunda lista
    '''
    lista1, lista2 = crear_listas()

    for elemento in lista2:
        if elemento in lista1:
            lista1.remove(elemento)
            print(f"Se ha eliminado '{elemento}' de la primera lista")
        else:
            print(f"'{elemento}' no estaba en la primer lista. ")
            
      
#Imprimir resultado final

    print("\nLa primer lista actualizada es:")
    print(lista1)
    return lista1

     
if __name__ == "__main__":   #__name__ es una variable especial en Python que se utiliza para determinar si un archivo de Python se está ejecutando como el programa principal o si se está importando como un módulo en otro archivo.
    eliminar_elementos()