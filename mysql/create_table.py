#!/usr/bin/env python3.8

import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "medpac",
	database = "PythonTest"
	)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS Customers (ID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255) )")

mycursor.execute("SHOW TABLES")

for x in mycursor:
	print(x)

mycursor.execute("ALTER TABLE Customers DROP COLUMN ID")
mycursor.execute("ALTER TABLE Customers ADD COLUMN ID INT AUTO_INCREMENT PRIMARY KEY")

mycursor.execute("DESCRIBE Customers") # same as mycursor.execute("SHOW COLUMNS FROM Customers")
for x in mycursor:
	print(x)

mycursor.execute("show create table Customers") # schema of a table
for x in mycursor:
	print(x)