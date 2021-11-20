#!/usr/bin/env python3.8

import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "medpac"
	)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE PythonTest")

mycursor.execute("SHOW DATABASES")

for i in mycursor:
	print(i)

mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "medpac",
	database = "PythonTest"
	)