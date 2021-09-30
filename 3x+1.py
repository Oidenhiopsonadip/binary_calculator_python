def main():
    try:
        UserInput = int(input('Enter Starting Number: '))
        showCycles = input('Enter 1 to Show Cycles: ')
    except:
        return 0
    count = 0
    if showCycles == '1':
        while True:
            print(UserInput)
            if UserInput == 1:
                break
            elif UserInput % 2 == 0:
                UserInput /= 2
            elif UserInput % 2 != 0:
                UserInput *= 3
                UserInput += 1
            count += 1
    else:
        while True:
            if UserInput == 1:
                break
            elif UserInput % 2 == 0:
                UserInput /= 2
            elif UserInput % 2 != 0:
                UserInput *= 3
                UserInput += 1
    print('\ncycles until 1: ' + str(count))

if __name__ == '__main__':
    main()