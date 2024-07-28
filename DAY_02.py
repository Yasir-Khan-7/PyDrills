# Write a Python program to calculate the area of a
# rectangle given its length and width

def Area_of_Recatangle(length,width):
    area_of_rectangle = length*width
    return area_of_rectangle

result = Area_of_Recatangle(4,5)
print("The area of rectangle is: ",result)

# Create a program that takes a user's name and age as
# input and prints a greeting message
def greeting(name,age):
    print(f"Hello {name} you are {age} years old")

name = input("Please Enter your name: ")
age = input("Enter your age: ")

greeting(name,age)
    


# Write a program to check if a number is even or odd

def check_for_odd_even(num):
    if num%2==0:
        print("number is even")
    else:
        num%2==1
        print("number is odd")
check_for_odd_even(11)
            
    
#  Given a list of numbers, find the maximum and minimum
# values

lst =[2,13,4,1,6,7]
def check_for_max_and_min(lst):
    max =0
    min =lst[0]
    for x in lst:
        if x>max:
            max =x
    print("maximum is: ",max)
    
    for x in lst:
        if x<min:
            min=x
    print("Minimum is: ",min)
    
check_for_max_and_min(lst)

#  Create a Python function to check if a given string is a
# palindrome



# Calculate the compound interest for a given principal
# amount, interest rate, and time period

#  Write a program that converts a given number of days
# into years, weeks, and days

#  Given a list of integers, find the sum of all positive
# numbers

# Create a program that takes a sentence as input and
# counts the number of words in it

# Implement a program that swaps the values of two
# variables.