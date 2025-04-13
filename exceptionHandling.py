# GIAIC Lesson 09 - Exception Handling (Clean Version)

# 1. Basic try-except
try:
    print("Dividing 10 by 0...")
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

print("-" * 40)

# 2. Multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result is:", result)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Please enter a valid number.")
except Exception as e:
    print("Something went wrong:", e)

print("-" * 40)

# 3. Raising custom exceptions
def check_age(age):
    if age < 18:
        raise ValueError("You must be at least 18 years old to register.")
    return "Registration successful!"

try:
    age = int(input("Enter your age: "))
    message = check_age(age)
    print(message)
except ValueError as e:
    print("Error:", e)

print("-" * 40)

# 4. Using assert (with exception handling)
age = -5
try:
    assert age >= 0, "Age cannot be negative"
    print("Age is valid.")
except AssertionError as e:
    print("Assertion failed:", e)

print("-" * 40)

# 5. Nested try-except with file handling
try:
    try:
        file = open("non_existing_file.txt", "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("File not found!")
    finally:
        print("Inner finally block.")
except Exception as e:
    print("Outer error:", e)
finally:
    print("Outer finally block.")
