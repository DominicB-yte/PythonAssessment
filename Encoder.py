characters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "<", ">", ",", ".", "?", "/", "\\", "|", "[", "]", "{", "}", ";", ":"
]


class Security:
    def CaesarEncrypt(self):
        CEshift = int(input("Please type the amount to shift by: "))
        File = list(self)
        Encrypted = []

        for i in File:
            if i in characters:
                CharIn = characters.index(i)
                newChar = characters[(CharIn + CEshift) % len(characters)]
                Encrypted.append(newChar)

        EncryptStr = ''.join(Encrypted)
        print("Successfully Encrypted Text!")

        print(EncryptStr)
        return EncryptStr

    def CaesarDecrypt(self):
        CDshift = int(input("Please type the amount to shift by: "))
        encrypted = list(self)
        Decrypted = []

        for j in encrypted:
            if j in characters:
                CharIn = characters.index(j)
                newChar = characters[(CharIn - CDshift) % len(characters)]
                Decrypted.append(newChar)

        DecryptStr = ''.join(Decrypted)
        print("Successfully Decrypted Text!")

        print(DecryptStr)
        return DecryptStr

    def PolyEncrypt(self):
        PEkey = input("Please enter your Keyword: ")
        File = list(self)
        Encrypted = []
        Move = []
        SplitKey = list(PEkey)

        for i in SplitKey:
            if i in characters:
                moveChar = characters.index(i)
                Move.append(moveChar)
        cnt = 0
        for stg in File:
            if stg in characters:
                CharIn = characters.index(stg)
                CharMove = Move[cnt % len(Move)]
                newChar = characters[(CharIn + CharMove) % len(characters)]
                Encrypted.append(newChar)
            cnt += 1

        EncryptStr = ''.join(Encrypted)
        print("Successfully Encrypted Text!")

        print(EncryptStr)
        return EncryptStr

    def PolyDecrypt(self):
        PDkey = input("Please enter your Keyword: ")
        File = list(self)
        Decrypted = []
        Move = []
        SplitKey = list(PDkey)

        for i in SplitKey:
            if i in characters:
                moveChar = characters.index(i)
                Move.append(moveChar)
        cnt = 0
        for stg in File:
            if stg in characters:
                CharIn = characters.index(stg)
                CharMove = Move[cnt % len(Move)]
                newChar = characters[(CharIn - CharMove) % len(characters)]
                Decrypted.append(newChar)
            cnt += 1

        DecryptStr = ''.join(Decrypted)
        print("Successfully Decrypted Text!")

        print(DecryptStr)
        return DecryptStr