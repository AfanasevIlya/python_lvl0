import random

# проверка валидности введеного числа


def is_valid(a):
    return a.isdigit() and 1 <= int(a) <= 100

# проверка валидности введенной границы


def is_valid_rightcorner(a):
    return a.isdigit() and int(a) > 1

# проверка выхода


def ext_try():
    while True:
        ext = input()
        if ext.isdigit() and int(ext) == 1:
            return False
        elif ext.isdigit() and int(ext) == 0:
            return True
        else:
            print(
                'Введите 1 чтобы повторить игру, 0 чтобы выйти')

# Защита от дурака для ввода числа


def dumb_protection():
    while True:
        num = input()
        if is_valid(num):
            return int(num)
        else:
            print(
                'А может быть все-таки введем целое число от 1 до 100?')

# Защита от дурака для границ


def corner_protection():
    while True:
        num = input()
        if is_valid_rightcorner(num):
            return int(num)
        else:
            print('n должно быть числом и быть больше 1')


print('Добро пожаловать в числовую угадайку')
flag_ext = False
while not flag_ext:
    answer, rightcorner, n_try,  = -1, 100, 0
    print('Укажите n для генерации чисел от 1 до n')
    rightcorner = corner_protection()
    a = random.randint(1, rightcorner)
    print('Число сгенерировано, введите число чтобы угадать')
    while answer != a:
        answer = dumb_protection()
        if answer == a:
            print('Вы угадали, поздравляем!')
        elif answer > a:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        n_try += 1
    print(f'Число попыток: {n_try}')
    print('Хотите сыграть ещё раз? 1 - да, 0 - нет')
    flag_ext = ext_try()
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
