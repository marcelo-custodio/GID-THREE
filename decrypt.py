import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.ECB())

encryptor = cipher.encryptor()
ciphertext = encryptor.update(b"a secret message") + encryptor.finalize()
print(ciphertext)

decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()
print(plaintext)