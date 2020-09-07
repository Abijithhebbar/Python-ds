import sqlite3

mycursor = sqlite3.connect('test.db')

sql = "CREATE TABLE data(id VARCHAR(255),imageurl VARCHAR(255), images VARCHAR(255))"

mycursor.execute(sql)