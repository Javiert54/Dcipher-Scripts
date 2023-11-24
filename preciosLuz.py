#Primero, abrir CMD en modo admin, y meter el siguiente comando:  python.exe -m pip install --upgrade pip
#Luego, meter este: #pip3 install requests
import requests
import json

def obtener_precios_luz(zona):
    url = f"https://api.preciodelaluz.org/v1/prices/all?zone={zona}"
    response = requests.get(url)
    data = json.loads(response.text)

    for hora, precio in data.items():
        print(f"Hora: {hora}, Precio: {precio}")
        
    with open('precios_luz.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("Los precios de la luz se han guardado en 'precios_luz.json'.")

# Ejemplo de uso
obtener_precios_luz('PCB')
