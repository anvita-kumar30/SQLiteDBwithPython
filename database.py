import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Create a table
# c.execute("""CREATE TABLE customers (
# 	first_name text,
# 	last_name text,
# 	email text
# 	)""")

# c.execute("CREATE TABLE customers (first_name DATATYPE, last_name DATATYPE, email DATATYPE)")

# Datatypes:- NULL, INTEGER, REAL, TEXT, BLOB

# Insert into table
# c.execute("INSERT INTO customers VALUES ('Anvita', 'Kumar', 'anvita@gmail.com')")
# c.execute("INSERT INTO customers VALUES ('Sam', 'Sparks', 'sam@gmail.com')")
# c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@gmail.com')")

# many_customers = [('Wes', 'Brown', 'wes@gmail.com'), ('Steph', 'Kuewa', 'steph@gmail.com'), ('Dan', 'Pas', 'dan@gmail.com')]
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# print("Command executed successfully...")

# Query the DB
# c.execute("SELECT * FROM customers")
# print(c.fetchone())
# print(c.fetchone()[0])
# print(c.fetchmany(3))
# print(c.fetchall())

# items = c.fetchall()
# print(items)

# for item in items:
# 	print(item)
# for item in items:
# 	print(item[0])

# print("NAME" + "\t\tEMAIL")
# print("-----" + "\t\t--------")
# for item in items:
# 	print(item[0] + " " + item[1] + "\t" + item[2])

# c.execute("SELECT rowid, * FROM customers")
# items = c.fetchall()

# for item in items:
# 	print(item)

# c.execute("SELECT * FROM customers WHERE last_name = 'Sparks'")
# items = c.fetchall()

# for item in items:
# 	print(item)

# c.execute("SELECT * FROM customers WHERE age >= 21")

# c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'")
# items = c.fetchall()

# for item in items:
# 	print(item)

# c.execute("SELECT * FROM customers WHERE email LIKE '%gmail.com'")
# items = c.fetchall()

# for item in items:
# 	print(item)

# Update records

# c.execute("""UPDATE customers SET first_name = 'Bob' WHERE last_name = 'Pas'
# 	""")
# conn.commit()
# c.execute("SELECT * FROM customers")
# items = c.fetchall()
# for item in items:
# 	print(item)

# c.execute("""UPDATE customers SET first_name = 'Marty' WHERE last_name = 'Brown'
#  	""")
# conn.commit()
# c.execute("SELECT * FROM customers")
# items = c.fetchall()
# for item in items:
# 	print(item)

# c.execute("""UPDATE customers SET first_name = 'Mary' WHERE rowid = 3
#  	""")
# conn.commit()
# c.execute("SELECT * FROM customers")
# items = c.fetchall()
# for item in items:
# 	print(item)

# c.execute("""UPDATE customers SET first_name = 'Wes' WHERE rowid = 4
#  	""")
# conn.commit()
# c.execute("SELECT * FROM customers")
# items = c.fetchall()
# for item in items:
# 	print(item)

# c.execute("""UPDATE customers SET email = 'mary@gmail.com' WHERE rowid = 3
#  	""")
# conn.commit()
# c.execute("SELECT * FROM customers")
# items = c.fetchall()
# for item in items:
# 	print(item)

# Use rowid to update

# c.execute("""UPDATE customers SET first_name = 'Bob' WHERE rowid = '6'
# 	""")
# conn.commit()
# c.execute("SELECT rowid, * FROM customers")
# items = c.fetchall()
# for item in items:
# 	print(item)

# Commit our command
conn.commit()

# Close our connection
conn.close()


