from cryptography.fernet import Fernet

# Generate a key for encryption/decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_message(message):
    return cipher_suite.encrypt(message.encode())

def decrypt_message(encrypted_message):
    return cipher_suite.decrypt(encrypted_message).decode()
