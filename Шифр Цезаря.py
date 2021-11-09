# функция кодирования
def code_text(text, step, max_code, count_code):
    text_code = []
    
    for a in text:
        a_ord = ord(a)  # узнаем код символа
        if a.isalpha():
            if a == a.lower():  # для маленьких букв
                # для маленьких русских букв смещение максимальное будет 1103 - я
                # для маленьких английских букв смещение максимальное будет 122 - z
                if ord(a) + step <= max_code:
                    a = ord(a) + step
                else:
                    step = ord(a) + step - max_code
                    a = max_code - count_code + step  # последняя буква алфавита - количество букв
                text_code.append(chr(a))
            
            elif a == a.upper():  # для больших букв
                # последняя буква маленького регистра - количество букв = последняя буква большого регистра
                if ord(a) + step <= max_code - count_code:
                    a = ord(a) + step
                else:
                    step = ord(a) + step - max_code
                    a = max_code - count_code + step  # последняя буква маленького регистра - количество букв * 2
                text_code.append(chr(a))        
        else:
            text_code.append(a)
    
    return text_code

# функция декодирования
def decode_text(text, step):
    text_code = []
    for a in text:
        if a.isalpha():
            a = ord(a) - step
            text_code.append(chr(a))
        else:
            text_code.append(a)
    return text_code

#text = input('Укажите строку текста: ')
#direction = input('Укажите направление: 1 - шифрование, 2 - дешифрование: ')
#language = input('Укажите язык алфавита: 1 - русский, 2 - английский: ') 
#step = input('Укажите число, т.е. на сколько букв сдвигаемся: ')

text_in = 'Z!'
direction = 1
language = 2
if language == 1:
    max_code = 1103  # код буквы я
    count_code = 32  # количество букв 
elif language == 2:
    max_code = 122   # код буквы z
    count_code = 26  # количество букв

step = 1

ABC = [chr(i) for i in range(65, 65 + 26)]
abc = [chr(i) for i in range(97, 97 + 26)]
ABC_ru = [chr(i) for i in range(1040, 1040 + 32)]
abc_ru = [chr(i) for i in range(1072, 1072 + 32)]

if direction == 1:
    text_out = code_text(text_in, step, max_code, count_code)
elif direction == 2:
    text_out = decode_text(text_in, step)
else:
    text_out = 'Неправильно указано направление шифрования / дешифрования!'

print(*text_out, sep='')
    
