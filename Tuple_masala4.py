# juft va toq o'rindagilarni chiqarish
a = (1, 4, 10, 6, 7)
print(a[1], a[3])
print(a[0], a[2], a[4])

# 1-usul.
juft = []
toq = []
for i in range(len(a)):
       if (i + 1) % 2 == 0:
              juft.append(a[i])
       else:
              toq.append(a[i])
print(juft)
print(toq)

# Maxsus masala - 2.
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

b = list(a)
c = []
for i in range(len(b)):
       c.append(b[0])
       if b[0] == b[-1]:
           break
       c.append(b[-1])
       b.pop(0)
       b.pop(-1)
       if not b:
              break
a = tuple(c)
print(a)