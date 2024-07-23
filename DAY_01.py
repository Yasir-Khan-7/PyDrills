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
    except  Exception as ValueError:
        
        

num_1 = input("Enter number 1: ")
num_2 = input("Enter number 2: ")
operator = input("Enter operator +,-,/,* to perform operation:  ")
sum(num_1,num_2,operator)    
# Q 3: Convert temperature from Celsius to Fahrenheit.