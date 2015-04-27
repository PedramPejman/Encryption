#!/usr/bin/python3

""" 
Calling Convention:
python3 encryption.py encrypt filename
python3 encryption.py decrypt filename key
"""

import sys, base64, os
from Crypto import Random
from Crypto.Cipher import AES

def create_key(length=64):
  return os.urandom(32)

def pad(s):
  return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):
  message = pad(message)
  iv = Random.new().read(AES.block_size)
  cipher = AES.new(key, AES.MODE_CBC, iv)
  return iv + cipher.encrypt(message)

def decrypt(ciphertext, key):
  iv = ciphertext[:AES.block_size]
  cipher = AES.new(key, AES.MODE_CBC, iv)
  plaintext = cipher.decrypt(ciphertext[AES.block_size:])
  return plaintext.rstrip(b"\0")

def encrypt_file(file_name, key):
  with open(file_name, 'rb') as fo:
    plaintext = fo.read()
  enc = encrypt(plaintext, key)
  with open(file_name + ".enc", 'wb') as fo:
    fo.write(enc)

def decrypt_file(file_name, key):
  with open(file_name, 'rb') as fo:
    ciphertext = fo.read()
  dec = decrypt(ciphertext, key)
  with open(file_name[:-4], 'wb') as fo:
    fo.write(dec)

def byte_to_int(byte_key):
  return int.from_bytes(byte_key, byteorder='big')
def int_to_byte(int_key):
  return int_key.to_bytes(32, byteorder='big')

def handle_input():
  if (len(sys.argv) < 3): raise Exception("No verb given")
  action = sys.argv[1]
  filename = sys.argv[2]
  if action == 'encrypt':
    key = create_key()
    encrypt_file(filename, key)    
    digits = byte_to_int(key)
    print(key)
    print(digits)
    print(int_to_byte(digits))

    #decrypt_file("input.txt.enc", key)
  if action == 'decrypt': 
    if (len(sys.argv) < 4): raise Exception("No key given for decryption")
    #key = b'\xa2t\xe0\x1f\x04 \xe3Q\xd0>\x9f\xd3C-\x1f\x95\xa4\xb7F\n\xcb\x9d\n\xd28\xe0\x02m\x9d\xebI)'
    key = sys.argv[3].replace("\\", "")
    #key = key.encode(sys.getfilesystemencoding(), 'surrogateescape')
    key = key.replace("x", "\\x")
    key = b'\x01X\x1b\x99U\xf6\x8f\x03\xec\xc36\xb5\x8c9\x18\xa3\x16\x10\xf1\xccO\\\x99CZ\xde)wZ?6l'
    print(type(key))
    print(len(key))
    print(key)
    decrypt_file(filename, key)


handle_input()


