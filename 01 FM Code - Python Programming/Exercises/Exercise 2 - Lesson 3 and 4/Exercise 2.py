# Question 1: Arithmetic and Assignment Operators
x = 3
y = 2
# TODO: Add 3 to x using the += operator
x +=3
# TODO: Multiply y by 2 using the *= operator
y *=2
# TODO: Divide x by y and store the result in a variable called 'result'
result = x / y
# TODO: Print the value of 'result'
print(result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators
a = 10
b = 15
c = 30
# TODO: Create a condition that checks if a is greater than b
condition1 = a > b
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
condition2 = b == b
# TODO: Create a condition that checks if c is less than or equal to  a
condition3 = c <= a
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#        The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a

# TODO: Print the value of 'final_condition'
final_condition = condition1 or("condition2 and condition3")
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = float(input("Enter the test score:"))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if 90 <= score <= 100:
   grade = "A"
elif 80 <= score < 90: 
   grade = "B"
elif 70 <= score < 80:
   grade = "C"
elif 60 <= score < 70:
   grade = "D"
elif  score < 60:
   grade = "Fail"     
# TODO: Print the grade for the given score
print(f"The grade for the score is {grade} ")
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = float(input("first number?"))
num2 = float(input("second number?"))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("enter operation (+, -, *, /): ")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
result = 10
if operation == "+":
   result = num1 + num2 
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
      print("error")
    else:
     result = num1 / num2
else: 
    print("provide an operator")

# TODO: Handle the case of division by zero

# TODO: Print the result of the operation
print(f"{num1} {operation} {num2} = {result}")