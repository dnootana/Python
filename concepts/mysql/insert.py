#!/usr/bin/env python3.8

import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "medpac",
	database = "PythonTest"
	)
mycursor = mydb.cursor()

mycursor.execute("INSERT INTO Customers (name, address) VALUES('D Nootana', 'Bhatkal')")
mydb.commit()

mycursor.execute("SELECT ID, name, address FROM Customers")
myresult = mycursor.fetchall()

for x in myresult:
	print(x)

sql = "INSERT INTO Customers (name, address) VALUES(%s, %s)"
val = ('Gagan', 'Kolkata')

mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted")

print("last inserted ID:", mycursor.lastrowid)

sql = "INSERT INTO Customers (name, address) VALUES(%s, %s)"
val = [('Sandhya', 'Banglore'), ('greeshma', 'Mandya'), ('Sujatha', 'Karwar')]

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted")
print("last inserted ID:", mycursor.lastrowid)

mycursor.execute("SELECT ID, name, address FROM Customers")
myresult = mycursor.fetchall()

for x in myresult:
	print(x)

