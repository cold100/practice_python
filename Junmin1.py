# 1. Список из числа.
# Дано: натуральное число N.
#
# Задание: написать функцию, которая возвращает список всех цифр этого числа в обратном порядке.
#
# Пример:
#
#  123, результат: [3, 2, 1]

def Junmin1(Number: int) -> list:
    reciprocal_number = []
    while Number > 0:
        remainder = Number % 10
        reciprocal_number.append(remainder)
        Number = Number // 10
    return reciprocal_number
  
  
num = 1234
res = Junmin1(num)
print(res)
