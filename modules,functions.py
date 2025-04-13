# GIAIC Lesson 08 - Modules & Functions

# -------------------------------
# 1. Defining Functions
# -------------------------------

# A simple function that greets a user
def greet(name):
    return f"Hello, {name}! Welcome to Python!"

# Calling the function
print(greet("Zainab"))

# Function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width

# Calling the function with arguments
print(f"Area of rectangle: {calculate_area(5, 3)}")

# -------------------------------
# 2. Using Built-in Modules
# -------------------------------

import math  # Importing the math module to use built-in functions

# Using math module to calculate the square root
number = 16
print(f"Square root of {number} is {math.sqrt(number)}")

# Using math module to find the factorial of a number
num = 5
print(f"Factorial of {num} is {math.factorial(num)}")

# -------------------------------
# 3. Creating Custom Modules (Uncomment to test in separate file)
# -------------------------------

# Suppose we create a separate Python file called 'my_module.py'
# Below is how you would import and use functions from it.

# import my_module
# result = my_module.some_function()
# print(result)

# -------------------------------
# 4. Lambda Functions (Anonymous Functions)
# -------------------------------

# Lambda function to multiply two numbers
multiply = lambda x, y: x * y
print(f"Multiplication result: {multiply(4, 7)}")

# -------------------------------
# 5. Function with Default Arguments
# -------------------------------

# Function with a default argument
def greet_with_default(name="Guest"):
    return f"Hello, {name}!"

print(greet_with_default())  # Uses default value
print(greet_with_default("Zainab"))  # Custom value
