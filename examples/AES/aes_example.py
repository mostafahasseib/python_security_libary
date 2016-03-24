# Title:	Python Crypto Library
# Author:	Matthias Konrath
# Email:	office@inet-sec.at

# Import the libary
# This is because the library is in another directory
import sys
sys.path.insert(0, '../../')
# This is used normaly
from psl import *


message = "Hallo Welt!"
# Create encryption object
aes_object = AESCipher("Test password!")
# Encrypt the message
ciphertext = aes_object.encrypt(message)
# Decrypt the message
cleartext = aes_object.decrypt(ciphertext)

# Check the message
if cleartext == message:
    print "Message is  the same!"
else:
    print "Message is not the same!"
