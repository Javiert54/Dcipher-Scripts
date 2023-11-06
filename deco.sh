#!/bin/bash

echo -e "\n"
echo "Decodificador"
echo "============="
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
	echo $1 | tr '\!-~' 'P-~\!-O'	 

echo "# Cesar:"
	echo $1 | tr [h-zabcdef] [a-z] | tr [H-ZABCDEF] [A-Z]	