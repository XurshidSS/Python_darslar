""" Lmabda funksiyasi """

ikkilangani = lambda a: a * 2
print(ikkilangani(10))

# sonning kvadratini chiqarish.

ikkilangani = lambda a: a ** 2
print(ikkilangani(10))

# Lambda funksiyasini ikki va undan ortiq parametr bilan qo'llash.

yigindi = lambda a, b: a + b

print(yigindi(2, 3))
print(yigindi(5, 8))

# To'rtta sonning o'rta arifmetigini chiqarish.

urtaArifmetik = lambda a, b, c, d: (a + b + c + d) / 4
urtaArifmetik1 = lambda a, b, c, d: yigindi(yigindi1(a, b), yigindi1(c, d)) / 4
print(urtaArifmetik(1, 2, 3, 4))
print(urtaArifmetik1(1, 2, 3, 4))

# Masala. Ixtiyoriy sonni darajasini chiqarish. Lambdani funksiya ichida qo'llash.

def kvadrat(n):
    return lambda a: n ** a
son = kvadrat(5)
print(son(2))
print(kvadrat(5)(2))

# Masala-1. Aylana radiusini kiritish orqali funksiya ichida lambdani qo'llab, doira yuzasini chiqaring.

def aylanaUzunligi(L):
    return lambda pi: pi * (L / (2 * pi) ** 2)
x = aylanaUzunligi(10)
print(x(3.14))

Masala-2.

def f(a, b):
    return lambda c: a * b * c
V = f(2, 3)
print(V(4))

# Masala-3.

def yigindi(a, b):
    return lambda n: (a + b) ** n
x = yigindi(2, 3)
print(x(4))

# Masala-4.

def ism(x):
    return lambda n: (x + ' ') * n
y = input("Ismingizni kiriting:  ")
k = ism(y)
print(k(5))