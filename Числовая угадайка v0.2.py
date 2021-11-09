# функции
def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100

def games():
    count = 0
    print('Число находится в интервале от 1 и до границы, которую выберет игрок')
    print('Выберите границу интервала')
    end = int(input())
    x = randint(1, end)
    #print('Подсказка', x)
    print('Введите число')

    while True:
        num = input('Попробуйте угадать число от 1 до ' + str(end) + ' ')
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

# основной код
from random import randint
print('Добро пожаловать в числовую угадайку')
games()
while True:
    print('Спасибо, что играли в числовую угадайку. Хотите еще поиграть? Тогда нажмите Y')
    a = input()
    if a == 'Y':
        games()
    else:
        print('До свидания!')
        break
