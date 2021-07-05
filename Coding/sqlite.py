import sqlite3

# Function to create Table 
def create_table():
    dbconnection = sqlite3.connect('lite.db')
    dbcursor = dbconnection.cursor()
    dbcursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    dbconnection.commit()
    dbconnection.close()

# Function to insert data
def insert_data(item, quantity, price):
    dbconnection = sqlite3.connect('lite.db')
    dbcursor = dbconnection.cursor()
    dbcursor.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    dbconnection.commit()
    dbconnection.close()

# Function to retrieve data
def view_data():
    dbconnection = sqlite3.connect('lite.db')
    dbcursor = dbconnection.cursor()
    dbcursor.execute("SELECT * FROM store")
    rows = dbcursor.fetchall()
    dbcursor.close()
    return rows
# Function to update data
def update_data(quantity, price,item):
    dbconnection = sqlite3.connect('lite.db')
    dbcursor = dbconnection.cursor()
    dbcursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    dbconnection.commit()
    dbconnection.close()
#  Function to delete data
def delete_data(item):
    dbconnection = sqlite3.connect('lite.db')
    dbcursor = dbconnection.cursor()
    dbcursor.execute("DELETE FROM store WHERE item=?", (item,))
    dbconnection.commit()
    dbconnection.close()


# insert_data('T-shirt', 10, 1500.0)
# delete_data("T-shirt")
update_data(10, 80.0, 'Jeans')
print(view_data())

