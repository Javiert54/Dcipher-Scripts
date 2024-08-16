from unidecode import unidecode

abc = "abcdefghijklmnnñopqrstuvwxyz"

frecuencesABC = {
    "A": 0.1216, "B": 0.0149, "C": 0.0387, "D": 0.0467,
    "E": 0.1408, "F": 0.0069, "G": 0.0100, "H": 0.0118,
    "I": 0.0598, "J": 0.0052, "K": 0.0011, "L": 0.0524,
    "M": 0.0308, "N": 0.0683, "Ñ": 0.0017, "O": 0.092,
    "P": 0.0289, "Q": 0.0111, "R": 0.0641, "S": 0.0720,
    "T": 0.0460, "U": 0.0469, "V": 0.0105, "W": 0.0004, 
    "X": 0.0014, "Y": 0.0109, "Z": 0.0047
}

def eliminar_acentos(cadena):
    with open(input("Introduzca el archivo con el contenido a descifrar:\n> "), 'r', encoding='utf-8', errors='ignore') as f:
        return [unidecode(i).lower() for i in  cadena.split("ñ")].join("ñ")  #Convertimos el texto a minúsculas y solo con caracteres ASCII

frecuencesabc = {clave.lower(): valor for clave, valor in frecuencesABC.items()} #A partir de ahora, usaremos el mismo diccionario, pero sin mayúsculas
def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key
    return "There is no such Key"

def getClosestValue(diccionario, value):
    # Ordenar los ítems del diccionario según la distancia absoluta de sus valores a la variable
    items_ordenados = sorted(diccionario.items(), key=lambda item: abs(item[1] - value))
    # Seleccionar los tres primeros elementos de la lista ordenada
    tres_mas_cercanos = items_ordenados[:3]
    # Convertir la lista de tuplas de vuelta a un diccionario
    return dict(tres_mas_cercanos)

with open(input("Introduzca el archivo con el contenido a descifrar:\n> "), 'r', encoding='utf-8', errors='ignore') as f:
    cipheredText = eliminar_acentos(f.read) #Convertimos el texto a minúsculas y solo con caracteres ASCII

def countLetters(text, alphabet):
    length = 0
    repeatedLetters = {}

    for letter in text:
        if letter not in alphabet:
            continue
        if letter not in repeatedLetters:
            repeatedLetters[letter] = 1
        else:
            repeatedLetters[letter] += 1

        length +=1
    value = 0
    key = ""
    for k, val in repeatedLetters.items():
        if val > value:
            value = val
            key = k
    return length, value, key

length, value, letter = countLetters(cipheredText, abc)
usagePorcentage = (value)/length
closestValues = getClosestValue(frecuencesabc, usagePorcentage)
print(f"Valores más cercanos a {letter}({usagePorcentage}):", closestValues)
for key, value in closestValues.items():
    if abc.find(key) - abc.find(letter)>=0:
        jump = abc.find(letter) - abc.find(key)
    else:
        jump = abc.find(key) - abc.find(letter)
    index = 0
    result =""
    for character in cipheredText:
        if character in abc:
            characterIndex = abc.find(character)
            # if (characterIndex + jump ) < 0:
            #     result += abc[characterIndex - jump]
            # else:
            #     result += abc[characterIndex + jump]
            result += abc[(characterIndex + jump) % len(abc)]
            continue
        result += character
    print("salto: ",jump)
    print(result)
