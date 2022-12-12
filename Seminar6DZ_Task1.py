# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


# my_list = ["йцу", "фыв", "ячс", "цук", "йцукен"]

# all_occurrences = [index for index, element in enumerate(my_list) if element == 'йцу']
   

# print("The element was found at: " + str(all_occurrences))
# print(f"The second occurrence of the element was found at: {all_occurrences[1]}" )


# # список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# test_list = []
# print(f"список: {test_list}")
# test_item = input("Введите искомую строку: ")


# def check_list(test_list, test_item):
#     count = 0
#     for i in range(len(test_list)):
#         if test_list[i] == test_item:
#             count += 1
#             if count == 2:
#                 return i
#     else:
#         return -1


# print(f"ответ: {check_list(test_list, test_item)}")



# # список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# test_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# test_item = ('qwe')

# filtering = list(filter(lambda x: test_item in x, test_list))
# print(filtering)



my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]

all_occurrences = [index for index, element in enumerate(my_list) if element == 'qwe']
   

print("The element was found at: " + str(all_occurrences))
print(f"The second occurrence of the element was found at: {all_occurrences[1]}" )