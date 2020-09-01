import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abijith123",
  database="mydatabase"
)
mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM customers where id = 1") # where clause
# mycursor.execute(sql)

# sql = "SELECT * FROM customers WHERE address = %s" # using the variable
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr) # attaching the varaible

# sql = "SELECT * FROM customers ORDER BY name desc" # order by command

sql = "SELECT * FROM customers"

# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'" # Update

# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2") # limit function

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

# mydb.commit() # to add the data

# print(mycursor.rowcount, "record(s) affected") # to get the rows affected


myresult = mycursor.fetchall()

print(myresult)