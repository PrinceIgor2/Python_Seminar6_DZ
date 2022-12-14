# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.


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

print(list(map(lambda i: ((-3)**i), [i for i in range(user_min_max_number('Введите количество членов последовательности: '))])))