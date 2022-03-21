from Defs import Functions

def fileExists(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createFile(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('\033[1:31mError on file creation.\033[m')
    else:
        print(f'File {name} successfully created.')


def readFile(name):
    try:
        a = open(name, 'rt')
    except:
        print('\033[1:31mError on reading file.\033[m')
    else:
        Functions.header('REGISTERED PEOPLE')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} year(s)')
    finally:
        a.close()


def register(arq, name='Unknown', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[1:31mError on opening file.\033[m')
    else:
        try:
            a.write(f'{name};{idade}\n')
        except:
            print('\033[1:31mError on data writing.\033[m')
        else:
            print(f'New register {name} has been added.')
            a.close()
