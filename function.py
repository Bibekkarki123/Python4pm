# def mathematical_operation (a,b):
#     print("Addition of two numbers: ",a+b)
#     print("Subtraction of two numbers: ",a-b)
#     print("Multiplication of two numbers: ",a*b)
#     print("Division of two numbers: ",a/b)

# mathematical_operation(10,5)

# def message(subject,number):
#     for i in range(number):
#         print(subject)

# message("Python",5)


# def marks_details(subject,marks_obtained,total,percentage,division):
#     print("Subject Name: ",subject)
#     print("Obtained Marks: ",marks_obtained)
#     print("Total Marks: ",total)
#     print("Percentage: ",percentage)
#     print("Division: ",division)

# marks_details("Science",80,100,80,"Distinction")

# def marks_details(subject1,marks1,subject2,marks2,subject3,marks3,subject4,marks4):
#     print("Subject Name: ",subject1)
#     print("Marks in Science: ",marks1)
#     print("Subject Name: ",subject2)
#     print("Marks in Social: ",marks2)
#     print("Subject Name: ",subject3)
#     print("Marks in Computer: ",marks3)
#     print("Subject Name: ",subject4)
#     print("Marks in Maths: ",marks4)
#     total = (marks1+marks2+marks3+marks4)
#     print("Total Marks: ",total)
#     percent = (total/400)*100
#     print("Percentage: ",percent)
#     if percent >= 80 and percent <= 100:
#             print("Division: Distinction")
#     elif percent >= 60 and percent < 79:
#             print("Division: First Division")
#     elif percent >= 45 and percent < 59:
#             print("Division: Second Division")
#     elif percent >= 32 and percent < 44:
#             print("Division: Third Division")
#     else:
#         print("Division: Fail")

# marks_details("Science",70,"Social",65,"Computer",85,"Maths",90)
    

# def add(x,y):
#     return x+y

# result = add(5,6)
# print(result)

# def take_value():
#     p = int(input("Enter value of P: "))
#     t = int(input("Enter value of T: "))
#     r = int(input("Enter value of R: "))
#     return[p,t,r]
# def result():
#     value = take_value()
#     p = value[0]
#     t = value[1]
#     r = value[2]
#     return (p*t*r)/100
# def display():
#     print("Simple Interest is ",result())

# display()

# def take_value():
#     name = input("Enter Name: ")
#     subject1 = int(input("Enter marks in Subject 1: "))
#     subject2 = int(input("Enter marks in Subject 2: "))
#     subject3 = int(input("Enter marks in subject 3: "))
#     return [name,subject1,subject2,subject3]
# def result():
#     value = take_value()
#     name = value[0]
#     subject1 = value[1]
#     subject2 = value[2]
#     subject3 = value[3]
#     total = subject1+subject2+subject3
#     percent = (total/300)*100
#     return [subject1,subject2,subject3,name,total,percent]
# def display():
#     subject1,subject2,subject3,name,total,percent = result()
    # if subject1<=100 and subject2<=100 and subject3<=100:
    #    if percent >= 80 and percent <= 100:
    #         print("Name: ",name)
    #         print("Total: ",total)
    #         print("Percentage: ",percent)
    #         print("Division: Distinction")
    #    elif percent >= 60 and percent < 79:
    #         print("Name: ",name)
    #         print("Total: ",total)
    #         print("Percentage: ",percent)
    #         print("Division: First Division")
    #    elif percent >= 45 and percent < 59:
    #         print("Name: ",name)
    #         print("Total: ",total)
    #         print("Percentage: ",percent)
    #         print("Division: Second Division")
    #    elif percent >= 32 and percent < 44:
    #         print("Name: ",name)
    #         print("Total: ",total)
    #         print("Percentage: ",percent)
    #         print("Division: Third Division")
    #    else:
    #       print("Division: Fail")
#     else:
#        print("Marks in subjects are exceeding 100")
    
# display()



# users = [
#     {'name':"ram",'gender':"male"},
#     {'name':"shyam",'gender':"male"},
#     {'name':"sita",'gender':"female"},
#     {'name':"gita",'gender':"female"}
# ]

# def male():
#     for user in users:
#         if user['gender'] == "male":
#             print(user)

# male()

# def female():
#     for user in users:
#         if user['gender'] == "female":
#             print(user)

# female()






