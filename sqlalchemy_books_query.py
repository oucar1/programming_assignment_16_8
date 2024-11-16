from sqlalchemy import create_engine, MetaData, Table

# Connect to the SQLite database
engine = create_engine('sqlite:///books.db')
metadata = MetaData()
metadata.reflect(bind=engine)

# Reflect the books table
books_table = Table('books', metadata, autoload_with=engine)

# Query the title column in alphabetical order
with engine.connect() as conn:
    result = conn.execute(books_table.select().order_by(books_table.c.title))
    print("Titles in alphabetical order:")
    for row in result:
        print(row.title)
