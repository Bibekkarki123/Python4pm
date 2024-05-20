users = {
        'username': "Bibekkarki123",
        'password': "Karki123"
    }
username = input("Enter username: ")
password = input("Enter password: ")

if users['username'] == username and users['password'] == password:
        print("Welcome to Dashboard")
else:
        print("Invalid username or password")
        