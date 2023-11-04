alfabeto = 'abcdefghijklmnopqrstuvwxyz'
def descifrar_cesar(codigo, salto):
    descifrado = ''

    if salto=="S":
        
        for jump in range(1, len(alfabeto)):
            print(descifrar_cesar(codigo, jump))
    else:
        salto= int(salto)
        for letra in codigo:
            if letra.lower() in alfabeto:
                isUp = letra.isupper()
                indice = alfabeto.index(letra.lower())
                nuevo_indice = (indice - salto) % len(alfabeto)
                if isUp:
                    descifrado += alfabeto[nuevo_indice].upper()
                else:
                    descifrado += alfabeto[nuevo_indice]
                    
            else:
                descifrado += letra
        return descifrado
        

print(descifrar_cesar(codigo = input("\n\nEJEMPLO: cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}\nRESULTADO: picoCTF{next_time_I'll_try_2_rounds_of_rot13_ulYvpVag}\n    Introduce el texto cifrado en caesar o rot:\n    "), salto = input("\nSI INTRODUCES 'S', APLICARÁ ROT CON VALOR DE SALTO DESDE 1 HASTA "+str(len(alfabeto))+"\nIntroduce el número de salto:\n    ")))
input("ingresa cualquier tecla para salir")