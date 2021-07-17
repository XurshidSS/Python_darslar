# Klasslarga kirish.
class Son:
    x = 1
    y = 2
son1 = Son()    # son1 -> bu obyekt, Son() -> klass
print(son1.x)
son2 = Son()
print(son2.y)

# Xulosa. Bitta klassdan xohlagancha obyekt olish mumkin.

""" def __init__() funksiyasi: """

class Son:
    def __init__(self, x, y):
        self.x = x
        self.y = y

son3 = Son(4, 5)
print(son3.x, son3.y)
son4 = Son(6, 7)
print(son4.x, son4.y)

""" xususiyatni o'chirish """
class Son:
    def __init__(self, x, y):
        self.x = x
        self.y = y

son1 = Son(1, 2)
son1.x = 3
print(son1.__dict__)

del son1.x   # son1.x ni o'chirish
print(son1.__dict__)

# obyektni o'zini o'chirish
del son1

""" class da metodlar """


class Avtomobil:
    def __init__(self, rusumi):
        self.rusumi = rusumi
    def signal(self):
        print("Biiib!!!")

malibu = Avtomobil("Malibu")
malibu.signal()

# shaxs degan metod tuzish
class Shaxs:
    def __init__(self, ism, fam, shahri, mahallasi):
        self.ism = ism
        self.fam = fam
        self.shahri = shahri
        self.mahallasi = mahallasi
    def tuliq_ism(self):
        return self.ism + ' ' + self.fam
    def tuliq_manzil(self):
        return self.shahri + ' ' + self.mahallasi

sh1 = Shaxs("Xurshid", "Saidov", "Jizzax shahri", "Olmazor mahallasi")
print(sh1.tuliq_ism(), sh1.tuliq_manzil())
