import sqlite3


# Function to create database
def connect_db():
    conn = sqlite3.connect('bookdatabase.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

# Function to insert books 
def insert_data(title, author, year,isbn):
    conn = sqlite3.connect('bookdatabase.db')
    cur  = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL, ?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()
# Function to view books
def view_data():
    conn = sqlite3.connect('bookdatabase.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows
# Function to search books
def search_data(title="", author="", year="", isbn=""):
    conn = sqlite3.connect('bookdatabase.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows
# Function to delete books
def delete_data(id):
    conn = sqlite3.connect('bookdatabase.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()
# Function to update books
def update_data(id,title,author,year,isbn):
    conn = sqlite3.connect('bookdatabase.db')
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()


# connect_db()
# insert_data("The Right Stuff", 'Tom Wolfe', 1989, 8521479)
# update_data(3,"Right Stuff","Tom Wolfe",1991,8521479)
# delete_data(4)
# print(view_data())
# print(search_data(author='Tom Wolfe'))