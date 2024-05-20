# With no Loop break
# while True:
#     print("Let's go")



# While Loop break:
# keep_going = True
# while keep_going == True:
#      print("Hello Nepal")
#      keep_going = False




# counter = 1
# while counter < 4:
#      counter += 1
#      print(counter)




# for i in range(4):
#      print("*******")
     


# Multiplication Table:
# num = int(input("Enter a Number: "))
# for i in range(20):
#     print(str(num)+"*"+str(i+1)+"="+str((i+1)*num))



# name = input("Enter a Name: ")
# for letter in name:
#     print(letter)



# Nested Loop:
# num = float(input("Enter a Number: "))
# if num >= 0:
#     if num == 0:
#         print("Neutral Number")
#     else:
#         print("Positive Number")
# else:
#  if num < 0:
#     print("Negative Number")



# Using for Loop:
# for i in range(10):
#     print("Next Candidate Please......")
#     skill = input(str(i+1)+"."+"enter a skill you have: ")
#     if skill == "Kubernetes":
#         print("Everyone go home. We found our candidate")
#         continue
# print("Done for the days")



# Using while Loop:
# i = 1
# while i <= 6:
#    print("Next Candidate Please......")
#    skill = input(str(i)+"."+"enter a skill you have: ")
#    i = i+1
#    if skill == "Kubernetes":
#         print("Everyone go home. We found our candidate")
#         continue
# print("Done for the days")



# data = [11,12,34,99,101]
# i = 0
# while i<len(data):
#     print(data[i])
#     i+=1


# data = [0,2,4,6,8,10,12,14,16,18,20]
# i= 0
# while i<len(data):
#     print(data[i])
#     i += 1

# Even numbers between 0-20:
# i = 0
# while i <= 20:
#     print(i)
#     i = i+2
    

# Adding two data:
# data = [
#     [10,20,30,40,50],
#     [200,300,400,500,600]
# ]
# i = 0
# ft = 0
# lt = 0
# while i< len(data):
#      ft += data[i][0]
#      lt += data[i][-1]
#      i += 1
# print(ft)
# print(lt)


# data = [
#     [10,20,30,40,50],
#     [200,300,400,500,600]
# ]
# i = 0
# while i< len(data):
#     print(sum(data[i]))
#     i += 1

# Multiplication Table:
# num = int(input("Multiplication Table of "))
# i = 1
# while i <= 10:
#     print(str(num)+"*"+str(i)+"="+str((i)*num))   
#     i += 1 


# lang = 'nep'
# match lang:
#     case 'nep':
#         print("Nepali")
#     case 'eng':
#         print("English")
#     case _:
#         print("Other languages")
         
# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# Operator = input("Enter Operator: ")
# match Operator:
#     case '+':
#         print('Addition is',a+b)
#     case '-':
#         print('Subtraction is',a-b)
#     case '*':
#         print('Multiplication is',a*b)
#     case '/':
#         print('Division is',a/b)
#     case _:
#         print("Other Operation")

    

# data = ['ram','sita','gita','hari']  
# for name in data:
#     print(name)


# users = [
#      ['ram','sita','gita'],
#      ['hari','shyam','gopal']
# ]
# for user in users:
#     for name in user:
#      print(name)

# Sorting data:
# users = [
#     ['ram', 'sita', 'gita'],
#     ['hari', 'shyam', 'gopal']
# ]
# for group in users:
#     sorted_users = [sorted(group)]
#     for group in sorted_users:
#         for name in group:
#          print(name)

# users = [
#     ['ram', 'sita', 'gita'],
#     ['hari', 'shyam', 'gopal']
# ]
# for group in users:
#     sorted_users = [sorted(group)]
#     for group in sorted_users:
#          print(group)


# users = [
#      ['ram','sita','gita','ram', 'hari'],
#      ['hari','shyam','gopal','shyam', 'gita'],
#      ['ram','laxmi','gita','laxmi']
# ]
# new_name = input("Enter a Name: ")
# name_found = False
# for user in users:
#     for name in user:
#      if name == new_name:
#         print(f"{name} is found")
#         name_found=True
# if not name_found:
#     print(f"{name} is not found")



# users = [
#     {'name':'ram','gender':'male'},
#     {'name':'sita','gender':'female'},
#     {'name':'laxmi','gender':'female'}
# ]
# name_input = input("Enter a Name: ")
# for user in users:
#     if name_input == 'ram':
#         if user['name'] == 'ram':
#             print("The gender of Ram is",user['gender'])
#     elif name_input == 'sita':
#         if user['name'] == 'sita':
#             print("The gender of sita is",user['gender'])
#     elif name_input == 'laxmi':
#         if user['name'] == 'laxmi':
#              print("The gender of laxmi is",user['gender'])
# else:
#     print("Name not recognized")

 

# users = [
#     {'name':'ram','gender':'male','status':'True'},
#     {'name':'sita','gender':'female','status':'False'},
#     {'name':'laxmi','gender':'female','status':'True'},
#     {'name':'hari','gender':'male','status':'True'},
#     {'name':'rama','gender':'female','status':'True'}
# ]
# total_users = len(users)
# print("Total Number of users are",total_users)

# total_male_users = 0
# for user in users:
#  if user['gender'] == 'male':
#     total_male_users += 1
# print("Total Number of male users are",total_male_users)
    


# total_female_users = 0
# for user in users:
#  if user['gender'] == 'female':
#     total_female_users += 1
# print("Total Number of female users are",total_female_users)

# total_active_users = 0
# for user in users:
#  if user['status'] == 'True':
#     total_active_users += 1
# print("Total Number of active users are",total_active_users)

# total_inactive_users = 0
# for user in users:
#  if user['status'] == 'False':
#     total_inactive_users += 1
# print("Total Number of inactive users are",total_inactive_users)

# total_active_male_users = 0
# for user in users:
#  if user['gender'] == 'male' and user['status'] == 'True':
#     total_active_male_users += 1
# print("Total Number of active male users are",total_active_male_users)

# total_inactive_male_users = 0
# for user in users:
#  if user['gender'] == 'male' and user['status'] == 'False':
#     total_inactive_male_users += 1
# print("Total Number of inactive male users are",total_inactive_male_users)

# total_active_female_users = 0
# for user in users:
#  if user['gender'] == 'female' and user['status'] == 'True':
#     total_active_female_users += 1
# print("Total Number of active female users are",total_active_female_users)
    
# total_inactive_female_users = 0
# for user in users:
#  if user['gender'] == 'female' and user['status'] == 'False':
#     total_inactive_female_users += 1
# print("Total Number of inactive female users are",total_inactive_female_users)

   







  
       

     
     
  



