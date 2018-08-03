import cx_Oracle
import time
import datetime
def debit(pin):
	con=cx_Oracle.connect("SYSTEM/user1@localhost/xe")
	cur=con.cursor()
	cur.execute("SELECT Balance,Account_no from Accounts where PIN = :pass",{'pass':pin})#Query#
	for line in cur:
		balance=line[0]
		account_no=line[1]
	now = datetime.datetime.now()
	a=(now.strftime("%Y-%m-%d"))
	#please fetch the current balance from the accounts table and store it in the variable named balance
	print("Your current account balance is ",balance)
	debit_amount = int(input("Enter the debit amount"))
	if (debit_amount<balance):
		updated_balance = balance-debit_amount
		print("Wait we are processing your request......")
		#code starts
		cur.execute("UPDATE Accounts SET Balance = :balanc where PIN = :pn",{'balanc':updated_balance,'pn':pin})#Update the balance in the Accounts table
		cur.execute("INSERT into passbook1 values(:account_no ,:dat ,:debit_amount)",{'account_no':account_no,'dat':a,'debit_amount':debit_amount})#Insert Query#
		#code ends
		con.commit()
		cur.close()
		con.close()
		time.sleep(10)
		print("Done")
		print("Your now updated balance is ",updated_balance)
	else:
		print("Your balance is insufficient to complte the transcation.\n")
	
def credit(pin):
	con=cx_Oracle.connect("SYSTEM/user1@localhost/xe")
	cur=con.cursor()
	cur.execute("SELECT Balance,Account_no from Accounts where PIN = :pass",{'pass':pin})
	for line in cur:
		balance=line[0]
		account_no=line[1]
	now = datetime.datetime.now()
	a=(now.strftime("%Y-%m-%d"))
	#please fetch the current balance from the accounts table and store it in the variable named balance
	print("Your current account balance is ",balance)
	credit_amount = int(input("Enter the amount to be credited in the account"))
	credit_balance=balance+credit_amount
	print("Wait we are processing your request......")
	#code starts
	cur.execute("UPDATE Accounts SET Balance = :balance where PIN = :pin",{'balance':credit_balance,'pin':pin})#Update the balance in the Accounts table
	cur.execute("INSERT into passbook2 values(:account_no ,:dat ,:credit_amount)",{'account_no':account_no,'dat':a,'credit_amount':credit_amount})
	#code ends
	con.commit()
	cur.close()
	con.close()
	time.sleep(10)
	print("Done")
	print("Your updated balance is ",credit_balance)

def passbook(pin):
    con=cx_Oracle.connect("SYSTEM/user1@localhost/xe")
    cur=con.cursor()
    cus=con.cursor()
    cut=con.cursor()
    cud=con.cursor()
    cur.execute("SELECT Account_no from Accounts where PIN = :pass",{'pass':pin})
    for line in cur:
            account_no=line[0]
    cut.execute("select name,date_of_birth,opening_date,type_of_account,balance from accounts where account_no= :b",{'b':account_no})#Query#
    cud.execute("select balance from accounts where account_no=:b",{'b':account_no})
    print("Account Details")
    for line in cut:
        print(line)
    print("debit details")
	#cur.execute("select transaction_date,debit_amount from passbook1 where account_no=:b union select date_of_transaction,credit_amount from passbook2 where account_no=:c",{'b':account_no ,'c':account_no})
    cur.execute("select transaction_date,debit_amount from passbook1 where account_no=:c",{'c':account_no})
    for line in cur:
        print(line)
    print("credit details")
    cus.execute("select date_of_transaction,credit_amount from passbook2 where account_no=:c",{'c':account_no})
    for line in cus:
        print(line)
	
	#Use the SELECT query and join operation if applicable or print both tables(passbook1 and passbook2)
    con.commit()
    cur.close()
    con.close()
	
def identification():
	con=cx_Oracle.connect("SYSTEM/user1@localhost/xe")
	cur=con.cursor()
	print("Hello Sir, Welcome to ABC bank. Here you can debit credit the amount and also you could see the list of last transaction you made.")
	print("So please enter acoount number and it's pin to proceed.")
	accno=int(input("ACCOUNT NUMBER: "))
	pin=int(input("PIN: "))
    
	try:
		cur.execute("select * from ACCOUNTS where PIN =:pin and ACCOUNT_NO=:accno",{'pin':pin,'accno':accno})
		for line in cur:
				account_no=line[0]
		print("So your account no is :",account_no)
		print("So please select the following:\n1>DEBIT THE AMOUNT\n2>CREDIT (DEPOSIT) THE AMOUNT\n3>PASSBOOOK PRINTING")
		i=int(input("Enter your choice: "))
		if (i==1):
			debit(pin)
			passbook(pin)
		if (i==2):
			credit(pin)
			passbook(pin)
		if (i==3):
			passbook(pin)
		if (i>3):
			print("Wrong choice....")
	except cx_Oracle.DatabaseError as e:
		print(e)
		print("Logon denied....Please Check your pin or account number.")
	
identification()
