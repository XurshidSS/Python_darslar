class Avtomobil:
    def __init__(self, firmasi, rusumi, yili, rangi):
        self.firmasi = firmasi
        self.rusumi = rusumi,
        self.yili = yili,
        self.rangi = rangi

malibu = Avtomobil("Malibi", 2022, "qora", "Chevrolet")
lacetti = Avtomobil("Lacetti", 2020, "oq", "Chevrolet")

print(malibu.rusumi, malibu.rangi)

# Xodim degan klass yaratish
class Xodim:
    def __init__(self, lavozimi, fani, yoshi, staji):
        self.lavozimi = lavozimi,
        self.fani = fani,
        self.yoshi = yoshi,
        self.staji = staji


Xurshid = Xodim("O'qituvchi", "Informatika va AT", 40, 19)
Alisher = Xodim("O'qituvchi", "Boshlang'ich", 28, 3)

print(Xurshid.__doc__)

# 1-masala.
class Xodim:
    def __init__(self, ismi, manzili, maoshi):
        self.ismi = ismi
        self.manzili = manzili
        self.maoshi = maoshi
    def gap(self):
         print("Mening ismim" + ' ' + self.ismi + ' ' + "maoshim" + ' ' + str(self.maoshi))

xodimlar = []
x1 = Xodim("Xurshid", "Jizzax shahri", 2500000)
xodimlar.append(x1)
x2 = Xodim("Alisher", "Sh. Rashidov tumani", 1800000)
xodimlar.append(x2)
x3 = Xodim("Sodiq", "Jizzax shahri", 2300000)
xodimlar.append(x3)
x4 = Xodim("Oybek", "Jizzax shahri", 1900000)
xodimlar.append(x4)

for xodim in xodimlar:
    xodim.gap()

# Masala-2.
class Xodim:
    def __init__(self, ism, manzili, maoshi):
        self.ism = ism
        self.manzili = manzili
        self.maoshi = maoshi

    def gap(self):
        print(f"Mening ismim {xodim.ism} maoshim {xodim.maoshi}")
        if self.maoshi < 1000000:
            print("Mening oyligim kam!!!")


xodimlar = []

n = int(input("Xodimlar soni: "))
for i in range(n):
    print(f"{i + 1} - xodim")
    ism = input("Ism kiriting: ")
    manzili = input("Manzil kiriting: ")
    maoshi = int(input("Maoshini kiriting: "))
    xodimlar.append(Xodim(ism=ism, manzili=manzili, maoshi=maoshi))



for xodim in xodimlar:
    xodim.gap()
