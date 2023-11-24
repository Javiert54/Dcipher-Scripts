import hashlib

#Necesitas tener rockyou.txt en el mismo directorio que md5.py
with open('rockyou.txt', 'r', errors='ignore') as archivo:
    passwordsList = [linea.strip() for linea in archivo]

#Para mostrar la lista del blog de notas
# print(passwordsList)

def hash_md5(cadena):
    resultado = hashlib.md5(cadena.encode())
    return resultado.hexdigest()

def decipherMd5(passwordMd5):
	for password in passwordsList:
		if hash_md5(password) == passwordMd5:
			return("Contraseña encontrada!\n    passwordMd5: "+ str(passwordMd5)+" | Password: "+str(password))
	return "Contraseña no encontrada :("

print(decipherMd5(input("Introduce el texto hasheado en md5:\n    ")))