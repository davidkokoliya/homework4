from functools import reduce


def my_func(el_p, el):
    return el_p * el

print(f'Список {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат  {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')