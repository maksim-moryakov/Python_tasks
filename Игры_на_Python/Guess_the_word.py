# Создаем игру угадай слово.

import random

# Инициализация переменных 
lowDigit = 10       # Нижняя граница случайных числа
highDigit = 99      # Верхняя граница случайных числа
digit = 0           # Загадонное комьютером число

countInput = 0      # Колличество попыток угадать
win = False         # Угадал текущее число?
playGame = True     # Продолжается ли игра?
x = 0               # Число, которое вводит пользователь
startScore = 100    # Начальное количество очков
score = 0           # Текущее количество очков
maxScore = 0        # Максимальное за сессию игры

# Главный цикл
while playGame:

    # Первое действие, приветсвие игрока.
    digit = random.randint(lowDigit, highDigit)
    score = startScore
    print('----------------------')
    print('Компьютер загадал число, попробуй отгадать!')
    print(f'Загаданое число {digit}')
    while not win and score > 0:
        print('-' * 30)
        print(f'Заработано очков: {score}')
        print(f'Рекорд: {maxScore}')
    
        x = '' # Начальное значение, до введеного пользователем.

        # Проверка введенно значения, является ли оно числом
        while not x.isdigit():
            x = input(f'Введите число в диапозоне от {lowDigit} до {highDigit}: ')
            if not x.isdigit():
                print('Введите, пожалуйста, число.')

        x = int(x)  # Преобразуем введеное значение в число.
        
        #  Проверка на выйгрыш
        if x == digit:
            win = True
        else:
            # Функционал подсказки для пользователя    
            length = abs(x - digit)
            if length < 3:
                print('Очень горячо!')
            elif length < 5:
                print('Горячо!')
            elif length < 10:
                print('Тепло')
            elif length < 20:
                print('Холодно')
            else:
                print('Стужа')   

            # Функционал подсчета очков
            if countInput == 7:
                score -= 10
                if  digit % 2 == 0:
                    print('Число четное')
                else:
                    print('Число нечетное')
            elif countInput == 6:
                score -= 8
                if digit % 3 == 0:
                    print('Число делиться на 3')
            elif countInput == 5:
                score -= 4
                if digit % 4 == 0:
                    print('Число делится на 4')
                else:
                    print('Число не делится на 4')
            elif 2 < countInput < 5:
                score -= 2
                if x > digit:
                    print('Загаданое число МЕНЬШЕ вашего')
                else:
                    print('Загаданное число БОЛЬШЕ вашего')
            score -= 5
        countInput += 1
    
    print('*' * 40)
    if x == digit:
        print('Победа! Поздравляем!')
        win = True
    else:
        print('У Вас закончились очки. Вы проиграли :(')
    
    # Предложение закончить или продолжить играть           
    if input('Enter - сыграем еще, 0 - выход ') == '0':
        playGame = False
    else:
        win = False
    
    if score > maxScore:
        maxScore = score



