"""У заданому рядку символів визначити кількість слів,
довжина яких більша за вказану користувачем."""


def clear(word):
    separators = ',:.-,\''
    if word.startswith(tuple(separators)): # Удаление лишних символов (',', ':', '.', '-', '\'')
        word = word[1:]                       # C начала строки 
    elif word.endswith(tuple(separators)):
        word = word[0:-1]                   # Удаление лишних символов (',', ':', '.', '-', '\'')
    return word                                  # C конца строки


def word_counter(string, n):
    separators = ',:.-'
    for i in string:
        if i in separators:
            string.replace(i,' ')
    word_list = []
    for word in string.split():
        if len(clear(word)) < n:                                          
            word_list.append(word)               
    return len(word_list), word_list
            
if __name__ == '__main__':
    d = word_counter("John's mom went there, but he wasn't there. So she said: 'Where are you'",5)
    print(d)
    
            
            
