info = "Program that creates the fibonacci sequence with user input for the amount of cycles and the starting number"

def main():
    num1 = num2 = input('Enter Starting Number: ')
    cycles = input('Enter Number of cycles: ')
    printCycles = input('Enter 1 to print every cycle: ')
    try:
        num1 = int(num1)
        num2 = int(num2)
        cycles = int(cycles)
        if printCycles == '1':
            print(num1)
            num1 += num2
            num3 = 0
            for x in range(cycles - 1):
                print(num1)
                num3 = num1
                num1 += num2
                num2 = num3
        else:
            num3 = 0
            for x in range(cycles):
                num3 = num1
                num1 += num2
                num2 = num3
            print(num1)
    except:
        return 0
    

if __name__ == '__main__':
    main()