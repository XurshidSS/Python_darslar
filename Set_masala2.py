# Tasodifiy sonlar tuzib, ularni setga o'tkazish.
import random
a = []
for i in range(10):
    k = random.randint(1, 10)
    a.append(k)
print(a)
a = set(a)
print(a)

# Matematika, fizika, informatika fanlaridan olimpiada ketma-ket bo'lib o'tdi.
# Olimpiadaga kirgan o'quvchilar ro'yxatini chiqaring.
matematika = ["Ibrohim", "Muhammad", "Abbos", "Bunyod"]
fizika = ["Oybek", "Ibrohim", "Shaxzod", "Abbos"]
informatika = ["Oybek", "Ibrohim", "Abbos", "Shaxzod"]
a = matematika + fizika + informatika
a = set(a)
print(a)

#
matematika = ["Ibrohim", "Muhammad", "Abbos", "Bunyod"]
fizika = ["Oybek", "Ibrohim", "Shaxzod", "Abbos"]
informatika = ["Oybek", "Ibrohim", "Abbos", "Shaxzod"]
x = matematika + fizika
y = fizika + informatika
z = matematika + informatika
a = matematika + fizika + informatika
mat_fiz = set(x)
fiz_inf = set(y)
mat_inf = set(z)
print(len(matematika))
print(len(fizika))
print(len(informatika))
print(len(mat_fiz))
print(len(fiz_inf))
print(len(mat_inf))
a = set(a)
print(len(a))

