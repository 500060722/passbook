import cx_Oracle
con = cx_Oracle.connect('SYSTEM/user1@localhost/xe')
cur = con.cursor()
try:
<<<<<<< HEAD
    cur.execute(""" CREATE TABLE Passbook(Pass_No Number(5) PRIMARY KEY,Account_No Number(10),Present_Date Varchar2(20),Avail_Balance Number(20),FOREIGN KEY(Account_No) REFERENCES Accounts(Account_No))""")
    cur.executemany(""" INSERT INTO Passbook VALUES(:1,:2,:3,:4)""",[(counter,'1712171052','22-May-2018','5000000'),(counter+1,'1712171051','07-Jan-2018','2000000'),(counter+2,'1712171054','27-Nov-2018','10000000'),(counter+3,'1712171053','12-Aug-2018','4000000')])
    cur.execute(""" CREATE TABLE  Passbook1(Account_No Number(5),Transaction_Date varchar2(20),Debit_Amount Number(20),FOREIGN KEY(Account_No) REFERENCES Accounts(Account_No))""")
    cur.executemany(""" INSERT INTO  Passbook1 VALUES(:1,:2,:3)""",[('17121','12-Aug-2015','2000000'),('17122','27-Nov-2016','500000'),('17123','06-Oct-2014','9000000'),('17123','23-Jun-2014','2000000')])
    cur.execute(""" CREATE TABLE  Passbook2(Account_No Number(5),Date_of_Transaction varchar2(20),Credit_Amount Number(20),FOREIGN KEY(Account_No) REFERENCES Accounts(Account_No))""")
    cur.executemany(""" INSERT INTO Passbook2 VALUES(:1,:2,:3)""",[('17121','12-Aug-2012','500000'),('17122','27-Nov-2012','47000'),('17123','06-Oct-2012','90000'),('17123','23-Jun-2012','200000')])
=======
    cur.execute(""" CREATE TABLE Passbook(Account_No Number(10),Present_Date Varchar2(20),Avail_Balance Number(20),FOREIGN KEY(Account_No) REFERENCES Accounts(Account_No))""")
    cur.executemany(""" INSERT INTO Passbook VALUES(:1,:2,:3)""",[('1712171052','22-May-2018','5000000'),('1712171051','07-Jan-2018','2000000'),('1712171054','27-Nov-2018','10000000'),('1712171053','12-Aug-2018','4000000')])
    cur.execute(""" CREATE TABLE  Passbook1(Account_No Number(10),Transaction_Date varchar2(20),Debit_Amount Number(20),FOREIGN KEY(Account_No) REFERENCES Accounts(Account_No))""")
    cur.executemany(""" INSERT INTO  Passbook1 VALUES(:1,:2,:3)""",[('1712171052','12-Aug-2015','2000000'),('1712171051','27-Nov-2016','500000'),('1712171053','06-Oct-2014','9000000'),('1712171054','23-Jun-2014','2000000')])
    cur.execute(""" CREATE TABLE  Passbook2(Account_No Number(10),Date_of_Transaction varchar2(20),Credit_Amount Number(20),FOREIGN KEY(Account_No) REFERENCES Accounts(Account_No))""")
    cur.executemany(""" INSERT INTO Passbook2 VALUES(:1,:2,:3)""",[('1712171052','12-Aug-2012','500000'),('1712171051','27-Nov-2012','47000'),('1712171053','06-Oct-2012','90000'),('1712171054','23-Jun-2012','200000')])
>>>>>>> e05d6a86f241aadc86084831e136bf5f1918def7(Commit by other user (MERGING DONE))
    con.commit()
except cx_Oracle.DatabaseError as e:
    print("error",e)
finally:
    con.close()
