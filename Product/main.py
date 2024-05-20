import sqlite3

connection = sqlite3.connect('Product/sms.sqlite3')

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS items(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               product VARCHAR(100),
               quantity VARCHAR(100),
               price VARCHAR(100)
)
""")
connection.commit()

def add_items(product,quantity,price):
    cursor.execute("""
    INSERT INTO items(product,quantity,price)
    VALUES(?,?,?) """,(product,quantity,price))
    connection.commit()
                                  
product = input("Enter Product Name: ")
quantity = input("Enter Quantity: ")
price = input("Enter Price: ")

add_items(product,quantity,price)



def show():
    cursor.execute("""
    SELECT *FROM items
    """)
    # print(cursor.fetchall())
    # print(cursor.fetchone())
    # print(cursor.fetchmany(2))
   
show()


# def delete(id):
#     cursor.execute("""
#     DELETE FROM items WHERE id=?
#     """,(id,))
#     connection.commit()

# delete(4)


# def update(id,product,quantity,price):
#     cursor.execute("""
#     UPDATE items SET product=?, quantity=?, price=? WHERE id=?
#     """,(product,quantity,price,id))
#     connection.commit()

# update(2,'Apple', '2', '200000')

