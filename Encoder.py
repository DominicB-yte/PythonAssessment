import pathlib

characters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "\n", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "<", ">", ",", ".", "?", "/", "\\", "|", "[", "]", "{", "}", ";", ":", " "
]

class Security:
    def CaesarDecrypt(self):

        CDshift = int(input("Please type the amount to shift by: "))
        encrypted = self
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
