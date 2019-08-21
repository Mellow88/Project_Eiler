fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1


def get_sum_fibonachi(n, limit):
    sum_list = []
    while fib(n) % 2 == 0 or fib(n) < limit:
        sum_list.append(fib(n))
        n += 1
    # print(sum_list)
    return sum(sum_list)


print(get_sum_fibonachi(0, 4000000))
