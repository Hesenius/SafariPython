
x = 99
y = 100
print(x == y)  # bool literals True, False
print(x != y)
print(type(x == y))

x = "Hello"
y = "He"
# y = y + "llo"
y += "llo"
print(x, y)
print(x == y)  # content-comparison equality, implemented __eq__
# many others __lt__ etc..
print(x != y)
print(x is y)

# "Recently" we got the "Walrus" operator
# Walrus assignment has value
print(f"x before is {x}")
print(x := 3)
print(f"x after is now {x}")

# < > <= >=
print(3 < 9)

# name = input("What is your name ")
# print("Hello", name)

# Not permitted, we're ignoring the value of the expression
# wal := 55
x = (wal := 55)
print(wal)
print(type(x))
# Not meaningful either, but evidently permitted
x + 2

x = "Hello"
y = "He"
y += "llo"
# y = "Hello"
print(x == y)
print(x is y)

# and, or are bool type operators xor is in a library!
# & | are bitwise operators (they work on bool)
print(x == "Hello" and len(x) > 3)
# bitwise xor is built in
print(3 ^ 6)
