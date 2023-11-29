#Primero, abrir CMD en modo admin, y meter el siguiente comando:  python.exe -m pip install --upgrade pip
#Luego, meter este: #pip3 install requests
import requests
import json

def check_internet():  #Esta función es para comprobar que tenemos internet y nos podemos conectar a la api
    url = "https://api.preciodelaluz.org"
    timeout = 5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No hay conexión a internet.")
        return False
    
def obtener_precios_luz(zona):
    url = f"https://api.preciodelaluz.org/v1/prices/all?zone={zona}"
    response = requests.get(url)
    data = json.loads(response.text)
    precios = {}
    for hora, precio in data.items():
        print(f"Hora: {hora}, Precio: {precio}")
        precios[hora] = precio
    with open('precios_luz.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("Los precios de la luz se han guardado en 'precios_luz.json'.")
    return precios

if check_internet():
    print(obtener_precios_luz('PCB'))
else:
    print("[ERROR] Algo pasa con el internet, o la api")
