from cryptography.fernet import Fernet

def generate_fernet_key():
    return Fernet.generate_key()

def fernet_encrypt(text, key):
    cipher = Fernet(key)
    return cipher.encrypt(text.encode()).decode()

def fernet_decrypt(text, key):
    cipher = Fernet(key)
    return cipher.decrypt(text.encode()).decode()
