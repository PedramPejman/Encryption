####NO LONGER BEING USED. REFER TO ENCRYPT.PY FOR NEWER IMPLEMENTATION

from Crypto.Cipher import AES
import base64
import os

def inputFile(input_file):
  fp = open(input_file,'r')
  contents = []
  for l in fp:
    contents.append(l)
  fp.close()
  text = str(contents)
  print(text)
  (key, encoded) = encryption(text)
  decryption(key, encoded)

def encryption(privateInfo):
  BLOCK_SIZE = 16
  PADDING = '{'
  pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
  EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
  secret = os.urandom(BLOCK_SIZE)
  print ('encryption key:',secret)
  cipher = AES.new(secret)
  encoded = EncodeAES(cipher, privateInfo)
  print ('Encrypted string:', encoded)
  return (secret, encoded)
  
def decryption(key, encryptedString):
  PADDING = '{'
  DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
  encryption = encryptedString
  cipher = AES.new(key)
  decoded = DecodeAES(cipher, encryption)
  print(decoded)
 
if __name__ == "__main__": inputFile("input.txt")  
