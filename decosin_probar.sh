#!/bin/bash


# Para instalar "haiti":
# sudo apt install rubygems
# sudo apt install haiti-hash

echo -e "\n"
echo "        Decodificador"
echo "============================="
echo "Texto a decodificar: " $1
echo -e "\n"

echo "# Base64:"
	echo $1 | base64 -d

echo "# Base32:"
	echo $1 | base32 -d

echo "# Hex a texto:"
	echo $1 | xxd -r -p && echo ''

echo "# ROT13:"
	echo $1 | tr 'A-Za-z' 'N-ZA-Mn-za-m'
	
echo "# ROT47:"
	echo $1 | tr '\!-' 'P-\!-O'	 

echo "# Cesar:"
	echo $1 | tr [h-zabcdef] [a-z] | tr [H-ZABCDEF] [A-Z]	
	
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
	hashcat -m 0 -a 0 $1 rockyou.txt