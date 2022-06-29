names = [ "Fred", "Jim", "Sheila"]
# list is the type Python generally uses for indexed sequence
print(type(names))
print(names)
print(names[0])  # zero-based index
print(names[-1])  # negative, "backwards from the end"
print(names[-2])

# "slicing"
numbers = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
print(numbers)
print(numbers[0:3]) # start, "fence"
print(numbers[0:8:2]) # start, "fence", stride

numbers.sort(reverse=True)
print(numbers)

numbers.append(-1)
print(numbers)

print(3 in numbers)
print(33 in numbers)

# somewhat lazy evaluation!
print(range(1, 20, 3))
print(range(1, 20, 3)[3])
# force evaluation:
print(list(range(1, 20, 3)))


# x = range(1,33,3)
# print(x)
print(x := range(1,33,3))
print(x)


tup = 10, "Albert"
# parens on tuples are generally optional
# tup = (10, "Albert")
print(type(tup))
print(tup)

print(tup[0])
# tuples are unmodifiable, this would fail
# tup[0] = 100

# number of items in tuple must match number of variables
count, name = tup
print(f"name is {name}, count is {count}")

names = {"Fred": "Jones", "Alice": "Smith"}
print(type(names))
print(names)
print("Fred" in names)
print(names["Fred"])
print("Bertie" in names)
# print(names["Bertie"])
# None is kinda like null?? or like undefined,
# "Unit" represents "I have no value to offer"
print(names.get("Bertie"))
print(names.keys())
print(names.values())
print(names.items())

unique = {"One", "Two", "Three"}
print(type(unique))
print(unique)
print("One" in unique)
unique.add("One")
print(unique)
unique = set()
print(type(unique))
print(unique)

