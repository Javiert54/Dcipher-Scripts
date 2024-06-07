import os
import fnmatch
import shutil

ruta_script = os.path.dirname(os.path.realpath(__file__))

def encontrar_archivos(patrones, ruta, cadenas=None):
    archivos_coincidentes = []
    for raiz, dirs, archivos in os.walk(ruta):
        for patron in patrones:
            for archivo in fnmatch.filter(archivos, patron):
                ruta_completa = os.path.join(raiz, archivo)
                if cadenas is None or any(cadena in ruta_completa for cadena in cadenas):
                    archivos_coincidentes.append(ruta_completa)
    return archivos_coincidentes

# Ejemplo de uso
patrones = input('Introduce los patrones que estes buscando, separandolos con ";". Por ejemplo: *.db;*.pdf;*.html\n    (si no quieres buscar ningun patron en particular, solo pulsa ENTER)\n').split(';')
ruta_carpeta = input('Introduce la ruta a la carpeta: ')
cadenas_input = input('Introduce las cadenas que deben estar contenidas en la ruta del archivo (si son varias palabras que pueden no estar pegadas, sepáralas con ";" EJEJMPLO: google;gmail;sent):\n')
cadenas = None if cadenas_input == '' else cadenas_input.split(';')
archivos_encontrados = encontrar_archivos(patrones, ruta_carpeta, cadenas)

newFolder = os.path.join(ruta_script, 'outputFiles')
if not os.path.exists(newFolder):
    os.makedirs(newFolder)
else:
    for filename in os.listdir(newFolder):
        file_path = os.path.join(newFolder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Error al borrar {file_path}. Razón: {e}')

print(f"Se encontraron {len(archivos_encontrados)} archivos que coinciden con los patrones {patrones} y cuya ruta contiene '{cadenas}':")
for archivo in archivos_encontrados:
    shutil.copy(archivo, newFolder)
    print(archivo)
print('Archivos guardados en:', newFolder)
