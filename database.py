import sqlite3

# Connect to DB
conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE customers (
	first_name text,
	last_name text,
	email text
	)""")

# c.execute("CREATE TABLE customers (first_name DATATYPE, last_name DATATYPE, email DATATYPE)")

# Datatypes:- NULL, INTEGER, REAL, TEXT, BLOB

# Insert into table
c.execute("INSERT INTO customers VALUES ('Anvita', 'Kumar', 'anvita@gmail.com')")
c.execute("INSERT INTO customers VALUES ('Sam', 'Sparks', 'sam@gmail.com')")
c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@gmail.com')")

many_customers = [('Wes', 'Brown', 'wes@gmail.com'), ('Steph', 'Kuewa', 'steph@gmail.com'), ('Dan', 'Pas', 'dan@gmail.com')]
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

print("Command executed successfully...")

# Query the DB
c.execute("SELECT * FROM customers")
# print(c.fetchone())
# print(c.fetchone()[0])
# print(c.fetchmany(3))
# print(c.fetchall())

items = c.fetchall()
print(items)

for item in items:
	print(item)
for item in items:
	print(item[0])

print("NAME" + "\t\tEMAIL")
print("-----" + "\t\t--------")
for item in items:
	print(item[0] + " " + item[1] + "\t" + item[2])

c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()

for item in items:
	print(item)

c.execute("SELECT * FROM customers WHERE last_name = 'Sparks'")
items = c.fetchall()

for item in items:
	print(item)

# c.execute("SELECT * FROM customers WHERE age >= 21")

c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'")
items = c.fetchall()

for item in items:
	print(item)

c.execute("SELECT * FROM customers WHERE email LIKE '%gmail.com'")
items = c.fetchall()

for item in items:
	print(item)

# Update records

c.execute("""UPDATE customers SET first_name = 'Bob' WHERE last_name = 'Pas'
	""")
conn.commit()
c.execute("SELECT * FROM customers")
items = c.fetchall()
for item in items:
	print(item)

c.execute("""UPDATE customers SET first_name = 'Marty' WHERE last_name = 'Brown'
 	""")
conn.commit()
c.execute("SELECT * FROM customers")
items = c.fetchall()
for item in items:
	print(item)

c.execute("""UPDATE customers SET first_name = 'Mary' WHERE rowid = 3
 	""")
conn.commit()
c.execute("SELECT * FROM customers")
items = c.fetchall()
for item in items:
	print(item)

c.execute("""UPDATE customers SET first_name = 'Wes' WHERE rowid = 4
 	""")
conn.commit()
c.execute("SELECT * FROM customers")
items = c.fetchall()
for item in items:
	print(item)

c.execute("""UPDATE customers SET email = 'mary@gmail.com' WHERE rowid = 3
 	""")
conn.commit()
c.execute("SELECT * FROM customers")
items = c.fetchall()
for item in items:
	print(item)

# Use rowid to update

c.execute("""UPDATE customers SET first_name = 'Bob' WHERE rowid = '6'
	""")
conn.commit()
c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
for item in items:
	print(item)

# Delete records

c.execute("DELETE from customers WHERE rowid = 6")
conn.commit()
c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
for item in items:
	print(item)

# Query the DB - ORDER BY

c.execute("SELECT rowid, * FROM customers ORDER BY rowid")
items = c.fetchall()
for item in items:
	print(item)

c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
items = c.fetchall()
for item in items:
	print(item)

c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")
items = c.fetchall()
for item in items:
	print(item)

# AND/OR Clause

c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' AND rowid = 3")
items = c.fetchall()
for item in items:
	print(item)

c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 3")
items = c.fetchall()
for item in items:
	print(item)

# Limiting results

c.execute("SELECT rowid, * FROM customers LIMIT 2")
items = c.fetchall()
for item in items:
	print(item)

c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")
items = c.fetchall()
for item in items:
	print(item)

# Drop table

c.execute("DROP TABLE customers")
conn.commit()
c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
for item in items:
	print(item)

# Show All Function (Create the table again and insert the same values)

def show_all():
	# Connect to DB and create cursor
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()

	# Query the DB
	c.execute("SELECT rowid, * FROM customers")
	items = c.fetchall()

	for item in items:
		print(item)

	# Commit our command
	conn.commit()

	# Close our connection
	conn.close()

# Add a new record to the table

def add_one(first,last,email):
	# Connect to DB and create cursor
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()

	# Query the DB
	c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

	# Commit our command
	conn.commit()

	# Close our connection
	conn.close()

# Delete a record from the table

def delete_one(id):
	# Connect to DB and create cursor
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()

	# Query the DB
	c.execute("DELETE from customers WHERE rowid = (?)", id)

	# Commit our command
	conn.commit()

	# Close our connection
	conn.close()

# Add many records to table

def add_many(list):
	# Connect to DB and create cursor
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()

	# Query the DB
	c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

	# Commit our command
	conn.commit()

	# Close our connection
	conn.close()

# Lookup with where

def email_lookup(email):
	# Connect to DB and create cursor
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()

	# Query the DB
	c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
	items = c.fetchall()

	for item in items:
		print(item)

	# Commit our command
	conn.commit()

	# Close our connection
	conn.close()

# Commit our command
conn.commit()

# Close our connection
conn.close()


