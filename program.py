import cx_Oracle
import time
def debit():
	con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
	cur=con.cursor()
	cur.execute("")#Query#
	#please fetch the current balance from the accounts table and store it in the variable named balance
	print("Your current account balance is ",balance)
	debit_amount = int(input("Enter the debit amount"))
	updated_balance = balance-debit_amount
	print("Wait we are processing your request......")
	#code starts
	cur.execute("")#Update the balance in the Accounts table
	cur.execute("")#Insert pass_no(or to keep it simple use only account no. as a foriegn key no need of pass_no.),debit_amount,date(take any date) and debit amount
	#code ends
	con.commit()
	cur.close()
	con.close()
	time.sleep(10)
	print("Done")
	print("Your now updated balance is ",updated_balance)
	
def credit():
	con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
	cur=con.cursor()
	cur.execute("")#Query#
	#please fetch the current balance from the accounts table and store it in the variable named balance
	print("Your current account balance is ",balance)
	credit_amount = int(input("Enter the amount to be credited in the account"))
	credit_balance=balance+credit_amount
	print("Wait we are processing your request......")
	#code starts
	cur.execute("")#Update the balance in the Accounts table
	cur.execute("")#Insert pass_no(or to keep it simple use only account no. as a foriegn key no need of pass_no.),debit_amount,date(take any date) and debit amount
	#code ends
	con.commit()
	cur.close()
	con.close()
	time.sleep(10)
	print("Done")
	print("Your updated balance is ",credit_balance)

def passbook():
	con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
	cur=con.cursor()
	cur.execute("")#Query#
	print("Your transactions is as follows: ")
	#Use the SELECT query and join operation if applicable or print both tables(passbook1 and passbook2)
	for line in cur:
		print(line)
	con.commit()
	cur.close()
	con.close()
	
def identification():
	con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
	cur=con.cursor()
	print("Hello Sir, Welcome to ABC bank. Here you can debit credit the amount and also you could see the list of last transaction you made.")
	print("So please enter pin to proceed.")
	pin=int(input("PIN: "))
	try:
		cur.execute("select ACCOUNTNO from ACCOUNTS where PIN =:pin",{'pin':pin})
		for line in cur:
				account_no=line[0]
		print("So your account no is :",account_no)
		print("So please select the following:\n1>DEBIT THE AMOUNT\n2>CREDIT (DEPOSIT) THE AMOUNT\n3>PASSBOOOK PRINTING")
		i=int(input("Enter your choice: "))
		if (i==1):
			debit()
		if (i==2):
			credit()
		if (i==3):
			passbook()
		if (i>3):
			print("Wrong choice....")
	except cx_Oracle.DatabaseError as e:
		print(e)
		print("Logon denied....Please Check your pin.")
	
identification()
