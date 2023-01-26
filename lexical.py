import mark_keywords as mk  # будем проверять на использование слов из pascal

def lexical(data):
    f = True
    if (type(data)==bool):
        f = False
        return f
    ans = [('', None)]  # название лексемы '' none- класс лексемы

    def addKey(Symbol, typeName):
        if ans[-1][1] == typeName:  # если последний эл-т массива равен тек.классу, то в последний эл-т вносим
            ans[-1] = (ans[-1][0] + Symbol, ans[-1][1])
        else:
            ans.append((Symbol, typeName))

    tek = 'Start'
    for sym in data:
        if tek == 'Start':
            if sym[1] == 'Letter':
                tek = 'Keyword'
                addKey(sym[0], 'Keyword')
            elif sym[1] == 'Space':
                tek = 'Start'
                ans.append((' ', 'Space'))
            else:
                f = False
                break

        elif tek == 'Keyword':
            if sym[1] == 'Letter' or sym[1] == 'Number':
                tek = 'Keyword'
                addKey(sym[0], 'Keyword')
            elif sym[1] == 'Space':
                tek = 'Space1'
                ans.append((' ', 'Space'))
            else:
                f = False  # программа не прерывается, переходит к самому первому if
                break

        elif tek == 'Space1':
            if sym[1] == 'Letter':
                tek = 'Name'
                addKey(sym[0], 'identificator')
            elif sym[1] == 'Space':
                tek = 'Space1'
                ans.append((' ', 'Space'))
            else:
                f = False
                break

        elif tek == 'Name':
            if sym[1] == 'Letter' or sym[1] == 'Number':
                tek = 'Name'
                addKey(sym[0], 'identificator')
            elif sym[1] == 'Space':
                tek = 'Space2'
                if mk.mark_keywords(ans[-1][0]):
                    f = False
                    break
                ans.append((' ', 'Space'))
            elif sym[1] == 'Comma':
                tek = 'Space2'
                if mk.mark_keywords(ans[-1][0]):
                    f = False
                    break
                ans.append((',', 'Comma'))
            elif sym[1] == 'Colons':
                tek = 'Colons'
                if mk.mark_keywords(ans[-1][0]):
                    f = False
                    break
                addKey(sym[0], 'Colons')
            else:
                f = False
                break

        elif tek == 'Space2':
            if sym[1] == 'Letter':
                tek = 'Name'
                addKey(sym[0], 'identificator')
            elif sym[1] == 'Colons':
                tek = 'Colons'
                addKey(sym[0], 'Colons')
            elif sym[1] == 'Space':
                tek = 'Space2'
                ans.append((' ', 'Space'))
            else:
                f = False
                break

        elif tek == 'Colons':
            if sym[1] == 'Letter':
                tek = 'Standard_type'
                addKey(sym[0], 'Standard_type')
            elif sym[1] == 'Space':
                tek = 'Colons'
                ans.append((' ', 'Space'))
            else:
                f = False
                break

        elif tek == 'Standard_type':
            if sym[1] == 'Letter':
                tek = 'Standard_type'
                addKey(sym[0], 'Standard_type')
            elif sym[1] == 'Space':
                tek = 'Space3'
                ans.append((' ', 'Space'))
            elif sym[1] == 'Leftbracket':
                tek = 'Leftbracket'
                addKey(sym[0], 'Leftbracket')
            elif sym[1] == 'Semicolon':
                tek = 'Semicolon'
                addKey(sym[0], 'Semicolon')
            else:
                f = False
                break

        elif tek == 'Space3':
            if sym[1] == 'Space':
                tek = 'Space3'
                ans.append((' ', 'Space'))
            elif sym[1] == 'Leftbracket':
                tek = 'Leftbracket'
                addKey(sym[0], 'Leftbracket')
            elif sym[1] == 'Semicolon':
                tek = 'Semicolon'
                addKey(sym[0], 'Semicolon')
            else:
                f = False
                break

        elif tek == 'Leftbracket':
            if sym[1] == 'Number':
                tek = 'Int'
                addKey(sym[0], 'Int')
            elif sym[1] == 'Space':
                tek = 'Leftbracket'
                ans.append((' ', 'Space'))
            else:
                f = False
                break

        elif tek == 'Int':
            if sym[1] == 'Number':
                tek = 'Int'
                addKey(sym[0], 'Int')
            elif sym[1] == 'Rightbracket':
                tek = 'Rightbracket'
                addKey(sym[0], 'Rightbracket')
            else:
                f = False
                break

        elif tek == 'Space4':
            if sym[1] == 'Space':
                tek = 'Space4'
                ans.append((' ', 'Space'))
            elif sym[1] == 'Rightbracket':
                tek = 'Rightbracket'
                addKey(sym[0], 'Rightbracket')
            elif sym[1] == 'Semicolon':
                tek = 'Semicolon'
                addKey(sym[0], 'Semicolon')
            else:
                f = False
                break

        elif tek == 'Rightbracket':
            if sym[1] == 'Space':
                tek = 'Space4'
                ans.append((' ', 'Space'))
            elif sym[1] == 'Semicolon':
                tek = 'Semicolon'
                addKey(sym[0], 'Semicolon')
            else:
                f = False
                break

        elif tek == 'Semicolon':
            if sym[1] == 'Space':
                tek = 'Semicolon'
                ans.append((' ', 'Space'))
            else:
                f = False
                break
        # print(tek,f)

    if sym[-1] != 'Semicolon':
        f = False
    if (not(f)):
        return f
    return ans[1:]