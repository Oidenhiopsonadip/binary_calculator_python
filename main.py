from os import listdir

files = dict(zip(range(len(listdir('.'))), (file for file in os.listdir('.') if file.endswith('.py') if file != 'main.py'))

if os.name == 'posix':
    clear = 'clear'
elif os.name == 'nt':
    clear = 'cls'
    

""" if __name__ == '__main__':
    cont = False
    while True:
        if cont == True and input(' Input 1 to Continue Running Program:') != '1':
            exit(0)
        cont = True
        os.system(clear)
        print(' 1. Default Calculator             2. Fibonacci Sequence')
        commandRouter[input(' : ')]() """