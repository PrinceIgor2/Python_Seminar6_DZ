# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

my_list, string = ["qwe", "asd", "zxc", "qwe", "ertqwe"], 'qwe'

second_occurence = -1 if my_list.count(string) < 2 else list(filter(lambda x: x[1] == string, enumerate(my_list)))[1][0]
  
print(f"The second occurrence of the string {string} was found at: {second_occurence}")