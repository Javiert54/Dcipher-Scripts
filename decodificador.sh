!/bin/bash

# Para instalar "haiti":
# sudo apt install rubygems
# sudo gem install haiti-hash
#MODO DE USO:
#vboxuser@ubuntu:$ ./decodificador.sh <texto cifrado>



echo -e "\n"
echo "        Decodificador"
echo "============================="
echo "Texto a decodificar: " $1
echo -e "\n"

echo "# Base64:"
        echo $1 | base64 -d
echo ""

echo "# Base32:"
        echo $1 | base32 -d
echo ""
echo "# Hex a texto:"
        echo $1 | xxd -r -p && echo ''
echo ""
echo "# ROT13:"
        echo $1 | tr 'A-Za-z' 'N-ZA-Mn-za-m'
echo ""
echo "# ROT47:"
        echo $1 | tr '\!-' 'P-\!-O'      
echo ""
echo "# Cesar:"
        echo $1 | tr [h-zabcdef] [a-z] | tr [H-ZABCDEF] [A-Z]   
echo ""
echo -e "\n"
echo "    Descubriendo el hash"
echo "=============================="
echo -e "\n# Con hashid:"
        hashid -m $1 | head -n6

echo -e "\n# Con haiti:"
        haiti $1 | head -n5

echo -e "\n"
echo "    Descifrando md5"
echo "=============================="
        hashcat -m 0 -a 0 -o cracked.txt $1 rockyou.txt | grep $1
echo "=============================="
echo "Si se pudo crackear el texto, se guardo en cracked.txt"
