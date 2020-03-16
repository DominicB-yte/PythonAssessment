import pathlib

characters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "\n", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "<", ">", ",", ".", "?", "/", "\\", "|", "[", "]", "{", "}", ";", ":", " "
]

class Security:
    def PolyDecrypt(self):
        PDkey = input("Please enter your Keyword: ")
        location = self
        toFile = pathlib.Path(__file__).parent / self
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