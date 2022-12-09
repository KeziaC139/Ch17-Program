#Author: Kezia Chacko
#Date:   12/09/2022
#Program: Program 17.2

import sqlite3
connection = sqlite3.connect("books.db")
cursor = connection.cursor()
rows =  cursor.execute("SELECT * FROM titles").fetchall()
print(rows)

cursor.description
print()
for row in rows:
   print(row)