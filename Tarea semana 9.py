#Que un bucle infinito solicite al usuario una letra (debe especificar al usuario la condicion para terminar el programa)
#Hará una funcion que imprima en la pantalla la letra siguiente en el alfabeto y la letra anteriror a la ingesada
#El porgrama debe continuar en el bulce hast aque el ususario decida salir del programa 

def letra_siguiente_anterior():
    '''
    Imprime la letra siguiente y anterior del alfabeto
    '''

    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    while True:
        letra = input("Ingrese una letra (o 'salir' para terminar): ")

        if letra.lower() == 'salir':
            print("Programa terminado.")
            break

        if len(letra) == 1 and letra.isalpha():
            letra_minus = letra.lower()
            indice = alfabeto.index(letra_minus)

            # Siguiente
            if indice < len(alfabeto) - 1:
                print(f"La letra siguiente a '{letra}' es '{alfabeto[indice + 1]}'.")
            else:
                print(f"La letra '{letra}' no tiene letra siguiente en el alfabeto.")

            # Anterior
            if indice > 0:
                print(f"La letra anterior a '{letra}' es '{alfabeto[indice - 1]}'.")
            else:
                print(f"La letra '{letra}' no tiene una letra anterior en el alfabeto.")

            print("-" * 40)
        else:
            print("Por favor, ingrese una letra válida.\n")


# 👇 Ejecutar
if __name__ == "__main__":
    letra_siguiente_anterior()
