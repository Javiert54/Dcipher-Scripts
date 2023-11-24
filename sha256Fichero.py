import hashlib

def calcular_sha256(archivo):
    sha256_hash = hashlib.sha256()
    sha1_hash = hashlib.sha1()
    with open(archivo,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
            sha1_hash.update(byte_block)
        print("SHA256: ", sha256_hash.hexdigest(), "\n", "SHA1: ", sha1_hash.hexdigest())

prompt =input("Introduce la ruta del fichero:\n")
calcular_sha256(prompt)