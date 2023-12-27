import requests
datos = None

while True:
    respuesta = input("¿Tienes las coordenadas de tu ubicación?: ")
    if respuesta.lower() == "si":
        try:
            latitud = float(input("Ingresa la latitud: "))
            longitud = float(input("Ingresa la longitud: "))
        except ValueError:
            print ("Por favor, ingresa una latitud y longitud válidas.")
        datos = f"lat={latitud}&lon={longitud}"
        break
    elif respuesta.lower() == "no":
        ciudad = input("Introduce el nombre de la ciudad y las siglas del país (ejemplo: 'Mexico City, MX'): ")
        datos = f"q={ciudad}"
        break
    else:
        print("Por favor, ingrese una opción válida. (si/no)")

if datos is None:
    print("No se ingresaron datos correctos.")
    exit()
api_key = input("Introduce tu API key de OpenWeather: ")

url = f"http://api.openweathermap.org/data/2.5/weather?{datos}&lang=es&appid={api_key}"

try:
    respuesta = requests.get(url, timeout=10)
except requests.Timeout:
    print("Error: el tiempo de espera ha finalizado")

if respuesta.status_code != 200:
    print("Ha ocurrido un error. Intenta nuevamente")
    exit()
datos = respuesta.json()
ciudad = datos["name"]

datos_clima = datos["weather"]
clima = datos_clima [0]["description"]

print(f"El clima en {ciudad} es {clima}")
