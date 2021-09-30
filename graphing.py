def printScreen(xlist, ylist, rnge):
    for y in range(rnge):
        y = -(y - (rnge / 2))
        for x in range(rnge):
            x = (x - (rnge / 2))
            if x == 0 and y == 0:
                print('0 ', end='', sep='')
            elif (x, y) in list(zip(xlist, ylist)):
                print('@ ', end='', sep='')
            else:
                print('. ', end='', sep='')
        print('')





def main():
    UserInput = input(' y=').lower()
    rnge = input(' Enter Range of Graph: ')
    UserInput.replace(' ', '')
    try:
        rnge = int(rnge)
    except:
        return 0
    ylist = []
    xlist = []
    x = -(rnge / 2)
    y = 0
    UserInput = UserInput.replace('y', '')
    UserInput = UserInput.replace('=', '')
    UserInput = UserInput.replace(' ', '')
    for j in range(rnge):
        equate = UserInput
        for i in equate:
            if i == 'x':
                i = x
        y = eval(equate)
        ylist.append(int(y))
        xlist.append(int(x))
        print('x = ' + str(x) + '   y = ' + str(y))
        x += 1
    printScreen(xlist, ylist, rnge)






if __name__ == '__main__':
    main()