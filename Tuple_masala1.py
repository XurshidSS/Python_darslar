numbers = (10, 2, 3, 4, 5, 6)
a = max(numbers)
b = min(numbers)
print(a + b)

# o'rta arifmetik
numbers = (10, 2, 3, 4, 5, 6)
print(sum(numbers) / len(numbers))

# o'rta arifmetikni maxsus yo'l bilan ishlash
i = 0
summa = 0
for number in numbers:
    i += 1
    summa += number
urta_arifmetik = summa / i
print(urta_arifmetik)