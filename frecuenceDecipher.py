from unidecode import unidecode

abc = "abcdefghijklmnñopqrstuvwxyz"
frecuencesABC = {
    "A": 12.16, "B": 1.49, "C": 3.87, "D": 4.67,
    "E": 14.08, "F": 0.69, "G": 1.00, "H": 1.18,
    "I": 5.98, "J": 0.52, "K": 0.11, "L": 5.24,
    "M": 3.08, "N": 6.83, "Ñ": 0.17, "O": 9.2,
    "P": 2.89, "Q": 1.11, "R": 6.41, "S": 7.20,
    "T": 4.60, "U": 4.69, "V": 1.05, "W": 0.04, 
    "X": 0.14, "Y": 1.09, "Z": 0.47
}
frecuencesabc = {clave.lower(): valor for clave, valor in frecuencesABC.items()} #A partir de ahora, usaremos el mismo diccionario, pero sin mayúsculas
def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key
    return "There is no such Key"

def getClosestValue(diccionario, value):
    clave_mas_cercana = min(diccionario, key=lambda k: abs(diccionario[k] - value))
    return clave_mas_cercana, diccionario[clave_mas_cercana]

with open(input("Introduzca el archivo con el contenido a descifrar:\n> "), 'r', encoding='utf-8', errors='ignore') as f:
    cipheredText = unidecode(f.read()).lower() #Convertimos el texto a minúsculas y solo con caracteres ASCII

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
    return length, repeatedLetters

for letter in frecuencesabc:
    length, repeatedLetters = countLetters(cipheredText, abc)
    clave, valor_cercano = getClosestValue(frecuencesabc, ((repeatedLetters.get(letter, 0)*100) / length))
    cipheredText = cipheredText.replace(letter, clave)
    print(f"Valor más cercano a la variable letter({letter}:{((repeatedLetters.get(letter, 0)*100) / len(cipheredText))}%): {clave}:{valor_cercano}")

print(cipheredText)
