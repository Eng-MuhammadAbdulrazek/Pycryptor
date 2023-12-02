import hashlib

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def sha512_hash(text):
    return hashlib.sha512(text.encode()).hexdigest()
