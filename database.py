import sqlite3

# conn = sqlite3.connect(':memory:')
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

# Commit our command
conn.commit()

# Close our connection
conn.close()


