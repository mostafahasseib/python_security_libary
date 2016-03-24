# Pyhton Server
# Author:	Matthias Konrath
# Email:	office@inet-sec.at


# This is because the library is in another directory
import sys
sys.path.insert(0, '../../')
# This is used normaly
from psl import *

# Filename of the server rsa private key
server_rsa_key = "server_rsa.key"


# AES and DH - Encrypted Socket
# Create socket and wait for connection
socket_transfare0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_transfare0.bind((socket.gethostname(), 1111))
socket_transfare0.listen(5)
client_sock0, client_addr0 = socket_transfare0.accept()

# Create encrypted socket object and start key exchange
sock_enc0 = socket_encryption_dh_aes(client_sock0)
sock_enc0.server_key_exchange()

# Print debug information
sock_enc0.debug()
# Print recived data
print sock_enc0.recv()
# Close socket
sock_enc0.close()
print "Finish 0"


# RSA and AES- Encrypted Socket
# Create socket and wait for connection
socket_transfare1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_transfare1.bind((socket.gethostname(), 2221))
socket_transfare1.listen(5)
client_sock1, client_addr1 = socket_transfare1.accept()

# Create encrypted socket object and start key exchange
sock_enc1 = socket_encryption_rsa_aes(client_sock1)
sock_enc1.server_key_exchange(server_rsa_key)

# Print debug information
sock_enc1.debug()
# Print recived data
print sock_enc1.recv()
# Close socket
sock_enc1.close()
print "Finish 1"

# RSA and AES - Encrypted Socket
# Create socket and wait for connection
socket_transfare2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_transfare2.bind((socket.gethostname(), 3331))
socket_transfare2.listen(5)
client_sock2, client_addr2 = socket_transfare2.accept()

# Create encrypted socket object and start key exchange
sock_enc2 = socket_encryption_authentication_rsa_aes(client_sock2)
sock_enc2.server_key_exchange(server_rsa_key)

# Print debug information
sock_enc2.debug()
# Print recived data
print sock_enc2.recv()
# Close socket
sock_enc2.close()
print "Finish 2"


# RSA, AES, DH - Encrypted Socket
# Create socket and wait for connection
socket_transfare3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_transfare3.bind((socket.gethostname(), 4441))
socket_transfare3.listen(5)
client_sock3, client_addr3 = socket_transfare3.accept()

# Create encrypted socket object and start key exchange
sock_enc3 = socket_encryption_authentication_rsa_aes_dh(client_sock3)
sock_enc3.server_key_exchange(server_rsa_key)

# Print debug information
sock_enc3.debug()
# Print recived data
print sock_enc3.recv()
# Close socket
sock_enc3.close()
print "Finish 3"
