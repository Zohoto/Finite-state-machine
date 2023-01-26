def translit():

    f = True
    string = open('input.txt', 'r').read()
    Transliterator = dict()  # создаем словарь со всеми названиями символов
    for e in range(ord('A'), ord('Z') + 1):
        Transliterator[chr(e)] = 'Letter'
    for e in range(ord('a'), ord('z') + 1):
        Transliterator[chr(e)] = 'Letter'
    for e in range(ord('0'), ord('9') + 1):
        Transliterator[chr(e)] = 'Number'
    Transliterator[' '] = 'Space'
    Transliterator[';'] = 'Semicolon'
    Transliterator[':'] = 'Colons'
    Transliterator['['] = 'Leftbracket'
    Transliterator[']'] = 'Rightbracket'
    Transliterator[','] = 'Comma'
    ans = []
    for i in string:
        if i in Transliterator:
            ans.append((i, Transliterator[i])) # подписываем все символы из считываемого файла
        else:
            f = False
            ans.append((i, 'Error'))
            break
    if (not(f)):
        return f
    return ans