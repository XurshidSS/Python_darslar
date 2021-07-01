name = str(input("name = "))
x = name[-1]
if x == "a" or x == "i" or x == "u" or x == "o" or x == "e":
    surname = name + "yev"
    print(surname)
elif name[-1] == "f":
    print(name.replace("f", "p") + "ov")
else:
    print(name + "ov")