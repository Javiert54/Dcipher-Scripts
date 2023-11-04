import itertools

def descifrar_transposicion(texto_cifrado, num_caracteres):
    
    if num_caracteres == "S":
        for i in range(2, round(len(texto_cifrado)/2)):
            print(descifrar_transposicion(texto_cifrado, i))
    else:
        num_caracteres = int(num_caracteres)
        unidades = [texto_cifrado[i:i+num_caracteres] for i in range(0, len(texto_cifrado), num_caracteres)]
        permutaciones = ["".join(p) for u in unidades for p in itertools.permutations(u)]
        num_permutaciones_primer_elemento = len(list(itertools.permutations(unidades[0])))

        # Borrar el contenido del archivo 'permutaciones.txt' antes de iniciar el bucle
        open('permutaciones.txt', 'w').close()

        permutaciones_agrupadas = {}
        for i in range(len(permutaciones)):
            resto = i % num_permutaciones_primer_elemento
            if resto in permutaciones_agrupadas:
                permutaciones_agrupadas[resto] += permutaciones[i]
            else:
                permutaciones_agrupadas[resto] = permutaciones[i]

            # Guardar cada elemento de permutaciones_agrupadas en un archivo de texto
            if i > len(permutaciones)- num_permutaciones_primer_elemento:
                with open('permutaciones.txt', 'a') as f:
                    f.write(permutaciones_agrupadas[resto]+ '\n')

        return permutaciones_agrupadas

print(
descifrar_transposicion(
    input("Introduce el texto cifrado\n    EJEMPLO: heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2\n    "),
    input("Ingresa el número de letras por bloque\n    EJEMPLO: 3\n    "),
))