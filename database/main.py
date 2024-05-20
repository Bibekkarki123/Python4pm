import sqlite3

connection = sqlite3.connect('database/sms.sqlite3')

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR(100),
               phone VARCHAR(100),
               address VARCHAR(100)
)
""")
connection.commit()


def add_student(name,phone,address):
               cursor.execute("""
               INSERT INTO students(name,phone,address) 
               VALUES(?,?,?) """,(name,phone,address))
               connection.commit()


# name = input('Enter Name: ')
# phone = input('Enter Phone Number: ')
# address = input('Enter Address: ')

# add_student(name,phone,address)


# def show():
#         cursor.execute("""
#         SELECT *FROM students
#         """)
#         # print(cursor.fetchall())
#         # print(cursor.fetchone())
#         print(cursor.fetchmany(3))
        
# show()


# def delete(id):
#         cursor.execute("""
#         DELETE FROM students WHERE id=?
#         """,(id,))
#         connection.commit()

# delete(1)

def update(id,name,phone,address):
        cursor.execute("""
        UPDATE students SET name=?, phone=?, address=? WHERE id=?
        """,(name,phone,address,id))
        connection.commit()

update(2,'John','123456789','Nairobi')


