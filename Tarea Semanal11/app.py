import m_retosemanal as m
import m_retosemanal2 as m2

listas = input("Por favor crea 2 listas (coloca 2): ")
if listas.isdigit():
    listas = int(listas)
    if listas == 2:
        lista1, lista2 = m.crear_listas()
        m2.eliminar_elementos(lista1, lista2)

    
    else:
        print("Tienes que crear 2 listas")