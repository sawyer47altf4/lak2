import base64
from cryptography.fernet import Fernet

print("these is a alpha build 0.1")

text = input("text to encrypt: ")
text = text.encode("utf-8")

def SUPPERSECRET(enc):
    enc1 = base64.b64encode(enc)
    print(enc1)

def fernetencryption(texttoplaywith):
    ask1 = input("enc = 1, dec = 2 :")
    if ask1 == ("1") or ask1 == ("enc"):
        key = Fernet.generate_key()
        safe = Fernet(key)
        enc = safe.encrypt(texttoplaywith)
        key = key.decode("utf-8")
        enc = enc.decode("utf-8")
        with open("key.txt", "w") as f:
            f.write(key)
        print(f"your key is {key} keep it in a safe place") 
        print(f"your message is {enc}")

    elif ask1 == ("2") or ask1 == ("dec"):
        loadortype = input("load from key.txt has to in lak2 = 1, type manual = 2 :")
        if loadortype == ("1") or loadortype == ("load"):
            with open("key.txt", "r") as f:
                key = f.read()

        elif loadortype == ("2"):
            key = input("plese provide key: ")
        safe = Fernet(key)
        dec = safe.decrypt(texttoplaywith)
        dec = dec.decode("utf-8")
        print(dec)
    
print("1, super secret base64 encode only")
print("2, fernet")
whatcipher = input("1, 2")
### add if for code here