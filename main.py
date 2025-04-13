print("Hello, world!")

# Operators

# -----------------------------
# 1. Arithmetic Operators
# -----------------------------
a = 10
b = 3

print("Arithmetic Operators:")
print("a + b =", a + b)       # Addition
print("a - b =", a - b)       # Subtraction
print("a * b =", a * b)       # Multiplication
print("a / b =", a / b)       # Division
print("a % b =", a % b)       # Modulus
print("a ** b =", a ** b)     # Exponentiation
print("a // b =", a // b)     # Floor Division
print()

# -----------------------------
# 2. Assignment Operators
# -----------------------------
x = 5
print("Assignment Operators:")
x += 3
print("x += 3 ->", x)
x -= 2
print("x -= 2 ->", x)
x *= 2
print("x *= 2 ->", x)
x /= 2
print("x /= 2 ->", x)
x %= 3
print("x %= 3 ->", x)
x **= 2
print("x **= 2 ->", x)
x //= 2
print("x //= 2 ->", x)
print()

# -----------------------------
# 3. Comparison Operators
# -----------------------------
a = 10
b = 20

print("Comparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print()

# -----------------------------
# 4. Logical Operators
# -----------------------------
x = True
y = False

print("Logical Operators:")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)
print()

# -----------------------------
# 5. Identity Operators
# -----------------------------
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("Identity Operators:")
print("a is b:", a is b)
print("a is c:", a is c)
print("a is not c:", a is not c)
print()

# -----------------------------
# 6. Membership Operators
# -----------------------------
numbers = [1, 2, 3, 4, 5]

print("Membership Operators:")
print("3 in numbers:", 3 in numbers)
print("6 not in numbers:", 6 not in numbers)
print()

# -----------------------------
# 7. Bitwise Operators
# -----------------------------
a = 5  # 0101 in binary
b = 3  # 0011 in binary

print("Bitwise Operators:")
print("a & b =", a & b)    # AND
print("a | b =", a | b)    # OR
print("a ^ b =", a ^ b)    # XOR
print("~a =", ~a)          # NOT
print("a << 1 =", a << 1)  # Left shift
print("a >> 1 =", a >> 1)  # Right shift
