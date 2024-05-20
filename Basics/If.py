# First Method:
data = [
    ['ram','sita','gita'],
    ['hari','shyam','gopal']
]
name = input("Enter a Name: ")
if name in data[0]:
    print(f"hello {name}")
elif name in data[1]:
    print(f"hello {name}")
else:
    print("Name is not present")

# Second Method:
name = input("Enter a Name: ")
if name == data[0][0]:
    print(f"Hello {name}")
elif name == data[0][1]:
    print(f"Hello {name}")
elif name == data[0][2]:
    print(f"Hello {name}")
elif name == data[1][0]:
    print(f"Hello {name}")
elif name == data[1][1]:
    print(f"Hello {name}")
elif name == data[1][2]:
    print(f"Hello {name}")
else:
    print("Name is not in the list")












