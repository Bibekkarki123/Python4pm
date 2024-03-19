users = {
        'username': "Bibekkarki123",
        'password': "Karki123"
    }
username = input("Enter username:\n")
password = input("Enter password:\n")

if users['username'] == username and users['password'] == password:
        print("Welcome to dashboard")
else:
        print("Invalid username or password")
        