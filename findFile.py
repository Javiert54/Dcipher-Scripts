import os
import fnmatch

def encontrar_archivos(patrones, ruta, cadena):
    """
    Esta función busca todos los archivos en una ruta dada que coinciden con los patrones proporcionados y cuya ruta contenga una cadena específica.
    
    Parámetros:
    patrones (list): Una lista de patrones de nombres de archivo que estamos buscando.
    ruta (str): La ruta de la carpeta que queremos buscar.
    cadena (str): La cadena que debe estar contenida en la ruta del archivo.
    
    Retorna:
    Una lista de rutas de archivos que coinciden con los patrones proporcionados y cuya ruta contenga la cadena especificada.
    """
    archivos_coincidentes = []

    # Recorremos la carpeta de manera recursiva
    for raiz, dirs, archivos in os.walk(ruta):
        for archivo in archivos:
            ruta_archivo = os.path.join(raiz, archivo)
            # Si no se proporcionaron patrones, añadimos todos los archivos cuya ruta contenga la cadena especificada
            if not patrones:
                if cadena in ruta_archivo:
                    archivos_coincidentes.append(ruta_archivo)
            else:
                for patron in patrones:
                    if fnmatch.fnmatch(archivo, patron) and cadena in ruta_archivo:
                        archivos_coincidentes.append(ruta_archivo)

    return archivos_coincidentes

# Ejemplo de uso
patrones = input('Introduce los patrones que estés buscando, separandolos con ";". Por ejemplo: *.db;*.pdf;*.html\n    (si no quieres buscar ningún patrón, solo pulsa ENTER)\n').split(';') # Reemplaza esto con los patrones que estás buscando
ruta_carpeta = input('Introduce la ruta a la carpeta: ')  # Reemplaza esto con la ruta de la carpeta que quieres buscar
cadena = input('Introduce la cadena que debe estar contenida en la ruta del archivo: ')  # Reemplaza esto con la cadena que debe estar contenida en la ruta del archivo
archivos_encontrados = encontrar_archivos(patrones, ruta_carpeta, cadena)

print(f"Se encontraron {len(archivos_encontrados)} archivos que coinciden con los patrones {patrones} y cuya ruta contiene '{cadena}':")
for archivo in archivos_encontrados:
    print(archivo)
