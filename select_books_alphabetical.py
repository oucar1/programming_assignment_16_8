import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Query to select title column alphabetically
cursor.execute('SELECT title FROM books ORDER BY title ASC')
rows = cursor.fetchall()

# Print the results
print("Titles in alphabetical order:")
for row in rows:
    print(row[0])

# Close the connection
conn.close()
