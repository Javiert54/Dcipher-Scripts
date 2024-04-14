import socket
import subprocess

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



# Define el comando que quieres ejecutar
# comando = f"python hoaxshell.py -s {direccion_ip}"
comando ="ls -l"
# Usa subprocess para ejecutar el comando
proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, shell=True)

# Recupera la salida y el código de error
salida, error = proceso.communicate()

if proceso.returncode == 0:
    print(salida.decode())
else:
    print("Hubo un error al ejecutar el comando.")