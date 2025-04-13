# GIAIC Lesson 06 – Lists, Tuples, and Dictionary Practice

# ------------------------------
# 1. Lists
# ------------------------------
print("📋 LISTS")

fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Adding elements
fruits.append("mango")
print("After append:", fruits)

# Inserting at index
fruits.insert(1, "orange")
print("After insert at index 1:", fruits)

# Removing elements
fruits.remove("banana")
print("After remove:", fruits)

# Accessing elements
print("First fruit:", fruits[0])

# Loop through list
print("Loop through list:")
for fruit in fruits:
    print("-", fruit)

print()

# ------------------------------
# 2. Tuples
# ------------------------------
print("🔗 TUPLES")

colors = ("red", "green", "blue")
print("Tuple:", colors)

# Accessing elements
print("Second color:", colors[1])

# Tuples are immutable – this will cause an error if uncommented
# colors[0] = "yellow"

# Loop through tuple
print("Loop through tuple:")
for color in colors:
    print("-", color)

print()

# ------------------------------
# 3. Dictionary
# ------------------------------
print("📚 DICTIONARY")

student = {
    "name": "Zainab",
    "age": 24,
    "course": "Python"
}

print("Original dictionary:", student)

# Access values
print("Name:", student["name"])

# Add new key-value
student["grade"] = "A"
print("After adding grade:", student)

# Update value
student["age"] = 25
print("After updating age:", student)

# Remove a key
del student["course"]
print("After deleting course:", student)

# Loop through dictionary
print("Looping through dictionary:")
for key, value in student.items():
    print(f"{key} → {value}")

print()

print("✅ Lists, Tuples, and Dictionary practice complete!")
