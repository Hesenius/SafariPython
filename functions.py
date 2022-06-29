
# dynamically typed language arg types are "unknown"
# can check dynamically with type(blah)
# language permits "annotations" of type (but does not check)
# plugins/pre-processors can use this to check
def add(a : int, b : int) -> int:
    # if type(a) != int:
    #     print("oops shouldn't be called unless with int")
    #     raise TypeError("called my function with something other than int")
    return a + b

print(f"adding 2 and 3 gives {add(2, 3)}")
print(f"adding 'Fred' and 'Jones' gives {add('Fred', 'Jones')}")

def nowt():
    pass # not returning anything results in returning "None"

print(nowt())

def sum(c, d):
    return add(c, d)

print(sum(3,4))

# args and kwargs are CONVENTION not syntax
def many_args(a = 99, b = 10, *args, **kwargs):
    print(f"a is {a} b is {b}")
    print(type(args))
    print(args)
    for v in args:
        print(f"> {v}")

many_args(1, 2)
many_args(1)
many_args(b="b", a="a")

def day_of_week(day, month, year):
    print(f"day = {day} month = {month}")

day_of_week(month=12, day=11, year=2022)

many_args(1, 2, 9, 8, 7, 6)