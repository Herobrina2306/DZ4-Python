# Задана натуральная степень k. Сформировать случайным образом список
#  коэффициентов (значения от 0 до 100) многочлена и записать
#  в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

n = int(input(f'Введите максимальную степень: '))
lst  = [f'{randint(0, 100)}x**{n}']
for i in range(n - 1, -1, -1):
    if randint(0, 10) > 5:
        m = randint(-100, 100)
        if m > -1:
            lst.append(f'+{m}x**{i}')
        else:
            lst.append(f'{m}x**{i}')

print(*lst, '= 0')
s = (''.join(lst))


def write_file(st):
    with open('file1.txt', 'w') as data:
        data.write(st)

write_file(s)

