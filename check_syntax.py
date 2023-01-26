def check_syntax(key):
    types = ['integer', 'boolean', 'byte', 'char', 'longint', 'real', 'string']

    def writes(f):
        ofile = open('output.txt', 'w')
        if type(f) == str:
            ofile.write(f)
        else:
            if f:
                ofile.write("ACCEPT")
            else:
                ofile.write("REJECT")
        ofile.close()

    if (type(key) == bool):
        writes(False)
        return
    tek = 'start'
    for e in key:

        if tek == 'start':
            if e[1] == 'Keyword':
                tek = 'Keyword'
                if (not(e[0].lower() == 'var')):
                    writes(False)
                    break
            else:
                writes(False)
                break
        elif tek == 'Keyword':
            if e[1] == 'identificator':
                tek = 'Name'
            elif e[1] == 'Space':
                tek = 'Name'
            else:
                writes(False)
                break
        elif tek == 'Name':
            if e[1] == 'Keyword':
                tek = 'Name'
            elif e[1] == 'Colons':
                tek = 'Colons'
            elif e[1] == 'identificator':
                tek = 'Name'
            elif e[1] == 'Comma':
                tek = 'Name'
            elif e[1] == 'Space':
                tek = 'Name'
            else:
                writes(False)
                break
        elif tek == 'Colons':
            if ((e[1] == 'Standard_type' and e[0].lower() in types) and e[0].lower =='string'):
                tek = 'Standard_type'
            elif ((e[1] == 'Standard_type' and e[0].lower() in types) and not(e[0].lower =='string')):
                tek = 'Standard_type'
            elif e[1] == 'Space':
                tek = 'Colons'
            else:
                writes(False)
                break
        elif tek == 'Standard_type':
            if e[1] == 'Leftbracket':
                tek = 'Leftbracket'
            elif e[1] == 'Semicolon':
                tek = 'Semicolon'
                writes(True)
                break
            else:
                writes(False)
                break
        elif tek == 'Leftbracket':
            if e[1] == 'Int':
                tek = 'Int'
            else:
                writes(False)
                break
        elif tek == 'Int':
            if e[1] == 'Rightbracket':
                tek = 'Rightbracket'
            else:
                writes(False)
                break
        elif tek == 'Rightbracket':
            if e[1] == 'Semicolon':
                tek = 'Semicolon'
                writes(True)
                break
            elif e[1] == 'Leftbracket':
                tek = 'Leftbracket'
            else:
                writes(False)
                break