# """ 1. modullar bilan ishlash """
# # import qilish
# '1. modulni import qilish'
# import pygame
#
# '2. moduldagi funksiyani import qilish'
# from time import daylight
#
# '3. moduldan bir necha obyektni import qilish'
# from os import chdir, remove
#
# '4. moduldagi barcha obyektlarni import qilish'
# from math import *
# import math
#
# print(sin(0))
#
# """ o'zimiz yaratgan modulni import qilish """
# # from meningModulim import *
# # print(y, x)
#
# """ boshqa papkalardagi modullarni import qilish """
# from examp2 import sonlar
# print(sonlar)
#
# # Masala.
# from matematikaModuli import *
# a = 5
# b = 2
# print(qushish(a, b))
# print(ayirish(a, b))
# print(kupaytirish(a, b))
# print(bulish(a, b))

""" dir -> funksiyasi bu - moduldagi barcha obyektlarni qaytaradigan funksiya """
from matematikaModuli import *
import math
print(dir(math))
import matematikaModuli
print(dir(matematikaModuli))