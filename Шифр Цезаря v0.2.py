# функция кодирования
def code_text(text, step, language):
    text_code = []
    #  сгенерируем алфавит для ru или eng из таблицы юникода
    if language == 2:
        abc = ''.join([chr(i) for i in range(97, 97 + 26)])
    else:
        abc = ''.join([chr(i) for i in range(1072, 1072 + 32)])  
    
    for a in text:
        if a.isalpha():
            flag_l = a == a.lower()         # запомним регистр буквы 
            index_abc = abc.find(a.lower())
            len_abc = len(abc)
            
            if index_abc + step < len_abc:  # буква + шаг не выходят за пределы последовательности
                a = abc[index_abc + step]
            else:                            # вышли за пределы алфавита, хвостик идет сначала
                a = abc[index_abc + step - len_abc]
            
            if flag_l:
                text_code.append(a)
            else:
                text_code.append(a.upper())
        else:
            text_code.append(a)              # шифр работает только для букв
    
    return text_code
# ##########################################################
# основной модуль программы
# ввод настроект
text_in = input('Укажите строку текста: ')

direction = input('Укажите направление: 1 - шифрование, 2 - дешифрование: ')
while not direction.isdigit():
    direction = input('Укажите ЧИСЛО: 1 шифрование, 2 - дешифрование: ')

language = input('Укажите язык алфавита: 1 - русский, 2 - английский: ')
while not language.isdigit():
    language = input('Укажите ЧИСЛО: 1 - русский, 2 - английский: ')
language = int(language)
step = input('Укажите число, т.е. на сколько букв сдвигаемся: ')
while not step.isdigit():
    step = input('Укажите ЧИСЛО для сдвига шифра: ')
step = int(step)

if int(direction) == 1:
    text_out = code_text(text_in, step, language)
elif int(direction) == 2:
    text_out = code_text(text_in, step * -1, language)
else:
    text_out = 'Неправильно указано направление шифрования / дешифрования!'

print(*text_out, sep='')
    
