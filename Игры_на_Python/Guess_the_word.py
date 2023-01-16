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
    print('----------------------')
    print('Компьютер загадал число, попробуй отгадать!')
    print(f'Загаданое число {digit}')    
    
    # Внутренний цикл
    while not win:
        x = '' # Начальное значение, до введеного пользователем.

        # Проверка введенно значения, является ли оно числом
        while not x.isdigit():
            x = input(f'Введите число в диапозоне от {lowDigit} до {highDigit}: ')
            if not x.isdigit():
                print('Введите, пожалуйста, число.')

        x = int(x)  # Преобразуем введеное значение в число.
        
        #  Проверка на выйгрыш
        if x == digit:
            print('Победа! Поздравляем!')
            win = True
    
    if input('Enter - сыграем еще, 0 - выход ') == '0':
        playGame = False
    else:
        win = False

