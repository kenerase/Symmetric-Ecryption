from cryptography.fernet import Fernet 
import os 

# def generate_key():
# 	key = Fernet.generate_key()
# 	file = open('key.key', 'wb')
# 	file.write(key)
# 	file.close()

file = open('key.key', 'rb')
key = file.read()
file.close()


path = input('Enter Name Folder: ')
def asking():
	enc_dec = input('What You Want To Do?: [1] - encrypt, [2] - decrypt: ')
	if enc_dec == '1':
		encrypt()
	elif enc_dec == '2':
		decrypt()


def encrypt():
	f = Fernet(key)
	names = os.listdir(path)
	for name in names:
		fullname = os.path.join(path, name)
		if os.path.isfile(fullname):
			with open(fullname, 'rb') as file:
				file_data = file.read()
			encrypted_data = f.encrypt(file_data)	
			with open(fullname, 'wb') as file:
				file.write(encrypted_data)

def decrypt():
	f = Fernet(key)
	names = os.listdir(path)
	for name in names:
		fullname = os.path.join(path, name)
		if os.path.isfile(fullname):
			with open(fullname, 'rb') as file:
				data = file.read()
			decrypted_data = f.decrypt(data)
			with open(fullname, 'wb') as file:
				file.write(decrypted_data)


asking()