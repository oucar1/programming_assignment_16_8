import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Create the books table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        title TEXT,
        author TEXT,
        year INTEGER
    )
''')

# Save changes and close the connection
conn.commit()
conn.close()

print("Database 'books.db' and table 'books' created successfully.")
