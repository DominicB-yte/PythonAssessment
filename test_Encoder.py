import pathlib
from io import StringIO
import pytest
from Encoder import Security

@pytest.mark.caesarencrypt
def test_caesar_encrypt_ifstr(monkeypatch):
    shift_to_encrypt = StringIO('3\n')
    monkeypatch.setattr('sys.stdin', shift_to_encrypt)
    assert isinstance(Security.CaesarEncrypt("Test.txt"), str)

def test_caesar_encrypt_samestr(monkeypatch):
    location = pathlib.Path(__file__).parent / "Test.txt"
    with open(location, 'r') as FileToEncrypt:
        data = FileToEncrypt.read()
    shift_to_encrypt = StringIO('3\n')
    monkeypatch.setattr('sys.stdin', shift_to_encrypt)
    assert Security.CaesarEncrypt("CaesarEncrypted.txt") != data
#####################################################################################################

@pytest.mark.caesardecrypt
def test_caesar_decrypt_ifstr(monkeypatch):
    shift_to_decrypt = StringIO('3\n')
    monkeypatch.setattr('sys.stdin', shift_to_decrypt)
    assert isinstance(Security.CaesarDecrypt("CaesarEncrypted.txt"), str)

def test_caesar_decrypt_samestr(monkeypatch):
    location = pathlib.Path(__file__).parent / "CaesarEncrypted.txt"
    with open(location, 'r') as FileToEncrypt:
        data = FileToEncrypt.read()
    shift_to_encrypt = StringIO('3\n')
    monkeypatch.setattr('sys.stdin', shift_to_encrypt)
    assert Security.CaesarDecrypt("CaesarDecrypted.txt") != data
#####################################################################################################

@pytest.mark.polyencrypt
def test_poly_encrypt_ifstr(monkeypatch):
    shift_to_encrypt = StringIO('HelloWorld\n')
    monkeypatch.setattr('sys.stdin', shift_to_encrypt)
    assert isinstance(Security.PolyEncrypt("Test.txt"), str)

def test_poly_encrypt_samestr(monkeypatch):
    location = pathlib.Path(__file__).parent / "Test.txt"
    with open(location, 'r') as FileToEncrypt:
        data = FileToEncrypt.read()
    shift_to_encrypt = StringIO('HelloWorld\n')
    monkeypatch.setattr('sys.stdin', shift_to_encrypt)
    assert Security.PolyEncrypt("PolyEncrypted.txt") != data
#####################################################################################################

@pytest.mark.polydecrypt
def test_poly_decrypt_ifstr(monkeypatch):
    shift_to_decrypt = StringIO('HelloWorld\n')
    monkeypatch.setattr('sys.stdin', shift_to_decrypt)
    assert isinstance(Security.PolyDecrypt("PolyEncrypted.txt"), str)

def test_poly_decrypt_samestr(monkeypatch):
    location = pathlib.Path(__file__).parent / "PolyEncrypted.txt"
    with open(location, 'r') as FileToEncrypt:
        data = FileToEncrypt.read()
    shift_to_encrypt = StringIO('HelloWorld\n')
    monkeypatch.setattr('sys.stdin', shift_to_encrypt)
    assert Security.PolyDecrypt("PolyDecrypted.txt") != data