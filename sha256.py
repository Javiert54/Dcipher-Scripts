import hashlib

#Necesitas tener rockyou.txt en el mismo directorio que sha256.py
with open('rockyou.txt', 'r', errors='ignore') as archivo:
    passwordsList = [linea.strip() for linea in archivo]
    
def dcryptSha256(texto):
    for password in passwordsList:
        if hashlib.sha256(password.encode()).hexdigest() == texto:
            return 'Contraseña encontrada!\n    PasswordSha256: '+str(texto)+" | " + "Password: "+str(password)
    return 'Contraseña no encontrada :('

print(dcryptSha256(input("Introduce el texto cifrado en sha256:\n    ")))