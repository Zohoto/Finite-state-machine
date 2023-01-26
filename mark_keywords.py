def mark_keywords(alphabet):
    pascal = ['and', 'end', 'nil', 'set', 'array', 'file', 'not', 'then', 'begin', 'for', 'of', 'to', 'case',
              'function', 'or', 'type', 'const', 'goto', 'packed', 'until', 'div', 'if', 'procedure', 'var',
              'do', 'in','program', 'while', 'downto', 'label', 'record', 'with', 'else', 'mod', 'repeat']
    pascal.sort()

    mid = len(pascal) // 2
    low = 0
    high = len(pascal) - 1

    while pascal[mid] != alphabet and low <= high:
        if alphabet > pascal[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return False
    else:
        print('"%s" is keywords' %alphabet)
        return True