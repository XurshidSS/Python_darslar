sonlar = [2, 8, 4, 14, 13, 0, 5, 6, 9]

for index in range(len(sonlar)):
    for key in range(len(sonlar)):
        if sonlar[index] < sonlar[key]:
            sonlar[index] = sonlar[key] + sonlar[index]
            sonlar[key] = sonlar[index] - sonlar[key]
            sonlar[index] = sonlar[index] - sonlar[key]
            print(sonlar)

print(sonlar)