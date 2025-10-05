# <<<FuncionEliminaElementos.py>>>
from m_retosemanal import crear_listas
def eliminar_elementos(lista1, lista2):
    '''
    Elimina de la primera lista los elementos que estan en la segunda lista
    '''

    for elemento in lista2:
        if elemento in lista1:
            while elemento in lista1:
              lista1.remove(elemento)

            print(f"Se ha eliminado '{elemento}' de la primera lista")
        else:
            print(f"'{elemento}' no estaba en la primer lista. ")
            
      
#Imprimir resultado final

    print("\nLa primer lista actualizada es:")
    print(lista1)
    return lista1
