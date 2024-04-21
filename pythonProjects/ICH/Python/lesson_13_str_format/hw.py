"""
1.  Напишите программу, которая запрашивает у пользователя его имя,
    возраст и место проживания, а затем выводит их
    в следующем формате:
    "Привет, меня зовут {0}. Мне {1} лет. Я живу в {2}."
    Вместо {0}, {1} и {2} подставьте соответствующие значения.
    Используйте метод format() для форматирования строки.
    Потом попробуйте использовать f-строку.
    Выведите результат на экран с помощью команды print.
    Пример вывода:
    Введите ваше имя: Alice
    Введите ваш возраст: 25
    Введите ваше место проживания: London
    Привет, меня зовут Alice. Мне 25 лет. Я живу в London.

"""

name = input("Введите ваше имя: ")
age = input("Введите ваш возраст: ")
city = input("Введите ваше место проживания: ")

string1 = "Привет, меня зовут {0}. Мне {1} лет. Я живу в {2}.".format(name, age, city)
print(string1)

string_f = f"Привет, меня зовут {name}. Мне {age} лет. Я живу в {city}."
print(string_f)


"""
    2. Напишите программу, которая запрашивает у пользователя два числа
    и выводит их сумму и произведение в следующем формате:


    "Сумма: {sum:.2f}, Произведение: {product:.2f}"
     Вместо {sum:.2f} и {product:.2f} подставьте соответствующие значения,
     округленные до двух десятичных знаков.

     Используйте f-строки с использованием форматных спецификаторов для
     форматирования чисел. Выведите результат на экран с помощью команды print.


Пример вывода:


Введите первое число: 3.14159

Введите второе число: 2.71828


Сумма: 5.86, Произведение: 8.54
"""

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))


sum_res = num1 + num2
prod_res = num1 * num2

print(f"Сумма: {sum_res:.2f}, Произведение: {prod_res:.2f}")