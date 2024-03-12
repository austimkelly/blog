import argparse
from cryptography.fernet import Fernet

def process_data(key_file, text, mode):
    try:
        # Load the key
        with open(key_file, 'rb') as file:
            key = file.read()

        # Create a cipher object
        cipher_suite = Fernet(key)

        if mode == 'encode':
            # Convert the text to bytes and encrypt it
            cipher_text = cipher_suite.encrypt(text.encode())
            print(f"Encrypted data: {cipher_text}")
        elif mode == 'decode':
            # Decrypt the text and convert it back to a string
            plain_text = cipher_suite.decrypt(text.encode()).decode('utf-8')
            print(f"Decrypted data: {plain_text}")
        else:
            print("Invalid mode. Please choose 'encode' or 'decode'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Encrypt or decrypt text using a key file.')
    parser.add_argument('key_file', help='The file containing the key.')
    parser.add_argument('text', help='The text to encrypt or decrypt.')
    parser.add_argument('mode', choices=['encode', 'decode'], help='Whether to encrypt (encode) or decrypt (decode) the text.')

    args = parser.parse_args()

    process_data(args.key_file, args.text, args.mode)