# Simple example to show inputs and outputs of various hashing algorithms.
# This is useful to testing offline hash cracking.

import hashlib

def hash_sha1(strings):
    for s in strings:
        result = hashlib.sha1(s.encode())
        print(f'SHA1: {result.hexdigest()}')

def hash_sha256(strings):
    for s in strings:
        result = hashlib.sha256(s.encode())
        print(f'SHA256: {result.hexdigest()}')

def hash_sha256_salt(strings, salt):
    for s in strings:
        s += salt  # Add the salt to the string
        result = hashlib.sha256(s.encode())
        print(f'SHA256 Salted: {result.hexdigest()}')

def hash_sha256_with_salt_and_pepper(strings, salt, pepper):
    for s in strings:
        s = s + salt + pepper  # Add the salt and pepper to the string
        result = hashlib.sha256(s.encode())
        print(f'SHA256: {result.hexdigest()}')

def hash_md5(strings):
    for s in strings:
        result = hashlib.md5(s.encode())
        print(f'MD5: {result.hexdigest()}')

def hash_sha224(strings):
    for s in strings:
        result = hashlib.sha224(s.encode())
        print(f'SHA224: {result.hexdigest()}')

def hash_sha384(strings):
    for s in strings:
        result = hashlib.sha384(s.encode())
        print(f'SHA384: {result.hexdigest()}')

def hash_sha512(strings):
    for s in strings:
        result = hashlib.sha512(s.encode())
        print(f'SHA512: {result.hexdigest()}')

# Test the functions
salt = "somesalt"
pepper = "somepepper"
strings_to_hash = ['HelloWorld', "P@ssword123", "ch1ck3n5OOp", "FyHmPVBtAV3G9y0eDdkf"]
hash_sha1(strings_to_hash)
# hash_md5(strings_to_hash)
# hash_sha256(strings_to_hash)
# hash_sha224(strings_to_hash)
# hash_sha384(strings_to_hash)
# hash_sha512(strings_to_hash)
# hash_sha256_salt(strings_to_hash, salt)
hash_sha256_with_salt_and_pepper(strings_to_hash, salt, pepper)

# Salt: A salt is random data that is used as an additional input to a hash 
# function. The primary function of salts is to defend against dictionary attacks 
# or against pre-computed rainbow table attacks. For each password, a unique salt 
# value is generated and then hashed together with the password. The salt is then 
# stored alongside the hashed output.

# Pepper: A pepper can be thought of as a type of salt, but it is not stored 
# alongside the hashed output. Instead, it is kept secret, often hard-coded within 
# the application code. The pepper is added to the password (or password and salt 
# combination) and the result is then hashed.