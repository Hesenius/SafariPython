
class Thing:
    # __slots__ defines the permitted attributes
    # they might not all be there
    __slots__ = ["x", "y", "z"]

    staticvar = "I'm a static-like variable"

    # no "method overloading"
    def __init__(self, x, y):
        print('invoking initializer')
        # self prefix is NOT OPTIONAL
        # self.x = "value for x"
        # self.y = 99
        self.x = x
        self.y = y

# for humans to debug
    def __str__(self):
        return f"I'm a Thing with x = {self.x}"

# repr should create a source-code version of the object
    def __repr__(self):
        return f"Thing({self.x}, {self.y})"

    @staticmethod
    def show_stuff():
        print("this is a static-like method")

class Anohter:
    def __init__(self):
        print("initliazing Another")

class Thang(Thing, Anohter):
    def __init__(self):
        print("initializing Thang")
        # special syntax for single inheritance
        # super().__init__("I'm making a Thang", 256)

        # long-form super, finds the type "to the right" of the listed type
        super(Thang, self).__init__("I'm making a Thang", 256)
        super(Thing, self).__init__()

# t = Thing("value for x")
t = Thing("value for x", 99)
# t.x = "value for x"
# t.y = 99

print(t.x)
print(t.y)
# not like this...
# print("x" in t)
print(hasattr(t, "x"))
print(hasattr(t, "banana"))

# __slots__ prevents this :)
# reputation is that objects created with __slots__ are smaller and faster
# t.bad = "hahnahaa"
# print(t.bad)

# print(t.z)

print(str(t))
print(t)

stuff = [t]
print(stuff)

Thing.show_stuff()

print(Thing.staticvar)

t2 = Thang()

print(t2)