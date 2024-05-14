import sqlite3

# Establishing a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

#query all data
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
print(cursor.fetchall())

#queru certain data
cursor.execute("SELECT band, date FROM events WHERE date='2088.10.15'")
print(cursor.fetchall())

# insert new rows
new_rows = [('cats', 'cats city', '2088.10.16'),
            ('hens', 'hen city', '2088.10.17')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()