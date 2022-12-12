# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

user_number = int(input("Введите число: "))
my_list = [(-3)**i for i in range(user_number)]
print(f"Итогоый список: {my_list}")