import hashlib

def calcular_sha256(archivo):
    sha256_hash = hashlib.sha256()
    sha1_hash = hashlib.sha1()
    md5_hash = hashlib.md5()
    with open(archivo,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
            sha1_hash.update(byte_block)
            md5_hash.update(byte_block)
        print("SHA256: ", sha256_hash.hexdigest(), "\nSHA1: ", sha1_hash.hexdigest(), "\nMD5: ", md5_hash.hexdigest())

prompt =input("Introduce la ruta del fichero: ")
calcular_sha256(prompt)