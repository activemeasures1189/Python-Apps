import psycopg2


# Function to create Table 
def create_table():
    dbconnection = psycopg2.connect("dbname='trialdb' user='postgres' password='australia2008' host='localhost' port='5432'")
    dbcursor = dbconnection.cursor()
    dbcursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    dbconnection.commit()
    dbconnection.close()

# Function to insert data
def insert_data(item, quantity, price):
    dbconnection = psycopg2.connect("dbname='trialdb' user='postgres' password='australia2008' host='localhost' port='5432'")
    dbcursor = dbconnection.cursor()
    dbcursor.execute("INSERT INTO store VALUES (%s, %s, %s)",(item, quantity, price))
    dbconnection.commit()
    dbconnection.close()

# Function to retrieve data
def view_data():
    dbconnection = psycopg2.connect("dbname='trialdb' user='postgres' password='australia2008' host='localhost' port='5432'")
    dbcursor = dbconnection.cursor()
    dbcursor.execute("SELECT * FROM store")
    rows = dbcursor.fetchall()
    dbcursor.close()
    return rows
# Function to update data
def update_data(quantity, price,item):
    dbconnection = psycopg2.connect("dbname='trialdb' user='postgres' password='australia2008' host='localhost' port='5432'")
    dbcursor = dbconnection.cursor()
    dbcursor.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    dbconnection.commit()
    dbconnection.close()
#  Function to delete data
def delete_data(item):
    dbconnection = psycopg2.connect("dbname='trialdb' user='postgres' password='australia2008' host='localhost' port='5432'")
    dbcursor = dbconnection.cursor()
    dbcursor.execute("DELETE FROM store WHERE item=%s", (item,))
    dbconnection.commit()
    dbconnection.close()

# create_table()
# insert_data('Jeans', 2, 70.0)
delete_data('Scarfs')
print(view_data())