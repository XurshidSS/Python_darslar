
# 81-bet 5-masala

import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b + math.sqrt(D))/(2 * a)
    x2 = (-b - math.sqrt(D))/(2 * a)
    print(f"x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
elif D < 0:
    print("Yechimga ega emas")