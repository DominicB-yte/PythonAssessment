from Encoder import CaesarEncrypt, CaesarDecrypt
Cryption = int(input("1. Encrypt\n2. Decrypt\n: "))

if Cryption == 1:
    Cipher = int(input("1. Encrypt in Caesar\n2. Encrypt in Polyalphabetical\n: "))
    if Cipher == 1:
        CaesarEncrypt()
    elif Cipher == 2:
        pass
        # Encrypt in Polyalphabetical

if Cryption == 2:
    Decode = int(input("1. Decrypt Caesar\n2. Decrypt Polyalphabetical\n: "))
    if Decode == 1:
        CaesarDecrypt()
    elif Decode == 2:
        pass
        # Decrypt in Polyalphabetical
