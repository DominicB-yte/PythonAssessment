from Encoder import Security

Cryption = int(input("1. Encrypt\n2. Decrypt\n: "))

def Main():
    if Cryption == 1:
        Cipher = int(input("1. Encrypt in Caesar\n2. Encrypt in Polyalphabetical\n: "))
        if Cipher == 1:
            CEinput = input("What would you like to Encrypt?: ")
            Security.CaesarEncrypt(CEinput)
        elif Cipher == 2:
            PEinput = input("What would you like to Encrypt?: ")
            Security.PolyEncrypt(PEinput)


    if Cryption == 2:
        Decode = int(input("1. Decrypt Caesar\n2. Decrypt Polyalphabetical\n: "))
        if Decode == 1:
            CDinput = input("What would you like to Decrypt?: ")
            Security.CaesarDecrypt(CDinput)
        elif Decode == 2:
            PDinput = input("What would you like to Decrypt?: ")
            Security.PolyDecrypt(PDinput)

if __name__ == "__main__":
    Main()
