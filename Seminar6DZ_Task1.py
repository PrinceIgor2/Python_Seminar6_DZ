# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


my_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]

all_occurrences = [index for index, element in enumerate(my_list) if element == 'йцу']

print("The element was found at: " + str(all_occurrences))
print(f"The second occurrence of the element was found at: {all_occurrences[1]}" )