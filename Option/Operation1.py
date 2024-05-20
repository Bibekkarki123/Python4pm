a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

option = int(input('''
  1.Addition
  2.Subtraction
  3.Multiplication
  4.Division
Choose a option:  '''))

if option == 1:
    print("Addition of two number is",a+b)
elif option == 2:
    print("Subtraction of two number is",a-b)
elif option == 3:
    print("Multiplication of two number is",a*b)
elif option == 4:
    print("Division of two number is",a/b)
else:
    print("Mathematical operation cannot be performed")