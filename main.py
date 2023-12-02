from caesar_cipher import caesar_cipher
from base64_operations import base64_encode, base64_decode
from fernet_operations import generate_fernet_key, fernet_encrypt, fernet_decrypt
from hash_operations import md5_hash, sha256_hash, sha512_hash

# Your menu and input handling logic can go here...
# Menu
# Your existing menu logic...
while True:
    print("Encryption Methods Menu:")
    print("1. Caesar Cipher (Encrypt)")
    print("2. Caesar Cipher (Decrypt)")
    print("3. Base64 Encode")
    print("4. Base64 Decode")
    print("5. Fernet Encryption")
    print("6. Fernet Decryption")
    print("7. MD5 Hash")
    print("8. SHA-256 Hash")
    print("9. SHA-512 Hash")
    print("10. Exit")

    choice = input("Enter your choice (1-10): ")

    if choice == '1':
        text = input("Enter text to encrypt: ")
        shift = int(input("Enter the shift value: "))
        result = caesar_cipher(text, shift)
    elif choice == '2':
        text = input("Enter text to decrypt: ")
        shift = int(input("Enter the shift value: "))
        result = caesar_cipher(text, shift, decrypt=True)
    elif choice == '3':
        text = input("Enter text to encode: ")
        result = base64_encode(text)
    elif choice == '4':
        text = input("Enter text to decode: ")
        result = base64_decode(text)
    elif choice == '5':
        text = input("Enter text to encrypt: ")
        key = generate_fernet_key()
        result = fernet_encrypt(text, key)
    elif choice == '6':
        text = input("Enter text to decrypt: ")
        key = input("Enter the Fernet key: ")
        result = fernet_decrypt(text, key)
    elif choice == '7':
        text = input("Enter text to hash: ")
        result = md5_hash(text)
    elif choice == '8':
        text = input("Enter text to hash: ")
        result = sha256_hash(text)
    elif choice == '9':
        text = input("Enter text to hash: ")
        result = sha512_hash(text)
    elif choice == '10':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")
        continue

    print(f"\nResult: {result}\n")