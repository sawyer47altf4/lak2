import base64
from cryptography.fernet import Fernet

print("these is a alpha build 0.1")

text = input("text to encrypt: ")
text = text.encode("utf-8")

def SUPPERSECRET(enc):
    enc1 = base64.b64encode(enc)
    print(enc1)
