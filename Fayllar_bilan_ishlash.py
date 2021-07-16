# Fayllar yaratish
f = open("mening_faylim.doc", "x")

# Faylni o'qish
f = open("mening_faylim.doc")
print(f.read())

# Faylga yozish uchub ochish
f = open("mening_faylim.doc", 'w')
f.write("Salom Xurshid!\n")
f.write("Ahvollaringiz yaxshimi?\n")

# Faylni ochish stillari:
# f = open("fayl_nomi.kengaytmasi", "stili")
# stillari:
# "r" -> read -> o'qish uchun
# "a" -> append -> matn oxiridan yozish uchun
#  "w" -> write -> ustidan yozish uchun (overwrite)
# "x" -> create -> yaratish uchun

# "t" -> text -> matn stili birlamchi holatda
# "binar" -> binar stili

# faylni yana o'qish uchun ochib ko'ramiz:
f = open("mening_faylim.doc", 'r')
print(f.read())

# "a" -> append
f = open("mening_faylim.doc", 'a')

f.write(" Salom")
f.close()

f = open("mening_faylim.doc", 'r')
print(f.read())

# Men haqimda
f = open("Men_haqimda.txt")
f.close()

f = open("Men_haqimda.doc", 'w')
f.write("Xurshid ")

f = open("Men_haqimda.doc", 'r')
print(f.read())

f = open("Men_haqimda.doc", 'a')

f.write("Saidov")
f.close()

f = open("Men_haqimda.doc", 'r')
print(f.read())