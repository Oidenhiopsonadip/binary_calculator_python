import os
import importlib
from time import sleep

if os.name == 'posix':
    clear = 'clear'
elif os.name == 'nt':
    clear = 'cls'

files = dict(zip(range(len(os.listdir('.'))), (x for x in os.listdir('.') if x.endswith('.py') if x != 'main.py')))
modules = {}

count = 0
os.system(clear)
print('Successfully Imported Modules: ')
for file in files.values():
    count += 1
    modules[count] = importlib.import_module(file[:len(file) - 3])
    if count % 2 != 0:
        print(str(count) + '. ' + file[:len(file) - 3], sep='', end='')
        for x in range(20 - (len(file) - 3)):
            print(' ', end='', sep='')
    elif count % 2 == 0:
        print(str(count) + '. ' + file[:len(file) - 3], sep=None, end=None)

def printModules():
    count = 0
    for file in files.values():
        count += 1
        if count % 2 != 0:
            print(str(count) + '. ' + file[:len(file) - 3], sep='', end='')
            for x in range(20 - (len(file) - 3)):
                print(' ', end='', sep='')
        elif count % 2 == 0:
            print(str(count) + '. ' + file[:len(file) - 3], sep=None, end=None)


if __name__ == '__main__':
    while True:
        os.system(clear)
        printModules()
        UserInput = input('\n : ')
        try:
            UserInput = int(UserInput)
        except:
            pass
        if UserInput in modules.keys():
            modules[UserInput].main()
        else:
            print('Invalid')
            sleep(1)