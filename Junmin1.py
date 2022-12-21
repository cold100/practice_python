# 1. Список из числа.
# Дано: натуральное число N.
#
# Задание: написать функцию, которая возвращает список всех цифр этого числа в обратном порядке.
#
# Пример:
#
#  123, результат: [3, 2, 1]

def Junmin1(intNumber) -> list:
    reciprocal_number = []
    while intNumber > 0:
        remainder = intNumber % 10
        reciprocal_number.append(remainder)
        intNumber = intNumber // 10
    return reciprocal_number
  
  
num = 1234
res = Junmin1(num)
print(res)
