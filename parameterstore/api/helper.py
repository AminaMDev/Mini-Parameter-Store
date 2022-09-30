
from cryptography.fernet import Fernet
from django.conf import settings

class Encryption():
    fernet =  Fernet(bytes(settings.FERNET_KEY, 'utf-8'))

    def encrypt(text):
        return Encryption.fernet.encrypt(text.encode())

    def decrypt(cipher):
        return Encryption.fernet.decrypt(cipher).decode()
