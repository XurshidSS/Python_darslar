# Vaqt bilan ishlash.
import datetime as dt
vaqt = dt.datetime.now()
print(vaqt.year)
print(vaqt.month)
print(vaqt.day)
print(vaqt.weekday())
print(vaqt.hour)
print(vaqt.minute)
print(vaqt.second)
print(vaqt.microsecond)
t = dt.datetime.now()
def vaqt(t):
    print(f"soat: {t.hour}:{t.minute} bo'ldi")
vaqt(t)

""" vaqtni belgilash """
x = dt.datetime(2021,7,28,19,0,0)
print(x)

# salom so'zini 10 sekundda chiqarish.
import datetime as dt
x = dt.datetime.now().second
while True:
    print(dt.datetime.now().second - x)
    if x + 10 == dt.datetime.now().second:
        print("SALOM")
        x = dt.datetime.now().second
        break
