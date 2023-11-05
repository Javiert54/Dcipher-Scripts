#!/bin/bash

# Solicita que ingrese hexadecimal
read -p "Ingresa hexadecimal: " hex_string

# Convertir hexadecimal a texto
original_text=$(echo -n "$hex_string" | xxd -r -p)

echo "Texto original: $original_text"

