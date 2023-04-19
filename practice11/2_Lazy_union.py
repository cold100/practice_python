# 2. Ленивое объединение
# Дано: 2 списка произвольной длины.
#
# Задание: написать функцию, которая возвращает результат объединения этих списков.
# Используйте функцию itertools.chain.
#
# Пример:
#  list(f([1, 2], [3, 4])), результат: [1, 2, 3, 4]


from itertools import chain


def list_concatenation(list1, list2):
    return list(chain(list1, list2))


print(list_concatenation([1, 2], [3, 4]))
