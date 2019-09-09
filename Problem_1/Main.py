# Задача 1. Числа, кратные 3 или 5
#
# Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

def get_natural_sum(start, end, arg_1, arg_2):
    sum_list = []
    for start in range(end):
        if start % arg_1 == 0 or start % arg_2 == 0:
            sum_list.append(start)
    return sum(sum_list)

print(get_natural_sum(1, 1000, 3, 5))

