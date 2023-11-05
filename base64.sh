#!/bin/bash

# Primero lo comprueba
is_base64() {
  if [[ "$1" =~ ^[A-Za-z0-9+/]*=*$ ]]; then
    return 0 # Válido
  else
    return 1 # No válido
  fi
}

#desencripta
decode_base64() {
  echo "$1" | base64 -d
}

if [ $# -ne 1 ]; then
  echo "Uso: $0 <cadena_base64>"
  exit 1
fi

cadena_base64="$1"

# Comprobar
if is_base64 "$cadena_base64"; then
  # Desencriptar Base64
  resultado=$(decode_base64 "$cadena_base64")
  echo "Resultado: $resultado"
else
  echo "Eso no es una cadena Base64 válida."
fi

