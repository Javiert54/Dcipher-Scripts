def offset(even, rails, rail):
    if rail == 0 or rail == rails - 1:
        return (rails - 1) * 2

    if even:
        return 2 * rail
    else:
        return 2*(rails - 1 - rail)



def decryptRailFence(encrypted, rails):
    
    if rails=="S":
        for i in range(round(len(encrypted)/2)):
            print(decryptRailFence(encrypted, i))
    
    else:
    
        rails= int(rails)
        array = [[" " for col in range(len(encrypted))] for row in range(rails)]
        read = 0
        
        #build our fence
        for rail in range(rails):
            pos = offset(1, rails, rail)
            even = 0;
            
            if rail == 0:
                pos = 0
            else:
                pos = int(pos / 2)
            
            while pos < len(encrypted):
                if read == len(encrypted):
                    break

                array[rail][pos] = encrypted[read];
                read = read + 1

                pos = pos + offset(even, rails, rail)
                even = not even

        #now return the decoded message
        decoded = ""

        for x in range(len(encrypted)):
            for y in range(rails):
                if array[y][x] != " ":
                    decoded += array[y][x]

        return decoded
print(decryptRailFence(input("Introduce el texto cifrado en rail-fence:\nEJEMPLO: Ta _7N6D8Dhlg:W3D_H3C31N__387ef sHR053F38N43DFD i33___N6\n"), input("Introduce el número de railes:\n(Si no sabes el número de railes, introduce S, y aplicará fuerza bruta)\nEJEMPLO: 4\n")))
