# Задача 5. Наименьшее кратное
#
# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?


#
# for i in range(2520, 10000000):
#     lst = []
#     for n in range(1, 21):
#         if i % n != 0:
#             lst.append(i)
#     if lst.count(i) == 20:
#         print(i)
#         break

num = 1

while n <= 20:
    if ifDividesAll(num):
        break
    else:
        num =+ 1

print(dd(20))