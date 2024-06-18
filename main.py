import base64
from cryptography.fernet import Fernet
from tkinter import *

print("these is a alpha build v0.6")

#text = input("text to encrypt: ").encode("utf-8")

def fernetcipher(texttoplaywith):   # need to make new function to encrypt text and make key, and make one to decrypt 
    encdec = input("enc = 1, dec = 2 :")  # get rid of all input(), and try to remove if statments
    if encdec == ("1") or encdec == ("enc"):
        key = Fernet.generate_key()
        safe = Fernet(key)
        enc = safe.encrypt(texttoplaywith)
        key = key.decode("utf-8")
        enc = enc.decode("utf-8")
        with open("key.txt", "w") as f:
            f.write(key)
        print(f"your key is {key} keep it in a safe place") 
        print(f"your message is {enc}")

    elif encdec == ("2") or encdec == ("dec"):
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

root = Tk()

mainname = Label(root, text="project Lock And Key").grid(row=1, column=1)
version = Label(root, text="av0.6").grid(row=2, column=1)
needkey = Label(root, text="input key").grid(row=3, column=1)
key = Entry(root).grid(row=3, column=2)
needencodedtext = Label(root, text="input encoded message").grid(row=4, column=1)
encodetext = Button(root, text="encrypt message").grid(row=1, column=2)
decodetext = Button(root, text="decode message").grid(row=2, column=2)
encodedtext = Entry(root).grid(row=4, column=2)
output = Label(root, text=f"output: ").grid(row=5, column=1)

root.mainloop()