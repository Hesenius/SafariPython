
# print(x)
# x = "Hello"
x = 99.9
# print("Hello") ; print('Hello')
print(x)
print(f'Hello the value of x is {x ** 2}')
print(type(x))
print(type(str(type(x))))
x = "Bonjour"
print(f'Hello the value of x is now {x}')
print(type(x))
ten = 10
three = 3
print(type(ten))
x = ten / three
print(type(x))
print(x)

x = ten // three
print(type(x))
print(x)

# % is MOD, not remainder (difference from remainder is visible with negatives
print(ten % three)

x = 1000000000
print(x)
# int type is essentially limited by memory
# this can sometimes take "a long time"
x = x ** 100
print(x)

# complex type
print(1j)
print(type(1j))

# string concat
print("Hello" + " World")

print("count is " + str(99))  # String conversion via __str__

print("Hello", "World", "It's a nice day", sep="--", end="")
print("and it's going to be warm in Colorado")
