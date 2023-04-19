# 2. Длинномер.
# Дано: список строковых значений.
#
# Задание: написать функцию, которая возвращает список длин каждой строки.
#
# Пример:
#  ['Tina', 'Raj', 'Tom'], результат: [4, 3, 3]


def string_lengths(string_list):
    length_list = list(map(len, string_list))
    return length_list


string_list = ['Tina', 'Raj', 'Tom', 'Jarry']
length_list = string_lengths(string_list)
print(length_list)
