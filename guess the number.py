from random import *

def is_valid(num):
    return str(num).isdigit() and int(num) in range(1, 101)

def initialization_game(num):
    r = randint(1, num)
    count = 1
    while True:
        n = input(f'Назовите число от 1 до {num}: ')
        if not is_valid(n):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        n = int(n)
        if n < r:
            count += 1
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        elif n > r:
            count += 1
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        else:
            print('Вы угадали, поздравляем!')
            print(f'кол-во попыток: {count}')
            break
    get_answer()

def get_answer():
    answer = input('Желаете повторить?(Y / N) ').lower()
    if answer =='y':
        start_game()
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

def start_game():
    num = int(input('Введите правую границу интервала случайного числа(1, n): '))    
    initialization_game(num)

print('Добро пожаловать в числовую угадайку')
start_game()











