# Python Server Client
# Author:	Matthias Konrath
# Email:	office@inet-sec.at


# This is because the library is in another directory
import sys
sys.path.insert(0, '../')
# This is used normaly
from psl import *
import time

# Filenames from the needed files
server_public_key = "server_rsa_public.key"
client_public_key = "client_rsa_public.key"
client_rsa_key = "client_rsa.key"



# AES and DH - Encrypted Socket
# Create socket and wait for connection
socket_transfare0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_transfare0.connect(("127.0.0.1", 1111))

# Create encrypted socket object and start key exchange
sock_enc0 = socket_encryption_dh_aes(socket_transfare0)
sock_enc0.client_key_exchange()

# Print debug information
sock_enc0.debug()
# Send data encrypted
sock_enc0.send("Test000")
# Close socket
sock_enc0.close()
# Wait for user to continue
test = raw_input("NEXT?")



# RSA and AES- Encrypted Socket
# Create socket and wait for connection
socket_transfare1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_transfare1.connect(("127.0.0.1", 2221))

# Create encrypted socket object and start key exchange
sock_enc1 = socket_encryption_rsa_aes(socket_transfare1)
sock_enc1.client_key_exchange(server_public_key)

# Print debug information
sock_enc1.debug()
# Send data encrypted
sock_enc1.send("Test000")
# Close socket
sock_enc1.close()
# Wait for user to continue
test = raw_input("NEXT?")



# RSA and AES - Encrypted Socket
# Create socket and wait for connection
socket_transfare2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_transfare2.connect(("127.0.0.1", 3331))

# Create encrypted socket object and start key exchange
sock_enc2 = socket_encryption_authentication_rsa_aes(socket_transfare2)
sock_enc2.client_key_exchange(client_public_key, client_rsa_key, server_public_key)

# Print debug information
sock_enc2.debug()
# Send data encrypted
sock_enc2.send("Test000")
# Close socket
sock_enc2.close()
# Wait for user to continue
test = raw_input("NEXT?")



# RSA, AES, DH - Encrypted Socket
# Create socket and wait for connection
socket_transfare3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_transfare3.connect(("127.0.0.1", 4441))

# Create encrypted socket object and start key exchange
sock_enc3 = socket_encryption_authentication_rsa_aes_dh(socket_transfare3)
sock_enc3.client_key_exchange(client_public_key, client_rsa_key, server_public_key)

# Print debug information
sock_enc3.debug()
# Send data encrypted
sock_enc3.send("Test000")
# Close socket
sock_enc3.close()
