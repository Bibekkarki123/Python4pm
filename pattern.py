# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     print("*"*i)




# *****
# ****
# ***
# **
# *

# for i in range(5,0,-1):
#     print("*"*i)




# *
# **
# ***
# ****
# *****
# *
# **
# ***
# ****
# *****

# Flag Pattern:
# for i in range(1,6):
#     print("*"*i)
# for i in range(1,6):
#     print("*"*i)



# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()



# *************
# *************
# *************
# *************
# *************
# *************
# *************
#              *************
#              ************* 
#              *************
#              *************
#              *************
#              *************


# Dimensions of the flag
# height = 13  # Number of rows
# width = 26   # Number of columns

# # Print the flag pattern
# for i in range(height):
#     for j in range(width):
#         if (i < 7 and j < 13) or (i >= 7 and j >= 13):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
