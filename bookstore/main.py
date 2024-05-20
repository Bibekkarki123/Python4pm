# import os

# if not os.path.exists('bookstore/books.txt'):
#     fObj = open('bookstore/books.txt','w')
#     fObj.close()

# if not os.path.exists('bookstore/users.txt'):
#     fObj = open('bookstore/users.txt','w')
#     fObj.close()



# def register():
#     username = input("Enter Username: ")
#     username = username.strip() 
#     if username in open('bookstore/users.txt').read():
#         print('Username already exist')
#         exit() 
#     password = input("Enter Password: ")
#     password = password.strip()
#     with open ('bookstore/users.txt','a') as fObj:
#         fObj.write(f'Username:{username},Password:{password}\n')
#         print('Username register sucessfully')
#         exit()

# # register()

# def login():
#     username = input("Enter Username: ")
#     username = username.strip()
#     password = input('Enter Password: ')
#     password = password.strip()
#     with open('bookstore/users.txt') as fObj:
#         users = fObj.readlines()
#     for user in users:
#         if f'Username:{username},Password:{password}\n'== user:
#             print('Login Successfully.')
#             break
#     else:
#         print('Login Failed.')
#         exit()

# login()


