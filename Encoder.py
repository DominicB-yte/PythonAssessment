import pathlib

characters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "\n", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "<", ">", ",", ".", "?", "/", "\\", "|", "[", "]", "{", "}", ";", ":", " "
]

class Security:
    def CaesarEncrypt(self):
        CEshift = int(input("Please type the amount to shift by: "))
        location = pathlib.Path(__file__).parent / self
        toFile = pathlib.Path(__file__).parent / "CaesarEncrypted.txt"
        with open(location, 'r') as FileToEncrypt:
            data = FileToEncrypt.read()
        SplitFile = list(data)
        Encrypted = []

        for i in SplitFile:
            if i in characters:
                CharIn = characters.index(i)
                newChar = characters[(CharIn + CEshift) % len(characters)]
                Encrypted.append(newChar)

        EncryptStr = ''.join(Encrypted)
        print("Successfully Encrypted File!")

        newFile = open(toFile, "w")
        newFile.write(EncryptStr)
        return EncryptStr

    def CaesarDecrypt(self):
        CDshift = int(input("Please type the amount to shift by: "))
        encrypted = pathlib.Path(__file__).parent / self
        toDecrypt = pathlib.Path(__file__).parent / "CaesarDecrypted.txt"

        with open(encrypted, 'r') as FileToDecrypt:
            data = FileToDecrypt.read()
        SplitFile = list(data)
        Decrypted = []

        for j in SplitFile:
            if j in characters:
                CharIn = characters.index(j)
                newChar = characters[(CharIn - CDshift) % len(characters)]
                Decrypted.append(newChar)

        DecryptStr = ''.join(Decrypted)
        print("Successfully Decrypted File!")

        newFile = open(toDecrypt, "w")
        newFile.write(DecryptStr)
        return DecryptStr

    def PolyEncrypt(self):
        PEkey = input("Please enter your Keyword: ")
        location = pathlib.Path(__file__).parent / self
        toFile = pathlib.Path(__file__).parent / "PolyEncrypted.txt"
        with open(location, 'r') as FileToEncrypt:
            data = FileToEncrypt.read()
        SplitFile = list(data)
        Encrypted = []
        SplitKey = list(PEkey)

        for i in SplitKey:
            if i in characters:
                move = characters.index(i)
        for j in SplitFile:
            if j in characters:
                CharIn = characters.index(j)
                newChar = characters[(CharIn + move) % len(characters)]
                Encrypted.append(newChar)

        EncryptStr = ''.join(Encrypted)
        print("Successfully Encrypted File!")

        newFile = open(toFile, "w")
        newFile.write(EncryptStr)
        return EncryptStr

    def PolyDecrypt(self):
        PDkey = input("Please enter your Keyword: ")
        location = pathlib.Path(__file__).parent / self
        toFile = pathlib.Path(__file__).parent / "PolyDecrypted.txt"
        with open(location, 'r') as FileToEncrypt:
            data = FileToEncrypt.read()
        SplitFile = list(data)
        Decrypted = []
        SplitKey = list(PDkey)

        for i in SplitKey:
            if i in characters:
                move = characters.index(i)
        for j in SplitFile:
            if j in characters:
                CharIn = characters.index(j)
                newChar = characters[(CharIn - move) % len(characters)]
                Decrypted.append(newChar)

        DecryptStr = ''.join(Decrypted)
        print("Successfully Decrypted File!")

        newFile = open(toFile, "w")
        newFile.write(DecryptStr)
        return DecryptStr