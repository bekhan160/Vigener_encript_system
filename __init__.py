alf = 'abcdefghijklmnopqrstuvwxyz'


def vig(text='', key='', typee='d'):
    if not text:
        print('Введите текст для шифровки')
        return
    if not key:
        print('Введите ключ')
        return
    if typee.lower() not in ('d', 'e'):
        print('Введите D или Е')
        return
    elif typee.lower() == 'd':
        decript = True
    else:
        decript = False
    for letter in text:
        if letter in alf:
            print(chr(ord(letter)))


vig(text='bekhan rayamjanov', key='ray', typee='d')
