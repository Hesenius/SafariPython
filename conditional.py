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

