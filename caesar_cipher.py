def caesar_cipher(text, shift, decrypt=False):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            if decrypt:
                result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result
