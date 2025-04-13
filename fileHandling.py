# GIAIC Lesson 10 - Input/Output and File Handling

# -------------------------------
# 1. Basic Input and Output
# -------------------------------
name = input("Enter your name: ")
print("Hello,", name)

print("-" * 40)

# -------------------------------
# 2. Writing to a File
# -------------------------------
with open("demo_file.txt", "w") as file:
    file.write("This is line 1.\n")
    file.write("This is line 2.\n")
print("Data written to file successfully.")

print("-" * 40)

# -------------------------------
# 3. Reading from a File
# -------------------------------
try:
    with open("demo_file.txt", "r") as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("The file does not exist.")

print("-" * 40)

# -------------------------------
# 4. Appending to a File
# -------------------------------
with open("demo_file.txt", "a") as file:
    file.write("This line was appended.\n")
print("New line appended to file.")

print("-" * 40)

# -------------------------------
# 5. Reading File Line by Line
# -------------------------------
with open("demo_file.txt", "r") as file:
    print("Reading line by line:")
    for line in file:
        print(line.strip())

print("-" * 40)
