# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

n = input(f'Введите точность: ')

m = len(n) - 2


def pi(eps = 1.0e-5):
    s = 0
    d = 1
    sgn = 1
    while True:
        a = 4 / d
        s = s + sgn * a
        if a < eps:
            return s
        sgn = -sgn
        d = d + 2
 
 
print(round(pi(), m))