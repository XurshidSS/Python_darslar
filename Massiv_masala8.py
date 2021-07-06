sonlar = [1, 2, 5, 8, 10, 13]

for son in sonlar:
    if son % 2 == 0:
        sonlar[sonlar.index(son)] = son * 2
    else:
        sonlar[sonlar.index(son)] = son ** 2
print(sonlar)