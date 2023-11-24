def descifrar_ascii(codigo_ascii):
    texto = ''
    for numero in codigo_ascii.split():
        texto += chr(int(numero))
    return texto

print(descifrar_ascii(input("Introduce el texto en código ascii:\n    EJEMPLO: 72 111 108 97 33\n    ")))