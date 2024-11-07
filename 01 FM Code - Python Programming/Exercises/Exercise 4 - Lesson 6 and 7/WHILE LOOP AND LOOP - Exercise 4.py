# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ['banana', 'apple', 'pear', 'mango', 'strawberry']
# TODO: Use a for loop to print each fruit in the list
for fruits in fruits:
    print(fruits)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count=int(input("set the count: "))

while count >= 0:
    print(count)
    count-=1
#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for number in range(1, 11):
    square = number*number
    print(square)
#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colours = ['blue', 'yellow', 'orange', 'green', 'black']
# TODO: Use a for loop to select and print 3 random colors from the list
for colours in colours:
    print(colours)

#-------------------------------------------------------------------------
# TODO: Create a new file named 'math_operations.py' with the following content:

# TODO: Import the custom module and use its functions
import math_operations
# TODO: Use a while loop to create a simple calculator
import math_operations  
  
while True:  
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtration")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number "))

    if choice == "1":
       result = math_operations.add(num1, num2)
    elif choice == "2":
       result = math_operations.subtract(num1, num2)
    elif choice == "3":
        result = math_operations.multiply(num1, num2)
    elif choice == "4":
        result = math_operations.divide(num1, num2)
    else:
        print("invalid, please try again")
