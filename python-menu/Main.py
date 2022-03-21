from Defs import Functions
from Defs import File
from time import sleep

arq = 'File.txt'

if not File.fileExists(arq):
    File.createFile(arq)

while True:
    answer = Functions.menu(['View registered people', 'Register new person', 'Get out System'])
    if answer == 1:
        File.readFile(arq)
    elif answer == 2:
        Functions.header('NOVO CADASTRO')
        name = str(input('Name: ')).title()
        age = Functions.readInt('Age: ')
        File.register(arq, name, age)
    elif answer == 3:
        Functions.header('Turning off...')
        sleep(2)
        Functions.header('Bye!')
        break
    else:
        print('\033[31mErro: digite uma opção válida.\033[m')
