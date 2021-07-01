a = int(input("a = "))
b = int(input("b = "))

if a > b:
    for son in range(b, a, 1):
        print(son)
else:
    for son in range(b, a, -1):
        print(son)
