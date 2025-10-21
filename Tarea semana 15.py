import requests #librería para hacer solicitudes HTTP

latitud =23.6585116
longitud = -102.0077097
API_KEY = '0932ed7aed5aef2c2914a9cc3ace2ee5' #no olvides cambiar esto por tu API key de OpenWeather
part = '' #variable para partes del código

URL = f'https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={API_KEY}&units=metric&lang=es'

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    clima_actual = data["main"] #main es un diccionario dentro del diccionario data
    print(f"Temperatura: {clima_actual['temp']} °C")
    print(f"Descripción: {data['weather'][0]['description']}") #weather es una lista dentro del diccionario data
    print(f"Humedad: {clima_actual['humidity']}%") #humidity es un dato dentro del diccionario main
else:
    print("Error al obtener datos:", response.status_code) #si no es 200, hubo un error
