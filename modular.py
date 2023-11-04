alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
#Si utilizas alfabeto ESPAÑOL, añade la "Ñ"

# Solicita al usuario que ingrese los valores
while True:
    try:
        x_str = input('Ingresa el mensaje encriptado en "modular" (SEPARADO POR ESPACIOS).\n    EJEMPLO: 350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213\n    ')
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
        divisor = int(input("\nIngresa el número mod.\n    EJEMPLO: 37\n    "))
        break
    except ValueError:
        print("Por favor, introduce un número.")

for i in x:
    print(alfabeto[i% divisor], end="")