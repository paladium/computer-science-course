from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Random import new as Random
from base64 import b64encode
from base64 import b64decode


class RSA_Cipher:
    def generate_key(self, key_length):
        rng = Random().read
        self.key = RSA.generate(key_length, rng)

    def encrypt(self, data):
        plaintext = b64encode(data.encode())
        rsa_encryption_cipher = PKCS1_v1_5.new(self.key)
        ciphertext = rsa_encryption_cipher.encrypt(plaintext)
        return b64encode(ciphertext).decode()

    def decrypt(self, data):
        ciphertext = b64decode(data.encode())
        rsa_decryption_cipher = PKCS1_v1_5.new(self.key)
        plaintext = rsa_decryption_cipher.decrypt(ciphertext, 16)
        return b64decode(plaintext).decode()


#Initialise our cipher
cipher = RSA_Cipher()
cipher.generate_key(1024)
print("n = {}, e = {}, d = {}, p = {}, q = {}, u = {}".format(cipher.key.n, cipher.key.e, cipher.key.d, cipher.key.p, cipher.key.q, cipher.key.u))
encrypted = cipher.encrypt("hello!")
print(encrypted)
print(cipher.decrypt(encrypted))