# 58-dars 1-masala.
# 1-usul.
n = int(input("n = "))

def kvadrat(n):
    for i in range(n):
        print(n * "*")

kvadrat(n)

# 2-usul.
n = int(input("n = "))

def kvadrat(n):
    print((n * "*" + '\n') * n)

kvadrat(n)

# 58-dars 2-masala.
# 1-usul.
n = int(input("n = "))

def NB(n):
    S = str("")
    for i in range(1, n + 1):
        if n % i == 0:
            S = S + str(i) + ' '
    print(S)

NB(n)

# 2-usul.
n = int(input("n = "))

def NB(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end = ' ')

NB(n)