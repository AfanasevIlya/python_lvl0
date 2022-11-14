def dumb_defence_do():
    while True:
        print('Зашифровать - 1, Дешифровать - 2')
        do = input()
        if do in '12' and len(do) == 1:
            return int(do)
        else:
            print('Неправильное действие, попробуйте ещё раз')

def dumb_defence_lang():
    while True:
        print('Выберите язык рус/англ')
        lang = input()
        if lang.lower() in ['русский', 'ру', 'рус', 'rus', 'ru', 'russian']:
            return 'ru'
        elif lang.lower() in ['английский', 'англ', 'en', 'eng', 'english']:
            return 'en'
        else:
            print('Вы ошиблись в выборе языка, попробуйте ещё раз')

def dumb_defence_step(lang):
    while True:
        print('Выберите шаг сдвига от 1 до 25 для англиского и от 1 до 31 для русского алфавита')
        step = input()
        if lang == 'ru':
            if step.isdigit() and 1 <= int(step) <= 31:
                return int(step)
            else:
                print('Неправильный шаг, попробуйте ещё раз')
        else:
            if step.isdigit() and 1 <= int(step) <= 25:
                return int(step)
            else:
                print('Неправильный шаг, попробуйте ещё раз')

def get_low_and_up(lang): #в зависимости от аргумента задает англ или русс алфавит, возвращает строчные,прописные и длинну алфавита
    if lang == 'ru':
        return "абвгдежзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", 32
    else:
        return 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 26

def dumb_defence_msg(lang): #защита от ввода на отличном от выбранного языка
    while True:
        print('Введите ваше сообщение')
        msg = input()
        if lang == 'ru':
            for i in msg.lower():
                if i in 'abcdefghijklmnopqrstuvwxyz':
                    print('Тут есть немножко англиского, введите сообщение на русском')
                    break
                else:
                    return msg
        else:
            for i in msg.lower():
                if i in "абвгдежзийклмнопрстуфхцчшщъыьэюя":
                    print('Тут есть немножко русского, введите сообщение на английском')
                    break
                else:
                    return msg

def caesar_foo(do, lang, step, msg):
    outcome_msg = ''
    low_al, up_al, alph_len = get_low_and_up(lang) #вызываем функцию которая наполнит переменные алфавитов и длинны
    for i in range(len(msg)):
        if msg[i].isalpha():
            if msg[i] == msg[i].lower():
                start_index = low_al.index(msg[i])
                if do == 1:
                    final_index = (start_index + step) % alph_len
                else:
                    final_index = (start_index - step) % alph_len
                outcome_msg += low_al[final_index]
            else:
                start_index = up_al.index(msg[i])
                if do == 1:
                    final_index = (start_index + step) % alph_len
                else:
                    final_index = (start_index - step) % alph_len
                outcome_msg += up_al[final_index]
        else:
            outcome_msg += msg[i]
    return outcome_msg


do = dumb_defence_do()
lang = dumb_defence_lang()
step = dumb_defence_step(lang)
msg = dumb_defence_msg(lang)
print(caesar_foo(do, lang, step, msg))
#for i in range(1, 26):
#    print(caesar_foo(2, 'en', i, 'oa reqi ku Veznut!'))