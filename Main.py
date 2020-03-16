import pathlib
from Encoder import Security

Cryption = int(input("1. Encrypt\n2. Decrypt\n: "))

def Main():
    if Cryption == 1:
        Cipher = int(input("1. Encrypt in Caesar\n2. Encrypt in Polyalphabetical\n: "))
        if Cipher == 1:
            CEinput = input("What file would you like to Encrypt?: ")
            theFile = CEinput + ".txt"
            CEFile = pathlib.Path(__file__).parent / theFile
            Security.CaesarEncrypt(CEFile)
        elif Cipher == 2:
            PEinput = input("What file would you like to Encrypt?: ")
            theFile = PEinput + ".txt"
            PEFile = pathlib.Path(__file__).parent / theFile
            Security.PolyEncrypt(PEFile)


    if Cryption == 2:
        Decode = int(input("1. Decrypt Caesar\n2. Decrypt Polyalphabetical\n: "))
        if Decode == 1:
            CDinput = input("What file would you like to Decrypt?: ")
            theFile = CDinput + ".txt"
            CDFile = pathlib.Path(__file__).parent / theFile
            Security.CaesarDecrypt(CDFile)
        elif Decode == 2:
            PDinput = input("What file would you like to Decrypt?: ")
            theFile = PDinput + ".txt"
            PDFile = pathlib.Path(__file__).parent / theFile
            # Security.PolyDecrypt(PDFile)

if __name__ == "__main__":
    Main()
