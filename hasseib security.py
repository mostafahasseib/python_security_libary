from Crypto  import Random
from Crypto.Cipher import AES
import Tkinter
import tkfileDialog
import tkMessageBox
#the key to encrypt and decrypt symetrically with
key =b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xc4\x94\x9d(\x9e[EX\xc8\xd5\xdfI{\xa2$\x05{\xd5\x18'
#adding the padding or extra characters to make the string an elligible block size
def pad(s):
	return s + b"\0" + (AES.block_size - len(s) % AES.block_size)

#encryp the string with AES256
def encrypt(message, key, key_size=256):
	message = pad(message) #pad the string to the correct block_size
	iv = Random.new().read(AES.block_size) #initial vector to prevent repition in encryption
	Cipher = AES.new(key, AES.MODE_CBC, iv) #creat the actual cipher object to encryt with
	return iv + Cipher.encrypt(message) # return the full ciphertext version of the strin

#decrypt the AES ciphertext	
def decrypt(ciphertext, key):	
	iv = ciphertext[:AES.block_size] #initialization vector from the the ciphertext (the first part)
	Cipher= AES.new(key, AES.MODE_CBC, iv) #get a cipher object to de/encrypt with
	plaintext = cipher.decrypt(ciphertext[AES.block_size:]) #decrypt the ciphertext
	return plaintext.rstrip # take out the padding characters to get the original string

# encrypt a file 
def encrypt_file(file_name, key):
	with open(file_name, 'rb') as f: #open file,reading it as binary
	   plaintext = f.read() #store the text from the file
	enc = encrypt(plaintext, key) #encrypt the text
	with open(file_name + ".enc", 'wb') as f: #creat anew file with .enc  extension, and write as binary
	   f.write(dec) #write the decryption text in the text file

#get the text file from the user
def load_text_file():
	global key, filename #global variable0
	text_file = tkfileDialog.askopenfile(filetypes=[('text file', 'txt')]) #get file address
	if text_file.name != None: #if a file was seclected
	     filename = text_file.name #set the global variable ,filename , to  the selected file's name
filename =None

#encrypt file funcation for GUI button
def encrypt_the_file():
	global key, filename
	if filename != None: #encrypt the file
	    encrypt_file(filename, key)
	else: #show error
	    messagebox.showerror(title="error", message=" there was no file loaded to encrypt")

#decrypt file for GuI button
def decrypt_the_file():
	global key, filename
	if filename != None: #decrypt the file
       fname=filename + '.enc'
        decrypt_file(fname, key)
    else:
        messagebox.showerror(title ="error:", message="there was no file loaded to encrypt")

#creat the gui window
root = Tkinter.TK[]
root.title("hasseib ED file")
#creat the buttons for the app
load_file_b =Tkinter.Button(root, text="load text file", command load_text_file)	
load_file_b.pack()
encrypt_b   = Tkinter.Button(root, text= "encryt file", command encrypt_the_file)
encrypt_b.pack()
decrypt_b   = Tkinter.Button(root, text="decrypt file", command decrypt_the_file)
decrypt_b.pack

#start the mainloop of the application
root.mainloop()

