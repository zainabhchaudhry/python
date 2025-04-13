# GIAIC Lesson 07 – Set, Frozenset & Garbage Collection Practice

import gc  # Import garbage collection module

# ------------------------------
# 1. Sets
# ------------------------------
print("🟢 SETS")

my_set = {1, 2, 3, 4, 4, 5}
print("Original set (no duplicates):", my_set)

# Adding and removing elements
my_set.add(6)
print("After adding 6:", my_set)

my_set.remove(2)
print("After removing 2:", my_set)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)

print()

# ------------------------------
# 2. Frozenset
# ------------------------------
print("🧊 FROZENSET")

frozen = frozenset([10, 20, 30, 30])
print("Frozen set:", frozen)

# frozen.add(40)  # ❌ This will throw error (uncomment to test)
# frozen.remove(10)  # ❌ This will throw error (frozenset is immutable)

# Can perform set ops
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
print("Union:", fs1 | fs2)
print("Intersection:", fs1 & fs2)

print()

# ------------------------------
# 3. Garbage Collection
# ------------------------------
print("🗑️ GARBAGE COLLECTION")

class Demo:
    def __del__(self):
        print("Destructor called. Object deleted.")

obj = Demo()
del obj  # Manually deleting object to trigger destructor

# Collecting garbage manually
print("Running garbage collector...")
collected = gc.collect()
print(f"Unreachable objects collected: {collected}")
