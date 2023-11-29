import math
from bitarray import bitarray

def criba_eratostenes(maxNum):
    compuestos = bitarray(maxNum)
    compuestos.setall(False)
    primos = []
    if maxNum > 2:
        primos.append(2)
    for i in range(3, math.isqrt(maxNum) + 1, 2):
        if not compuestos[i]:
            primos.append(i)
            compuestos[i*i : maxNum : i] = True
    for i in range(math.isqrt(maxNum) + 1, maxNum, 2):
        if not compuestos[i]:
            primos.append(i)
    return primos

maxNum = int(input("Introduce el número máximo: "))
lista = criba_eratostenes(maxNum)
print(lista)
print("Números primos encontrados: ",len(lista))