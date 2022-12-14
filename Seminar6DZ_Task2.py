# 2- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math, random

def user_min_max_number(input_string: str, min_num: int = None, max_num: int = None) -> int:
    """
    Спрашивает у пользователя число в диапзоне от  min_num до  mах_num:
    Args:
    input_string - предложение ввода
    Returns:
    int - число
    """
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите больше {min_num}')
                continue
            if max_num and num > max_num:
                print(f'Введите меньше, чем {max_num}')
                continue
            return num
        except ValueError:
            print('Похоже это не число, попробуте еще раз')

nums = [random.randint(0, 20) for _ in range(user_min_max_number('Введите количество элементов списка: '))]
print(f'Исходный список -> {nums}')
mult_list = list(map(lambda i: (nums[i]*nums[-(i+1)]), [i for i in range(math.ceil(len(nums)/2))]))
print(f'Произведение пар элементов -> {mult_list}')


