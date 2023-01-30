import sqlite3

#Open database
conn = sqlite3.connect('database.db')

#Create admin table


conn.execute('''CREATE TABLE admin 
		(userId INTEGER PRIMARY KEY, 
		password TEXT,
		email TEXT,
		firstName TEXT,
		lastName TEXT,
		address1 TEXT,
		address2 TEXT,
		zipcode TEXT,
		city TEXT,
		state TEXT,
		country TEXT, 
		phone TEXT
		)''')