import cx_Oracle
con = cx_Oracle.connect('SYSTEM/user123@localhost/xe')
cur = con.cursor()
counter=1712171051
try:
    cur.execute(""" CREATE TABLE Accounts(Account_No Number(10) PRIMARY KEY ,Name Varchar2(30) NOT NULL,Date_of_Birth Varchar2(20) NOT NULL,Opening_Date Varchar2(20),Type_of_Account varchar2(20) CHECK (Type_of_Account IN('Savings','Current')),PIN NUMBER(4) NOT NULL UNIQUE,Balance NUMBER(20))""")
    cur.executemany(""" INSERT INTO Accounts VALUES(:1,:2,:3,:4,:5,:6)""",[(counter,'Sajal','27-nov-1998','10-oct-2010','Savings','3639','2000'),(counter+1,'Prakhar','20-May-1999','12-Dec-2011','Current','2428','2000'),(counter+2,'Prajawal','24-May-1999','07-Nov-2009','Current','1415','2000'),(counter+3,'Ishaan','13-Jan-1999','24-Jun-2007','Savings','1234','2000')])
    con.commit()
except cx_Oracle.DatabaseError as e:
    print("error",e)
finally:
    con.close()
    
