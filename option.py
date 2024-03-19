
num_1 = int(input("Enter a First number:\n"))
num_2 = int(input("Enter a second number:\n"))


print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")

option =int(input("Enter a option:\n"))

if option == 1:
    print(num_1+num_2)
elif option == 2:
    print(num_1-num_2)
elif option == 3:
    print(num_1*num_2)
else:
    print(num_1/num_2)
