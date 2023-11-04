x = []
a = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
while True:
    try:
        x_str= input("Ingresa el mensaje encriptado en 'Modular Inverse' (SEPARADO POR ESPACIOS).\n    EJEMPLO: 104 372 110 436 262 173 354 393 351 297 241 86 262 359 256 441 124 154 165 165 219 288 42\n    ")
        x = [int(num) for num in x_str.split()]
        break
    except ValueError:
        print("Por favor, introduce solo números separados por espacios.")
        # Encuentra el primer elemento no numérico
        for i, num in enumerate(x_str.split()):
            try:
                int(num)
            except ValueError:
                print(f"El elemento {i+1} ('{num}') no es un número.")
                break

# Solicita al usuario que ingrese el divisor
while True:
    try:
        divisor = int(input("\nIngresa el número mod.\n    EJEMPLO: 41\n    "))
        break
    except ValueError:
        print("Por favor, introduce un número.")
        
def inverso_modular(a, m):
    if m == 1:
        return 0
    else:
        g, x, y = algoritmo_extendido_euclides(a, m)
        if g != 1:
            raise Exception('El inverso modular no existe')
        else:
            return x % m

def algoritmo_extendido_euclides(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = algoritmo_extendido_euclides(b % a, a)
        return g, y - (b // a) * x, x

for i in x:
    print(a[inverso_modular(i, divisor)], end="")