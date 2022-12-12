# 2- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# def mult_lst(lst):
#     l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
#     new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
#     print(new_lst)

# lst = [2, 3, 4, 5, 6]
# mult_lst(lst)
# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# mult_lst(lst)



# # Python code to demonstrate working of
# # List consecutive pair Product
# # Using zip() + list comprehension

# # initializing list
# test_list = [5, 8, 3, 5, 9, 10]

# # printing list
# print("The original list : " + str(test_list))

# # List consecutive pair Product
# # zip() + list comprehension
# res = [i * j for i, j in zip(test_list, test_list[1:])[::2]]

# # Printing result
# print("Pair product of list : " + str(res))


from random import randint


number = int(input('Введите размер списка '))
list = []
list2 = []

for i in range(number):
    list.append(randint(0, 9))

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number = number - 1
        a = list[i] * list[number]
        list2.append(a)
        i += 1

print(list)
print(list2)

