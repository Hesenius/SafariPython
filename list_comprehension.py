
names = ["fred", "jim", "sheila"]
upper_names = [x.upper() for x in names]  # effectively a map operation
print(names)
print(upper_names)

from math import sqrt
# flat map like? or nested loop like??
# if is "filter-like"
vals = [ (o, a, h) for o in range(1, 13) for a in range(1, o) if (h := sqrt(o*o + a*a) % 1) == 0]
print(vals)

