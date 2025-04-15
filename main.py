import time
from pyfiglet import Figlet
import os
import random

h = ('+------------------------------------------------------------+\n'
     '|  help - all commands                                       |\n'
     '|  cls - clearing console                                    |\n'
     '|  echo - prints text ex.: echo text                         |\n'
     '|  echo text > file.txt - writes "text" to file.txt          |\n'
     '|  crypter(-h / --help) - starts encrypter                   |\n'
     '|  ls - show what is in the current directory                |\n'
     '|  touch file.txt - creates file with name "file.txt"        |\n'
     '|  cat file - prints file                                    |\n'
     '|  using flags tutorial: "command -f"  or  "command --flag"  |\n'
     '+------------------------------------------------------------+\n')

def commands(c, oss):
    if c:
        if c == 'help':
            print(h)
        elif c.startswith('echo'):
            print(c[c.find(' ')+1:])
            if c[c.find(' ')+1:].startswith('>'):
                if oss == '1':
                    os.system(f'echo "{c[c.find(' ')+1:c.find('>')-1]}" > {c[c.find('>')+2:]}')
                elif oss == '2':
                    os.system(f'echo {c[c.find(' ')+1:c.find('>')-1]} > {c[c.find('>')+2:]}')
        elif c == ('cls'):
            if oss == '1':
                os.system('clear')
            elif oss == '2':
                os.system('cls')
        elif c == 'crypter':
            crypter()
        elif c.startswith('crypter') and c[c.find(' ')+1:] == '-h' or c.startswith('crypter') and c[c.find(' ')+1:] == '--help':
            print('How it works:\n'
              '1. Outputs a one-time key\n'
              '2. Asks if you want to decrypt/encrypt the text/file\n'
              '3. Outputs the result and saves it to a text file in the folder with this code. If you need to decrypt it, then you need the key that was used to encrypt it.\n\n'
              'No libraries installing needed)\n'
              'There is also a list of allowed characters at the very beginning, which you can change.\n')
        elif c == 'ls':
            if oss == '1':
                os.system('ls')
            elif oss == '2':
                os.system('dir')
        elif c.startswith('touch'):
            f = c[c.find(' ')+1:]
            if oss == '1':
                os.system(f'touch {f}')
            elif oss == '2':
                os.system(f'NUL> {f}')
        elif c.startswith('cat'):
            f = c[c.find(' ')+1:]
            if oss == '1':
                os.system(f'cat {f}')
            elif oss == '2':
                os.system(f'type {f}')
        else:
            print('err:wrong command/flag')

def start():
    oss = input('Your OS: \n'
                '1. Linux\n'
                '2. Windows\n'
                '3. Quit\n'
                '\n'
                '<Unity> Your choice(1/2/3): ')
    if oss != '1' and oss != '2':
        exit()
    else:
        s = Figlet(font='standard')
        print(s.renderText('Starting Unity'))
        print('Wait, please...')
        time.sleep(3)
        if oss == '1':
            os.system('clear')
        elif oss == '2':
            os.system('cls')
    return oss


def crypter():
    lst = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',
           'v', 'b', 'n', 'm',
           'й', 'ц', 'у', 'к', 'е', 'н', 'ё', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д',
           'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю',
           '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '&', '*', '%', '-', '_', '+', '=', '?', '.',
           ',', ' ']

    lst2 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
            'c', 'v', 'b', 'n', 'm',
            'й', 'ц', 'у', 'к', 'е', 'н', 'ё', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л',
            'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '&', '*', '%', '-', '_', '+', '=', '?',
            '.', ',', ' ']
    hsh = {}
    unhsh = {}
    hsh_key = ''

    for i in lst:
        a = random.choice(lst2)
        hsh[i] = a
        unhsh[a] = i
        lst2.remove(a)

    for k, v in hsh.items():
        hsh_key = hsh_key + v

    print('Try not to use it in Windows terminal!')
    print('YOUR KEY IS:', hsh_key)
    print('SAVE IT')

    # ===========================

    n = input('Crypt/encrypt(c/e)?: ')

    if n == 'c':
        n = input('File or text(f/t)?: ')

        if n == 't':
            n = input('Input text: ')
            n = n.lower()
        elif n == 'f':
            n = input("Ful path to file: ")
            file = open(n, 'r')
            n = file.read()
            file.close()
        else:
            print('BAD!!!')
            exit()

        for i in n:
            if i not in lst:
                n = n.replace(i, '')
            else:
                n = n.replace(i, hsh[i], 1)

        try:
            file = open('crypted.txt', 'x')
            file.close()
            file = open('crypted.txt', 'w')
            file.write(n)
            file.close()
        except:
            file = open('crypted.txt', 'w')
            file.write(n)
            file.close()

        print(f'Text saved to crypted.txt\nOutput: {n}')

    elif n == 'e':
        hsh_key = input('Your key: ')
        unhsh = {}
        c = 0

        n = input('File or text(f/t)?: ')

        if n == 't':
            n = input('Input text: ')
            n = n.lower()
        elif n == 'f':
            n = input("Full path file: ")
            file = open(n, 'r')
            n = file.read()
            file.close()
        else:
            print('BAD!!!')
            exit()

        for i in lst:
            if hsh_key[c] not in lst:
                hsh_key = hsh_key.replace(hsh_key[c], '')
            else:
                unhsh[hsh_key[c]] = i
                c += 1

        for i in n:
            if i not in lst:
                n = n.replace(i, '')
            else:
                n = n.replace(i, unhsh[i], 1)

        try:
            file = open('encrypted.txt', 'x')
            file.close()
            file = open('encrypted.txt', 'w')
            file.write(n)
            file.close()
        except:
            file = open('encrypted.txt', 'w')
            file.write(n)
            file.close()

        print(f'Text saved to encrypted.txt\nOutput: {n}')

    else:
        print('BAD!!!')



def main():
    oss = start()
    while True:
        c = input('<Unity>: ')
        c = c.lower()
        c = c.strip()
        commands(c, oss)

main()
