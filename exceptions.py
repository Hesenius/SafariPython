import random

def might_break():
    if random.random() > 0.5:
        raise ValueError("it's big!!")
    if random.random() > 0.5:
        raise TypeError("wrong type (honest)")
    # if random.random() > 0.5:
    #     raise IndexError("invalid index")
    return "success"

try:
    msg = might_break()
    print(msg)
    # ...
except ValueError as ve:
    print(f"it broke with bad value... {ve}")
except TypeError as te:
    print(f"broke with TypeError {te}")
else:
    print("none of those exceptions")
    might_break()
    print("still going in else")
finally:
    print("finally....")


