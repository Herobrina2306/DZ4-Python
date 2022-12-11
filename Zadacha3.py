# Задайте последовательность чисел. Напишите программу, которая
#  выведет список неповторяющихся элементов исходной
#  последовательности.

lst = [1, 1, 2, 3, 4, 5, 4, 2, 6, 6, 7, 8, 7]


found = set()
found_again = set()

for a in lst:
    if a in found_again:
        continue
    if a in found:
        found.remove(a)
        found_again.add(a)
    else:
        found.add(a)

print(list(found))