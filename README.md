# Python Security Library (PSL)
This Python library should help you getting your privacy straight

Author: Matthias Konrath

Email:  office@inet-sec.at

# Included Encryption Methods
Symmetric ciphers:
AES, Blowfish, CAST, DES, 3DES, RC2, RC4, AES - Blowfish - 3DES

Asymmetric ciphers:
RSA

Extra encryption:
The library has also classes for socket encryption with Diffie Hellman, AES and RSA

# Encryption Classes
Symmetric encryption classes:
AES, Blowfish, CAST, DES, 3DES, RC2, RC4, AES - Blowfish - 3DES

All this classes have the same methods:
encrypt and decrypt

Asymmetric ciphers:
RSA

This class has the following methods:

generate_new_key, import_key, store_key, store_key_encrypted, store_public_key, encrypt, decrypt, encrypt_aes, decrypt_aes, encrypt_file, decrypt_file, sign, verify, sign_file, verify_file, show_private_key, show_public_key

# Socket Encryption Classes
socket_encryption_dh_aes, socket_encryption_rsa_aes, socket_encryption_authentication_rsa_aes, socket_encryption_authentication_rsa_aes_dh, 
