# 1-masala. 57-dars.
from math import factorial as f

def myFunction(n, k):
    return(f(n) / (f(k) * f(n - k)))

print(myFunction(6, 4))

# 2-masala.
# 1-usul.
n = int(input("n = "))

def naturalSon(n):
    for i in range(1, n):
        if i ** 2 < n:
            print(i)

naturalSon(n)

#2-usul.
n = int(input("n = "))

def naturalSon(n):
    qiymat = []
    for i in range(1, n):
        if i ** 2 < n:
            qiymat.append(i)
    return qiymat

print(naturalSon(n))

# 3-masala.
# 1-usul.
n = int(input("n = "))

def chiziqcha(n):
    txt = ''
    for i in range(n):
        txt += '-'
    print(txt)

chiziqcha(n)

# 2-usul.
n = int(input("n = "))

def chiziqcha(n):
    print('-' * n)

chiziqcha(n)