import os
import importlib
from time import sleep

builtinoptions = ('Exit*', 'Info*')

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

def printModules(options=False):
    count = 0
    for file in files.values():
        count += 1
        if count % 2 != 0:
            print(str(count) + '. ' + file[:len(file) - 3], sep='', end='')
            for x in range(20 - (len(file) - 3)):
                print(' ', end='', sep='')
        elif count % 2 == 0:
            print(str(count) + '. ' + file[:len(file) - 3], sep=None, end=None)
    if options:
        for x in builtinoptions:
            count += 1
            if count % 2 != 0:
                print(str(count) + '. ' + x, sep='', end='')
                for y in range(20 - len(x)):
                    print(' ', sep='', end='')
            elif count % 2 == 0:
                print(str(count) + '. ' + x, sep=None, end=None)



if __name__ == '__main__':
    cont = False
    while True:
        if cont and input(' Enter 1 to Continue: ') == 1:
            pass
        os.system(clear)
        printModules(True)
        try:
            UserInput = int(input('\n : '))
        except:
            pass

        if UserInput in modules.keys():
            cont = True
            if modules[UserInput].main() == 0:
                print('Invalid')
        elif UserInput == (len(modules) + 1):
            exit(0)
        elif UserInput == (len(modules) + 2):
            os.system(clear)
            print('This is a completely modular python program for all of your calculation needs\n')
            for x in modules:
                print()
            input()
        else:
            print('Invalid')
            sleep(1)