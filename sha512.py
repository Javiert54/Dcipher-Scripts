import hashlib

#Necesitas tener rockyou.txt en el mismo directorio que sha512.py
with open('rockyou.txt', 'r', errors='ignore') as archivo:
    passwordsList = [linea.strip() for linea in archivo]

def dcryptSha256(texto):
    for password in passwordsList:
        # print(passwordsList.index(password))
        if hashlib.sha512(password.encode()).hexdigest() == texto:
            return 'Contraseña encontrada!\n    PasswordSha256: '+str(texto)+" | " + "Password: "+str(password)
    return 'Contraseña no encontrada :('

print(dcryptSha256(input("Introduce el texto cifrado en sha512:\n    ")))