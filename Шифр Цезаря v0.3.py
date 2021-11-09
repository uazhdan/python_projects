# функция кодирования
def code_text(text):
    text_code = []
    #  сгенерируем алфавит eng из таблицы юникода
    abc = ''.join([chr(i) for i in range(97, 97 + 26)])
    for word in text:
        step = len([i for i in word if i.isalpha()])
        for a in word:
            if a.isalpha():
                flag_l = a == a.lower()  # запомним регистр буквы
                index_abc = abc.find(a.lower())
                len_abc = len(abc)

                if index_abc + step < len_abc:  # буква + шаг не выходят за пределы последовательности
                    a = abc[index_abc + step]
                else:  # вышли за пределы алфавита, хвостик идет сначала
                    a = abc[index_abc + step - len_abc]

                if flag_l:
                    text_code.append(a)
                else:
                    text_code.append(a.upper())
            else:
                text_code.append(a)  # шифр работает только для букв
        text_code.append(' ')
    return text_code


# ##########################################################
# основной модуль программы
# ввод настроект
text_in = input('Укажите строку текста: ').split()
text_out = code_text(text_in)

print(*text_out, sep='')