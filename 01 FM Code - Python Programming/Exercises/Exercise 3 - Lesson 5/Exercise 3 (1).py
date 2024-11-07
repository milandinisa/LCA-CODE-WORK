# Question 1: Basic Function Definition and Calling

# Define a function called 'greet' that prints "Hello, World!"
def greet():
    print("Hello, World!")  # Fixed the punctuation

# Call the 'greet' function
greet()

#------------------------------------------------------------------------------------
# Question 2: Function with Parameters

# Define a function called 'personalized_greeting' that takes a name as a parameter and prints a personalized greeting
def personalized_greeting(name):  # Changed parameter name to 'name'
    print("Hello, " + name + "!")  # Added a comma and exclamation mark for better formatting

# Call the 'personalized_greeting' function with your name
personalized_greeting("Mila")

#------------------------------------------------------------------------------------
# Question 3: Function with Return Value

# Define a function called 'square' that takes a number as a parameter and returns its square
def square(number):
    return number * number
# Call the 'square' function with the number 5 and print the result
result_square = square(5)  
print(result_square)  

#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value

# Define a function called 'rectangle_area' that takes length and width as parameters and returns the area of the rectangle
def rectangle_area(length, width): 
    area = length * width
    return area  

# Call the 'rectangle_area' function with length 4 and width 5, and print the result
result_area = rectangle_area(4, 5)  
print(result_area)  

#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument

# Define a function called 'apply_operation' that takes a function and a number as parameters
def apply_operation(func, number):
    return func(number)
# Define a function called 'double' that takes a number as a parameter and returns its double
def double(number):
    return number * 2
# Use the 'apply_operation' function with the 'double' function and the number 7, and print the result
result_double = apply_operation(double, 7)
print(result_double, 7)  

# Use the 'apply_operation' function with the 'square' function and the number 3, and print the result
result_square_operation = apply_operation(square, 3)
print(result_square_operation)  
