# 5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 200.
#  Создайте список кортежей, первый элемент которого - индекс элемента, 
# а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

import random


random_nums = [random.randint(1, 10) for _ in range(30)]
print(f'Список кортежей без совпадений -> {list(filter(lambda x: x[0] != x[1], enumerate(random_nums)))}')
print(f'Список удаленных кортежей -> {list(filter(lambda x: x[0] == x[1], enumerate(random_nums)))}')   
