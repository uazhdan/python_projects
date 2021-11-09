
# функция генерация пароля по длине
def generate_password(lenght):
    chars = []
    while len(chars) < int(len_pw):
        if digit_pw == 'Y':  # включает ли пароль цифры
            if neodn_pw == 'Y':  # включает ли в себя неоднозначные цифры 1 и 0
                chars.append(random.choice(digits))
            else:
                chars.append(random.choice(digits_o))

            if upper_pw == 'Y':  # включает ли пароль большие буквы
                if neodn_pw == 'Y':  # включает ли в себя неоднозначные буквы L и O
                    chars.append(random.choice(uppercase_letters))
                else:
                    chars.append(random.choice(uppercase_letters_o))
    
            if low_pw == 'Y':  # включает ли пароль маленькие буквы
                if neodn_pw == 'Y':  # включает ли в себя неоднозначные буквы l, o, i
                    chars.append(random.choice(lowercase_letters)) 
                else:
                    chars.append(random.choice(lowercase_letters_o)) 
    
            if char_pw == 'Y':  # включает ли пароль знаки
                chars.append(random.choice(punctuation))
        
    return chars
 
# основной модуль программы
import random
digits = '0123456789'
digits_o = '23456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
lowercase_letters_o = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
uppercase_letters_o = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

quant_pw = int(input('Укажите количество паролей для генерации: '))
len_pw = int(input('Укажите длину пароля: '))
digit_pw = input('Включать ли цифры 012345678? Y или N: ')
upper_pw = input('Включать ли прописные буквы ABC...? Y или N: ')
low_pw = input('Включать ли строчные буквы abc...? Y или N: ')
char_pw = input('Включать ли символы !#$%&*+-=?@^_? Y или N: ')
neodn_pw = input('Включать ли неоднозначные символы !il1Lo0O? Y или N: ')

while quant_pw:
    print(*generate_password(len_pw), sep = '')
    quant_pw -= 1

