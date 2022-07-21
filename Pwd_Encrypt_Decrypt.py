Pwd_Key = 3 #Enter personal Encryption Key


#Encrypt password using Hill Cipher
def Cipher(Account,Password) :
    
    Cipher_Pwd = ''    
    for i in Password:
        a = chr(ord(i) + Pwd_Key )
        Cipher_Pwd += a
    
    T = Account + ',' + Cipher_Pwd + '\n'
    return T


#Entry of encrypted data into storage file
def Entry(Data):
	file = open('Password_Info.txt', 'a')
	file.write(Data)
	
	print('\nEntered data has been successfully recorded..!!!\n')

	file.close()


#Decrypted data extraction from storage file
def Extract():
	Records,En_Pwd = [],[]

	file = open('Password_Info.txt', 'r')
	x = file.readlines()

	for i in x:
		Records.append(i)

	for i in range(len(Records)):
		Fields = Records[i].split(',')
		print((i+1),":",Fields[0])

	for i in range(len(Records)):
		N = Records[i].split(',')
		En_Pwd.append(N[1][0:-1])

	Op_no = int(input('\nEnter the Option Number : '))
	Deciphered_Pwd = ''
	for i in En_Pwd[Op_no-1] :
		Deciphered_Pwd += chr(ord(i) - Pwd_Key )
	print("\nThe Password is : ",Deciphered_Pwd)

	file.close()


#Deleting a Record
def delete_rec():
	Records = []

	file = open('Password_Info.txt', 'r')
	x = file.readlines()

	for i in x:
		Records.append(i)

	for i in range(len(Records)):
		Fields = Records[i].split(',')
		print((i+1),":",Fields[0])

	file.close()

	Op_no = int(input('\nEnter the Option Number : '))

	file_2 = open('Password_Info.txt', 'w')
	for i in range(len(Records)):
		if i != (Op_no-1):
			file_2.write(Records[i])

	file_2.close()

	print("\nYour Record has been sucessfully deleted!!")



def Update_Rec():
	Records = []

	file = open('Password_Info.txt', 'r')
	x = file.readlines()

	for i in x:
		Records.append(i)

	for i in range(len(Records)):
		Fields = Records[i].split(',')
		print((i+1),":",Fields[0])

	file.close()
	Op_no = int(input('\nEnter the Option Number : '))

	file_2 = open('Password_Info.txt', 'w')
	for i in range(len(Records)):
		if i == (Op_no-1) :
			New_Pwd = input("\nEnter the new Password : ")
			file_2.write(Cipher(Records[i].split(',')[0],New_Pwd))
		else :
			file_2.write(Records[i])

	file_2.close()

	print("\nYour password has been successfully updated!!")

	

while True:
	print('1 to Entry.')
	print('2 to Extract. ')
	print('3 to Update.')
	print('4 to Delete.')
	print('0 to Exit.')

	n = int(input('\nEnter: '))

	if n == 1:
		a = int(input('\nNumber of Datasets : '))
		for i in range(0,a):
			Acc = input('\nEnter the Account : ')
			Pwd = input('Enter the Password : ')

			Entry(Cipher(Acc,Pwd))
		print("\n")

	elif n == 2:
		print("\nPresent Dataset : ")
		Extract()
		print("\n")
	elif n == 3:
		print("Present Dataset : ")
		Update_Rec()


	elif n == 4:
		print("\nPresent Dataset : ")
		delete_rec()
		print("\n")

	elif n == 0:
		exit()

	else:
		print("\nNo such option exists!! ")
