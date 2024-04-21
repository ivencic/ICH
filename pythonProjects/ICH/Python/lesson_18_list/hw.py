"""
1. Напишите программу, которая принимает строку от пользователя и
разбивает ее на отдельные слова. Затем программа должна объединить
слова в обратном порядке с использованием метода join().
Используйте динамический массив и методы для работы со строками.
Выведите результат на экран с помощью команды print.

Пример вывода:

Введите предложение: Программирование это интересно и полезно
Перевернутое предложение: полезно и интересно это Программирование
"""
text = input("Введите предложение: ")
words = text.split()
revers_text = ' '.join(words[::-1])

print("Перевернутое предложение:", revers_text)

"""
2. Напишите программу, которая принимает список чисел от пользователя
 и добавляет каждое число в динамический массив. 
 Затем программа должна принимать новое число от пользователя и 
 добавлять его в динамический массив до тех пор, 
 пока пользователь не введет команду "Выход". 
 Используйте метод append() для добавления элементов в 
 динамический массив и условный оператор для проверки команды "Выход". 
 Выведите итоговый динамический массив на экран с помощью команды print.

Пример вывода:

Введите число (или 'Выход' для завершения): 1
Введите число (или 'Выход' для завершения): 2
Введите число (или 'Выход' для завершения): Выход
Динамический массив: [1, 2]
"""
my_array = []

while True:
    user_input = input("Введите число (или 'Выход' для завершения): ")
    if user_input.lower() == 'выход':
        break
    else:
        number = int(user_input)
        my_array.append(number)

print("Динамический массив:", my_array)
