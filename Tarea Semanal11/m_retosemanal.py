# <<<m_retosemanal.py>>>

#Funcion que permite crear listas y elimine los valores existentes en otras listas

def crear_listas():  #Definimos la funcion para crear listas
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