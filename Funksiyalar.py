# # funksiyani e'lon qilish
# def salom(name):
#     print(f"Salom {name}")
# # funksiyani chaqirish
# ism = input("ism = ")
# salom(ism)
#
# # sonning ikkilanganini chiqarish
# def my_func(son):
#     print(f"son * 2 = {son * 2}")
# a = int(input("son = "))
# my_func(a)
#
# """ ko'p parametrli funksiya """
# def tuliq_ism(ism, familiya):
#     tuliq = ism + ' ' + familiya
#     print(tuliq)
#
# tuliq_ism("Oybek", "Narzullayev")
# tuliq_ism("Xurshid", "Saidov")

# """ *args -> bu parametrlar to'plami """
# def ismlar_ruyxati(*ism):
#     print(ism)
#
# ismlar_ruyxati("Oybek", "Xurshid", "Jamshid", "Bekzod")
# ismlar_ruyxati("Oybek")
# ismlar_ruyxati("Xurshid")
# ismlar_ruyxati("Jamshid")
# ismlar_ruyxati("Bekzod")

# def fanlar_ruyxati(*fan):
#     print(fan)
#
# fanlar_ruyxati("Ona tili", "Adabiyot", "Rus tili", "Ingliz tili")

# def myfunction(tulov = 0):
#     print(f"Sizdan to'lov {tulov} so'm")
#
# myfunction(20000)
# myfunction(10000)
# myfunction()

def mycolor(color="qora"):
    print(f"Men yoqtirgan rang {color}")

mycolor("oq")
mycolor("ko'k")
mycolor()