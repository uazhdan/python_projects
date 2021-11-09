
def only_char(text):
    result = ''
    for i in text:
        if i.isalpha():
            result += i
    return result


text_in = 'Day, mice. "Year" is a mistake!'.split()
for word in text_in:
    print(len([i for i in word if i.isalpha()]))
    print(len(only_char(word)))