def get_natural_sum(start, end, arg_1, arg_2):
    sum_list = []
    for start in range(end):
        if start % arg_1 == 0 or start % arg_2 == 0:
            sum_list.append(start)
    return sum(sum_list)

print(get_natural_sum(1, 1000, 3, 5))

