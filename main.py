import os
import shutil
from cryptography.fernet import Fernet


def Cipher(Password) :

	key = Fernet.generate_key()

	refKey = Fernet(key)
	mypwdbyt = bytes(Password, 'utf-8')

	encryptedPWD = refKey.encrypt(mypwdbyt)
	entry = key.decode() + ',' + encryptedPWD.decode()
	return entry


def Entry(Account,Data):
	file = open('Key_Password_Info.txt', 'a')
	file.write(Data)
	file.write('\n')

	file2 = open('Account_Info.txt', 'a')
	file2.write(Account)
	file2.write('\n')

	
	print('\nEntered data has been successfully recorded..!!!\n')

	file.close()


def Extract():
	acc, En_Pwd, keys = [],[],[]

	# Accounts
	file3 = open('Account_Info.txt', 'r')
	acc = file3.readlines()

	if(len(acc) == 0):
		print("Empty Dataset\n")
	else:
		print("\nPresent Accounts : ")
		for i in range(len(acc)):
			print(i+1,'.',acc[i].rstrip('\n'))
		file3.close()

	
		# Encrypted Passwords and Keys
		file1 = open('Key_Password_Info.txt', 'r')
		info = file1.readlines()
		for i in info:
			data = i.split(',')
			keys.append(bytes(data[0], 'utf-8'))
			En_Pwd.append(bytes(data[1], 'utf-8'))
		file1.close()	


		Op_no = int(input('\nEnter the Option Number : '))
		# Decrypt
		keytouse = Fernet(keys[Op_no-1])
		encryptedPWD = En_Pwd[Op_no-1]

		Deciphered_Pwd = (keytouse.decrypt(encryptedPWD))

		print("\nThe Password is : ",Deciphered_Pwd.decode())



def delete_rec():
	Records, acc = [],[]

	# Encrypted Passwords and Keys
	file1 = open('Key_Password_Info.txt', 'r')
	info = file1.readlines()
	for i in info:
		Records.append(i)
	file1.close()	

	# Account
	file3 = open('Account_Info.txt', 'r')
	info = file3.readlines()
	for i in range(len(info)):
		acc.append(info[i])
		print(i+1,'.',info[i].rstrip('\n'))
	file3.close()

	Op_no = int(input('\nEnter the Option Number : '))

	file4 = open('Key_Password_Info.txt', 'w')
	for i in range(len(Records)):
		if i != (Op_no-1):
			file4.write(Records[i])

	file4.close()

	file5 = open('Account_info.txt', 'w')
	for i in range(len(acc)):
		if i != (Op_no-1):
			file5.write(acc[i])

	file5.close()



	print("\nYour Record has been sucessfully deleted!!")



def Update_Rec():
	Records, acc = [],[]

	# Encrypted Passwords and Keys
	file1 = open('Key_Password_Info.txt', 'r')
	info = file1.readlines()
	for i in info:
		Records.append(i)
	file1.close()	

	# Account
	file3 = open('Account_Info.txt', 'r')
	info = file3.readlines()
	for i in range(len(info)):
		acc.append(info[i])
		print(i+1,'.',info[i].rstrip('\n'))
	file3.close()
	
	Op_no = int(input('\nEnter the Option Number : '))

	# Update Key
	file4 = open('Key_Password_Info.txt', 'w')
	for i in range(len(Records)):
		if i == (Op_no-1) :
			New_Pwd = input("\nEnter the new Password : ")
			file4.write(Cipher(New_Pwd))
		else :
			file4.write(Records[i])

	file4.close()

	print("\nYour password has been successfully updated!!")

	

while True:
	print('1 to Entry.')
	print('2 to Extract. ')
	print('3 to Update.')
	print('4 to Delete.')
	print('0 to Exit.')

	n = int(input('\nEnter: '))

	if n == 1:
		a = int(input('\nNumber of Accounts : '))
		for i in range(0,a):
			Acc = input('\nEnter the Account : ')
			Pwd = input('Enter the Password : ')

			Entry(Acc,Cipher(Pwd))
		print("\n")

	elif n == 2:
		Extract()
		print("\n")
	elif n == 3:
		print("Present Accounts : ")
		Update_Rec()


	elif n == 4:
		print("\nPresent Dataset : ")
		delete_rec()
		print("\n")

	elif n == 0:
		
		exit()

	else:
		print("\nNo such option exists!! ")


