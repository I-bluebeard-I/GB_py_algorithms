"""
6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более
чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
"""


from random import randint

number = randint(0, 100)
user_number = -1
count = 1
max_count = 10

while user_number != number:
    print(f'Попытка № {count}')

    while True:
        user_number = input('Угадайте число от 0 до 100: ')
        if user_number.replace('-', '').isdigit():
            user_number = int(user_number)
            count += 1
            break
        else:
            print(f'"{user_number}" не является числом, повторите ввод')

    if count > max_count:
        print(f'Закончилось количество попыток. Згаданное число {number}')
        break
    elif user_number > number:
        print('Нужно меньше\n')
    elif user_number < number:
        print('Нужно больше\n')
    elif user_number == number:
        print(f'Победа! Згаданное число {number}')
