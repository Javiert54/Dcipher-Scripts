#Necesitas tener rockyou.txt en el mismo directorio que md5.py
with open('nombre_del_archivo.txt', 'r') as archivo:
    lista = [linea.strip() for linea in archivo]

print(lista)