# Задача 2. Четные числа Фибоначчи
#
# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1


def get_sum_fibonachi(n, limit):
    sum_list = []
    while fib(n) % 2 == 0 or fib(n) < limit:
        sum_list.append(fib(n))
        n += 1
    # print(sum_list)
    return sum(sum_list)


print(get_sum_fibonachi(0, 4000000))
