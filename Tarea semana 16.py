#Debe consultar el clima de la ciudad o la latitud y la longitud del usuario
#Preguntarle, primero, al usuario si tiene a la mano las coordenadas o el nombre de la ciudad, en el siguiente formato:“CIUDAD,SIGLAS_DEL_PAÍS”.
#Debemos solicitarle su API key de OpenWeather
#Si el usuario introduce mal los datos, debes indicar qué dato es el incorrecto.
#Los posibles errores deben estar cubiertos por un try/except
#Si la API no encuentra la ciudad, debes indicarlo al usuario con un mensaje
#Al final, si todo salió bien, debes mostrar un mensaje como este: El clima en Mexico City es muy nuboso”.

import requests #librería para hacer solicitudes HTTP

def consultar_clima():
    eleccion = input('Tienes las coordenadas (latitud y longitud) o el nombre de la ciudad ? (Si/No): ')
    API_KEY = input('Ingresa tu API key de openWeather: ')
    if eleccion.lower() == 'si':
        try:
            latitud = float(input('Ingresa la latitud: '))
            longitud = float(input('Ingresa la longitud: '))
        except ValueError:
            print('Error: las coordenadas deben ser numeros validos.')
            return
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={API_KEY}&units=metric&lang=es'
    else:
         ciudad = input('Ingrese le nombre de la ciudad (formato: CIUDAD, SIGLAS_DEL_PAIS):')
         url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es' 

    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status() #Lanza un error para códigos de estado HTTP 4xx/5xx
    except requests.Timeout:
        print('Error: la solicitud ha excedido el tiempo de espera.')
        return
    except requests.RequestException as e:
        print(f'Error en la solicitud: {e}')
        return
    

    datos = respuesta.json()

    if datos.get('cod') != 200:
        print('Ciudad no encontrada')

    ciudad_nombre = datos['name']
    clima = datos['weather'][0]['description']
    print(f'El clima en {ciudad_nombre} es: {clima}')

consultar_clima()