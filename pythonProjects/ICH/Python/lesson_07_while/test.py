"""
3. Напишите программу, которая запрашивает у пользователя целое положительное число
   и проверяет, является ли оно простым.
   Простое число - это число, которое делится только на 1 и на само себя без остатка.
   Используйте цикл while и проверку деления числа на все числа от 2 до N-1 для решения задачи.
   Выведите соответствующее сообщение на экран с помощью команды print.

Пример вывода:

Введите целое положительное число: 17

Число 17 является простым.

"""
"""a, b, = int(input('a: ')), int(input('b: '))
for i in range(a, b + 1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
"""


number = int(input('Введите целое положительное число: '))
count = 2
egal = 0
res = number % count
while count < number:
    if egal == res:
        break
    else:
        count += 1
else:
    print('Число', number, 'является простым.')















