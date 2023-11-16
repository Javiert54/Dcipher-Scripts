import hashlib
def calcular_sha256(archivo):
    md5_hash = hashlib.md5() #Instancia de hash md5
    sha256_hash = hashlib.sha256() #Instancia de hash sha256
    sha1_hash = hashlib.sha1() # Instancia de hash sha1
    with open(archivo,"rb") as f: # Abrir archivo en modo binario
        for byte_block in iter(lambda: f.read(4096),b""): # Interar en el archivo
            md5_hash.update(byte_block) # Actualizar el hash de md5
            sha256_hash.update(byte_block) # Actualizar el hash de sha256
            sha1_hash.update(byte_block) # Actualizar el hash de sha1    
    #Imprimir los hashes
    print("SHA256: ", sha256_hash.hexdigest(), "\nSHA1: ", sha1_hash.hexdigest(), "\nmd5: ", md5_hash.hexdigest()) 
#Ejecutar la función recién declarada pidiendo la ruta del archivo a hashear
calcular_sha256(input("Introduce la ruta del fichero:\n"))