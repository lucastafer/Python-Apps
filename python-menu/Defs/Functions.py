def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def line(tam=42):
    return '\033[1:36m-' * tam


def menu(lista):
    header('MENU')
    c = 1
    for item in lista:
        print(f'\033[1:97m{c} - {item}\033[m')
        c += 1
    print(line())
    choice = readInt('\033[1:32mYour option: \033[m')
    return choice


def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1:31mError: please input a valid integer.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1:31mUser preferred not to type.')
            return 0
        else:
            return n
