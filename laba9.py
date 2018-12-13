"""У заданому рядку символів визначити кількість слів,
довжина яких більша за вказану користувачем."""


def word_counter(string, n):
    separators = ',:.-'
    for i in string:
        if i in separators:
            string.replace(i,' ')
    separators += "'"
    word_list = []
    for i in string.split():
        if len(i) < n:            
            if i.startswith(tuple(separators)): # Удаление лишних символов (',', ':', '.', '-', '\'')
                i = i[1:]                       # C начала строки 
            elif i.endswith(tuple(separators)):
                i = i[0:-1]                   # Удаление лишних символов (',', ':', '.', '-', '\'')
            word_list.append(i)               # C конца строки
    return len(word_list), word_list


if __name__ == '__main__':
    d = word_counter("John's mom went there, but he wasn't there. So she said: 'Where are you'",5)
    print(d)
    
            
            
