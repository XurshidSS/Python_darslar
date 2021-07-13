# rekursiya - o'ziga murojaat qiladigan funksiya

# 1-masala. k dan n gacha bo'lgan

def birDanNgacha(k, n):
    if n == k:
        print(f"{k}, {n})
    else:
        print(f"{k}, {n}")
        birDanNgacha(k + 1)

birDanNgacha(1, 10)

# 2-masala. n dan 1 gacha teskari tartibda:

def n_dan_1_gacha(n):
    if n == 1:
        print(n)
    else:
        print(n)
        n_dan_1_gacha(n - 1)

n_dan_1_gacha(10)

# 3-masala. Faktorial
def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n - 1)

print(f(5))

# 4-masala. 1 dan n gacha bo'lgan sonlar yig'indisi
def yigindi(n):
    if n == 1:
        return 1
    else:
        return n + yigindi(n - 1)

print(yigindi(10))

# 5-masala. n gacha bo'lgan toq sonlarni teskari tartibda chiqaring.
def toqSonlar(n):
    if n == 1:
        print(n)
    else:
        if n % 2 == 0:
            n = n - 1
        print(n)
        toqSonlar(n - 2)

print(toqSonlar(10))

# 6-masala. n gacha bo'lgan toq sonlar yig'indisini chiqaring.
def toqSonlar(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            n = n - 1
        return n + toqSonlar(n - 2)

print(toqSonlar(10))

# 7-masala. Fibonachi sonlarining n-chi hadini chiqaring.
def fibonachi(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n-2)

def fibonachiHadlari(n):
    for i in range(1, n + 1):
        print(fibonachi(i), end=" ")

fibonachiHadlari(20)


