
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

name = input("What is your name ")
print("Hello", name)
