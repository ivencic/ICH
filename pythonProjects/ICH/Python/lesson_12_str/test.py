'''
3.  Напишите программу, которая запрашивает у пользователя строку и
    выравнивает ее по центру с заданной шириной. Если строка не может
    быть выровнена по центру из-за нечетной ширины,
    она должна быть выровнена смещением вправо.
    Используйте методы center() и rjust() для выравнивания строки.

Пример вывода:
Введите строку: Python
Введите ширину: 10
Результат:

  Python
'''

text = input('Введите строку: ')
count = int(input('Введите ширину: '))

if count <= len(text):
    print('Вы ввели меньше символов чем сама строка')
elif len(text) % 2 == count % 2:
    text = text.center(count)
elif len(text) % 2 != count % 2:
    text = text.rjust(count)
print(text)




