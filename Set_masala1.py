# add metodi yordamida bitta parametr qo'shish mumkin.
mevalar = {"Olma", "Anor"}
mevalar.add("Gilos")
print(mevalar)

# setni listga o'tkazib, listni setga o'tkazib, toifasini chop etish.
mevalar = {"Olma", "Anor"}
mevalar = list(mevalar)
print(type(mevalar))
mevalar = set(mevalar)
print(type(mevalar))

# setga update metodi yordamida elementlar qo'shish.
mevalar = {"Olma", "Anor"}
mevalar.update(["Shaftoli", "Gilos"])
print(mevalar)

# setdan bitta mevani o'chirish.
mevalar = {"Olma", "Anor"}
mevalar.remove("Olma")
print(mevalar)

# setdagi barcha parametrlarni tozalab tashlash.
mevalar = {"Olma", "Anor"}
mevalar.clear()
print(mevalar)

# setni butunlay xotiradan tozalash.
mevalar = {"Olma", "Anor"}
del mevalar