def minMax(x, y):
    if x > y:
        x = x + y
        y = x - y
        x = x - y
    print(f"x = {x}, y = {y}")

a = 1
b = 2
c = 3
d = 4

minMax(a, b)
minMax(c, d)
minMax(b, c)
minMax(a, d)