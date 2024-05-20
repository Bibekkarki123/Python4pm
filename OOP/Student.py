
# class Student:
#     x=10
#     def hello(self):
#         obj = Student()
#         print(obj.x)
#         print(self.x)
#         self.info()

#     def info():
#         print("This is info method.")



# obj = Student()
# obj.hello()



# class Student:
#     def add(self,a,b):
#         return a+b
    
    
#     def subtract(self,a,b):
#         return a-b
    
# calulator = Student()


        
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
            return x / y



x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))



calc = Calculator()
print("Addition: ", calc.add(x, y))
print("Subtraction: ", calc.subtract(x, y))
print("Multiplication: ", calc.multiply(x, y))
print("Division: ", calc.divide(x, y))


