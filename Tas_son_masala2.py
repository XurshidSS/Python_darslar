import random
imkoniyat = 1
while imkoniyat <= 5:
    kiritilganSon = int(input("a = "))
    tasodifiySon = random.randint(1, 10)
    if kiritilganSon == tasodifiySon:
        print("Yutdingiz!")
        break
    else:
        print("Yutqazdingiz")
    imkoniyat += 1