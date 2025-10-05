import sys #Importamos el modulo sys para poder salir del programa si se requiere

#Aqui generamos la contraseña

def generar_contraseña(Numero1, palabra1):
    return f"{Numero1}{palabra1}" #return devuleve el valor de la funcion
    

#Validamos numero y palabras ingresadas por el usuario

def validar_numero(numero1): 
    if numero1.strip() == "":  #strip() elimina espacios en blanco al inicio y al final
        print("Debes incluir un numero")
        sys.exit()

    if numero1.isnumeric():
        return int(numero1)
    else:
        print("La contraseña debe de iniciar con un numero")
        sys.exit()
#Validamos las palabras introducidas por el ususario

def validar_palabra(palabra):
    palabra = palabra.strip()
    if palabra.isalpha():
        return palabra
    else:
        print("Debes introducir una palabra")
        sys.exit()

    
#Comenzamos con la ejecucion
num = validar_numero(input("Introduce un numero: "))
palabra1 = validar_palabra(input("Introduce una palabra: "))


#Generamos la contraseña
contraseña = generar_contraseña(num, palabra1)
print("Contraseña generada")

#Introducimos la contraseña
print("Ingresa la contraseña generada")
contraseña_ingresada = input("Contraseña: ")
if contraseña_ingresada == contraseña:
    print("Ingrese nuevamente la contraseña para verificar")
    retry = input("Contraseña: ") #Retry para reintentar y verificar la contraseña
    print("Contraseña Correcta")
else:
    print("Las contraseñas no coinciden")
    sys.exit()


