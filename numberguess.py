# Игра в угадывание чисел
import random

secretNumber = random.randint(1, 15)
print('Загадал число от 1 до 15')

# Игроку дается 5 попыток
for guessesTaken in range(1, 6):
    print('Угадайте число')
    guess = int(input())

    if guess < secretNumber:
        print('Я загадал число больше предложенного Вами')
    elif guess > secretNumber:
        print('Я загадал число меньше предложенного Вами')
    else:
        break # Число отгадано!

if guess == secretNumber:
    print('Отлично! Количество попыток: ' + str(guessesTaken) + '.')
else:
    print('Не повезло, я загадал число ' + str(secretNumber))