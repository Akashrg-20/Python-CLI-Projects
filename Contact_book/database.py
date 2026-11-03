import sqlite3

conn=sqlite3.connect("Contact_book/contacts.db")
cursor=conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS CONTACTS
    (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    PHONE TEXT UNIQUE NOT NULL
    )

""")
conn.commit()

