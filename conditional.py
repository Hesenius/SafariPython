x = 99
# indentation matters, must be consistent
# PEP8 must be four spaces :)
if x == 99:
    print("oh look, it's 99!")
    print("still in the if part")
elif x == 98:  # elif avoids excessive indentation
    print("it's 98")
else:
    print("really, I thought it would be 99")
# if x == 99:
#     print("oh look, it's 99!")
#     print("still in the if part")
# else:
#     if x == 98:
#         print("it's 98")
#     else:
#         print("really, I thought it would be 99")

print("all done with conditions")

y = "ninety nine" if x == 99 else "something else"
print(y)

# new with Python 3.10
# kinda "switch/case" in many other languages
# STATEMENT, not expression
x = 101
match x:
    case 99: print("it's 99")
    case 100: print("odd, wasn't expecting that")
    # case _: matches anything else
    case _: print("something else entirely")

# match can do "destructuring" or "extraction"
x = ("One", "Un")
match x:
    case (a, b): print(f"tuple contains {a} and {b}")
