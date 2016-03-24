# Title:	Python Crypto Library
# Author:	Matthias Konrath
# Email:	office@inet-sec.at

# Import the libary
# This is because the library is in another directory
import sys
sys.path.insert(0, '../../')
# This is used normaly
from psl import *

# Key filenames
server_public_key = "server_rsa_public.key"
server_rsa_key = "server_rsa.key"



"""
RSA KEY GENERATION
"""
# Create RSA object
rsa_obj = RSA_ENC()
# Generate RSA key with 2048 bit keylength
rsa_obj.generate_new_key(2048)
# Store RSA key (unencrypted) (stores the private key)
rsa_obj.store_key(server_rsa_key)
# Export the public key
rsa_obj.store_public_key(server_public_key)



"""
RSA ENCRYPTION
"""
cleartext = "Hallo Welt!"
# Encryption with public key
ciphertext = rsa_obj.encrypt(cleartext)
# Decryption with private key
deccrypted_text = rsa_obj.decrypt(ciphertext)
# Check the message
if cleartext == deccrypted_text:
    print "Encryption and decryption was successful!"
else:
    print "Encryption and decryption FAILED!"



"""
RSA SIGNING
"""
message = "Hallo Welt!"
# Signing the text message with the private key
signature = rsa_obj.sign(message)
# Checking the signed message with the public key
if rsa_obj.verify(signature, message):
    print "Signing was successful!"
else:
    print "Signing FAILED!"
