# Welcome to PyQues!
# This repository is dedicated to Python mini challenges,
# ranging from basic to intermediate levels.
# It is designed to help you enhance your coding skills through a series of questions and exercises.

# Q 1: Write a Python program to print "Hello, World!"

user_input = input("Say Hello World!: ")

print(user_input)

# Q 2: Calculate the sum of two numbers entered by the user(changed to mini calculator)

def mini_Calculator(x,y,operator):
    try:
        if operator =="+":
            return x+y
        elif operator == "-":
            return x-y
        elif operator =="*":
            return x*y
        elif operator =="/":
            return x/y
        else:
            print("invalid Operator... ")
    except ValueError:
        print(ValueError)
        
        

num_1 = input("Enter number 1: ")
num_2 = input("Enter number 2: ")
operator = input("Enter operator +,-,/,* to perform operation:  ")
mini_Calculator(int(num_1),int(num_2),operator)    

# Q 3: Convert temperature from Celsius to Fahrenheit.
def Temperature_conversion(Temp,type_of_conversion):
    print(Temp)
    if type_of_conversion =="F":
        celsious = (Temp-32)*(5/9)
        return round(celsious,2)
    
    elif type_of_conversion =="C":
        Farhenheit = (Temp*9/5)+32
        return round(Farhenheit,2)
    
Temp = input("Enter Temperature: ")
type_of_conversion = input("Enter conversion type 'F' for Farhenheit and 'C' for Celsius:  ")

result =Temperature_conversion(int(Temp),type_of_conversion)
print(result)

    