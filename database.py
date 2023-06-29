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
# c.execute("INSERT INTO customers VALUES ('Anvita', 'Kumar', 'anvita@gamil.com')")
# c.execute("INSERT INTO customers VALUES ('Sam', 'Sparks', 'sam@gamil.com')")
# c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@gamil.com')")

# many_customers = [('Wes', 'Brown', 'wes@gmail.com'), ('Steph', 'Kuewa', 'steph@gmail.com'), ('Dan', 'Pas', 'dan@gmail.com')]
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
#
# print("Command executed successfully...")

# Commit our command
conn.commit()

# Close our connection
conn.close()


