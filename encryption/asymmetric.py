from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Generate a new RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Derive the public key from the private key
public_key = private_key.public_key()

# Serialize the public key to PEM format
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Serialize the private key to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Print the public key in PEM format
print("Public key:", public_pem)

# Print the private key in PEM format
print("Private key:", private_pem)

# Get a message from the user
message = input("Enter a message to encrypt: ").encode()

# Encrypt the message with the public key
ciphertext = public_key.encrypt(
    # The message to be encrypted. In this case, it's the user's input.
    message,
    # The padding scheme to be used. Padding is necessary in many encryption algorithms
    # to ensure that the plaintext fits into the block size of the encryption algorithm.
    # OAEP (Optimal Asymmetric Encryption Padding) is a commonly used padding scheme
    # for RSA encryption. It's secure and recommended for encrypting short messages.
    padding.OAEP(
        # A mask generation function. MGF1 is a commonly used mask generation function.
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        # The hash algorithm to be used. SHA256 is a secure hash algorithm that produces a 256-bit hash.
        algorithm=hashes.SHA256(),
        # An optional label to associate with the message. In this case, no label is used.
        label=None
    )
)

# Print the encrypted message
print("Encrypted message:", ciphertext)

# Decrypt the message with the private key
plaintext = private_key.decrypt(
    # The ciphertext to be decrypted. This is the output of the encryption process.
    ciphertext,
    # The padding scheme used for encryption. This must be the same as the one used for encryption.
    padding.OAEP(
        # The mask generation function used for encryption. This must be the same as the one used for encryption.
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        # The hash algorithm used for encryption. This must be the same as the one used for encryption.
        algorithm=hashes.SHA256(),
        # The label used for encryption. This must be the same as the one used for encryption.
        label=None
    )
)

# Print the decrypted message
print("Decrypted message:", plaintext.decode())
