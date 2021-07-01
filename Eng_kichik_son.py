sonlar = [2, 8, 4, 14, 13, 0, 5, 6, 9]

kichikSon = sonlar[0]

for son in sonlar:
    if kichikSon > son:
        kichikSon = son

print(f"kichikSon = {kichikSon}")