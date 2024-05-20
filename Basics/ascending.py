# x = int(input("Enter a value of x: "))
# y = int(input("Enter a value of y: "))
# z = int(input("Enter a value of z: "))
# print("Ascending order are as follows:")
# if x<y and x<z:
#     print(x)
#     if y<z:
#         print(y)
#         print(z)
#     else:
#         print(z)
#         print(y)
# elif y<x and y<z:
#     print(y)
#     if x<z:
#        print(x)
#        print(z)
#     else:
#        print(z)
#        print(x)
# else:
#     print(z)
#     if x<y:
#         print(x)
#         print(y)
#     else:
#         print(y)
#         print(x)


# x = int(input("Enter a value of x: "))
# y = int(input("Enter a value of y: "))
# z = int(input("Enter a value of z: "))
# print("Descending order are as follows:")
# if x>y and x>z:
#     print(x)
#     if y>z:
#         print(y)
#         print(z)
#     else:
#         print(z)
#         print(y)
# elif y>z and y>x:
#     print(y)
#     if z>x:
#         print(z)
#         print(x)
#     else:
#         print(x)
#         print(z)
# else:
#     print(z)
#     if x>y:
#         print(x)
#         print(y)
#     else:
#         print(y)
#         print(x)



# Another Method:
# Ascending Order:
x = int(input("Enter a value of x: "))
y = int(input("Enter a value of y: "))
z = int(input("Enter a value of z: "))
if x<y and x<z:
    print(x)
    print(y)
    print(z)
elif y<z and y<x:
    print(y)
    print(z)
    print(x)
elif z<x and z<y:
    print(z)
    print(x)
    print(y)
    



