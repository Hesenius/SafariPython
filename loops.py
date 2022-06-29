x = 3
while x > 0:
    print(f"> {x}")
    # x = x - 1
    x -= 1
    # Python does NOT have ++/--
    # x--
print("------------")

x = 4
while x > 0:
    print(x)
    x -= 1
    if x == 2:
        # break and continue, but not "labled"
        continue
        # break
    print("still in loop")
print("------------")

x = 4
while x > 0:
    print(x)
    x -= 1
    if x == 2:
        break
        # pass
    print("still in loop")
else:  # executes if the test terminates the loop
    print("test failed")

print("out of loop")

# no "do-while"

names = ["Fred", "Jim", "Sheila"]
for n in names:
    print(f"name is {n}")

for idx, n in enumerate(names):
    print(f"at index {idx} name is {n}")

names = {"Fred": "Jones", "Alice": "Smith"}
for n in names:
    print(f"n is {n}")

# pull tuples of key, value
for n in names.items():
    print(f"n is {n}")

for k, v in names.items():
    print(f"name is {k} value is {v}")

names = ["Fred", "Jim", "Sheila"]
# mapping is lazy! produces a map object that has not been evaluated
# y = map(lambda x: x.upper(), names)
y = list(map(lambda x: x.upper(), names))
print(f"names is {names}, y is {y}")

# lambda "body" must be a simple, single expression
adder = lambda a, b: a + b
sum = adder(1, 2)
print(sum)

name_lengths = list(map(lambda x: len(x), names))
print(name_lengths)