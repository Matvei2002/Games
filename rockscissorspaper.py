import random, sys

print('Камень, ножницы, бумага')

# В данных переменных - количество побед, ничьих и поражений
wins = 0
ties = 0
losses = 0

while True: # главный цикл игры
    print ('%s побед, %s поражений, %s ничьих' % (wins, losses, ties))
    while True: # цикл выбора хода
        print("Камень, ножницы или бумага? (Введите к, н, б или в): ")
        playerMove = input()

        if playerMove == 'в':
            sys.exit() # выход из программы
        if playerMove == 'к' or playerMove == 'н' or playerMove == 'б':
            break # выход из цикла выбора хода

# Отображение выбора пользователя
    if playerMove == 'к':
        print('КАМЕНЬ и ...')
    elif playerMove == 'н':
        print('НОЖНИЦЫ и ...' )
    elif playerMove == 'б':
        print('БУМАГА и ...')

    # Отображение выбора компьютера
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'к'
        print('КАМЕНЬ')
    elif randomNumber == 2:
        computerMove = 'н'
        print('НОЖНИЦЫ')
    elif randomNumber == 3:
        computerMove = 'б'
        print('БУМАГА')

    # Отображение и учет результата
    if playerMove == computerMove:
        print('Ничья!')
        ties = ties + 1
    elif playerMove == 'к' and computerMove == 'н':
        print('Вы выиграли!')
        wins = wins + 1
    elif playerMove == 'б' and computerMove == 'к':
        print('Вы выиграли!')
        wins = wins + 1
    elif playerMove == 'н' and computerMove == 'б':
        print('Вы выиграли!')
        wins = wins + 1
    elif playerMove == 'к' and computerMove == 'б':
        print('Вы проиграли!')
        losses = losses + 1
    elif playerMove == 'б' and computerMove == 'н':
        print('Вы проиграли!')
        losses = losses + 1
    elif playerMove == 'н' and computerMove == 'к':
        print('Вы проиграли!')
        losses = losses + 1
