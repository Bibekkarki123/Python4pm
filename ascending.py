x = int(input("Enter a value of x:\n"))
y = int(input("Enter a value of y:\n"))
z = int(input("Enter a value of z:\n"))
if x<y and x<z:
    print(x)
    if y<z:
        print(y)
        print(z)
    else:
        print(z)
        print(y)
elif y<x and y<z:
    print(y)
    if x<z:
       print(x)
       print(z)
    else:
       print(z)
       print(x)
else:
    print(z)
    if x<y:
        print(x)
        print(y)
    else:
        print(y)
        print(x)