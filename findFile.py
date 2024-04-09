import os
import fnmatch

def encontrar_archivos(patrones, ruta, cadenas=None):
    """
    Esta función busca todos los archivos en una ruta dada que coinciden con los patrones proporcionados y cuya ruta contenga una lista de cadenas específicas.
    
    Parámetros:
    patrones (list): Una lista de patrones de nombres de archivo que estamos buscando.
    ruta (str): La ruta de la carpeta que queremos buscar.
    cadenas (list): La lista de cadenas que deben estar contenidas en la ruta del archivo. Si no se proporciona, se buscarán todos los archivos que coincidan con los patrones.
    
    Retorna:
    Una lista de rutas de archivos que coinciden con los patrones proporcionados y cuya ruta contenga las cadenas especificadas.
    """
    archivos_coincidentes = []

    # Recorremos la carpeta de manera recursiva
    for raiz, dirs, archivos in os.walk(ruta):
        for archivo in archivos:
            ruta_archivo = os.path.join(raiz, archivo).lower()  # Convertimos la ruta a minúsculas
            # Si no se proporcionaron patrones, añadimos todos los archivos cuya ruta contenga las cadenas especificadas
            if patrones == ['']:
                if cadenas is None or all(cadena.lower() in ruta_archivo for cadena in cadenas):  # Convertimos las cadenas a minúsculas
                    archivos_coincidentes.append(ruta_archivo)
            else:
                for patron in patrones:
                    if fnmatch.fnmatch(archivo, patron) and (cadenas is None or all(cadena.lower() in ruta_archivo for cadena in cadenas)):  # Convertimos las cadenas a minúsculas
                        archivos_coincidentes.append(ruta_archivo)

    return archivos_coincidentes

# Ejemplo de uso
patrones = input('Introduce los patrones que estes buscando, separandolos con ";". Por ejemplo: *.db;*.pdf;*.html\n    (si no quieres buscar ningun patron, solo pulsa ENTER)\n').split(';') # Reemplaza esto con los patrones que estás buscando
ruta_carpeta = input('Introduce la ruta a la carpeta: ')  # Reemplaza esto con la ruta de la carpeta que quieres buscar
cadenas_input = input('Introduce las cadenas que deben estar contenidas en la ruta del archivo (si son varias palabras que pueden no estar pegadas, sepáralas con ";" EJEJMPLO: facebook;gmail;twitter):\n')  # Reemplaza esto con las cadenas que deben estar contenidas en la ruta del archivo
cadenas = None if cadenas_input == '' else cadenas_input.split(';')
archivos_encontrados = encontrar_archivos(patrones, ruta_carpeta, cadenas)

print(f"Se encontraron {len(archivos_encontrados)} archivos que coinciden con los patrones {patrones} y cuya ruta contiene '{cadenas}':")
for archivo in archivos_encontrados:
    print(archivo)
