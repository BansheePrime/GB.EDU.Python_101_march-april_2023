"""
Задание 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""
#!/usr/bin/env python3
user_input = input("Пожалуйста, введите целые числа через пробел: ")
i = 0
user_list = user_input.split()
print(type(user_list))
print(user_list)

if len(user_list) % 2 == 0:
    print(f"Вы ввели чётное количество чисел.")
else:
    print(f"Вы ввели нечётное количество чисел.")
    odd_number = 

while i < list_size:
    user_input = input("Пожалуйста, введите значение: ")
    user_list.append(user_input)
    i = i + 1

print(f"Мы с Питоном посчитали, что список будет таким: {user_list}")
