from random import randint
x = randint(0, 100)
count = 0
print('Добро пожаловать в числовую угадайку')
print('Введите число')

def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100

while True:
    num = input('Попробуйте угадать число от 1 до 100: ')
    count += 1
    if is_valid(num):
        num = int(num)
        if num < x:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif num > x:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print('Ваше число попыток угадать число =', count)
            break
    else:
        print('А может введем целое число от 1 до 100?')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')