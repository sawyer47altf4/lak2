import base64

print("these is a alpha build 0.1")
# version
print("i can convert text to base64 right now")
# make a list on what the program can convert
choice = input("what do you wnat to use to convert the text :")
# chose what to convert the text in the store var
# match case is like if but better soooo yah
match choice:
    case "base64":
        match input("enc or dec:"):
            case "enc":
                data = input("text to encypt: ")
                data = data.encode("utf-8")
                data = base64.b64encode(data)
                print(data.decode("utf-8"))
            case "dec":
                data = input("base64 to convert back:")
                data = base64.b64decode(data)
                print(data.decode("utf-8"))