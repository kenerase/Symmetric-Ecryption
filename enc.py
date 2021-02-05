from cryptography.fernet import Fernet 

# def generate_key():
# 	key = Fernet.generate_key()
# 	file = open('key.key', 'wb')
# 	file.write(key)
# 	file.close()


file = open('key.key', 'rb')
key = file.read()
file.close()



filename = input('Enter FileName: ')
def asking():
	enc_dec = input('What You Want To Do?: [1] - encrypt, [2] - decrypt: ')
	if enc_dec == '1':
		encrypt()
	elif enc_dec == '2':
		decrypt()


def encrypt():
	f = Fernet(key)
	with open(filename, 'rb') as file:
		file_data = file.read()
	encrypted_data = f.encrypt(file_data)
	with open(filename, 'wb') as file:
		file.write(encrypted_data)

	
def decrypt():
	f = Fernet(key)
	with open(filename, 'rb') as file:
		file_data = file.read()
	decrypted_data = f.decrypt(file_data)
	with open(filename, 'wb') as file:
		file.write(decrypted_data)

asking()

