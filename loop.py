# GIAIC Lesson 05 – Control Flow & Loops Practice

# ------------------------------
# 1. if, if-else, if-elif-else
# ------------------------------
print("🚦 Control Flow Statements")

age = 18

if age < 18:
    print("You're a minor.")
elif age == 18:
    print("You're just 18! Welcome to adulthood!")
else:
    print("You're an adult.")

print()

# ------------------------------
# 2. for loop
# ------------------------------
print("🔁 For Loop - Printing numbers 1 to 5")
for i in range(1, 6):
    print("Number:", i)

print()

# ------------------------------
# 3. while loop
# ------------------------------
print("🔄 While Loop - Counting down from 5")
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1

print()

# ------------------------------
# 4. break statement
# ------------------------------
print("🛑 Break Statement Example")
for num in range(1, 10):
    if num == 5:
        print("Breaking at number 5")
        break
    print("Number:", num)

print()

# ------------------------------
# 5. continue statement
# ------------------------------
print("➡️ Continue Statement Example")
for num in range(1, 6):
    if num == 3:
        print("Skipping number 3")
        continue
    print("Number:", num)

print()

# ------------------------------
# 6. pass statement
# ------------------------------
print("⏭️ Pass Statement Example")
for letter in "AI":
    if letter == "I":
        pass  # Placeholder - does nothing
    print("Letter:", letter)

print()

print("✅ Practice Complete – Great job!")
