def fibPrintCycle(num1, num2, cycles):
    print(num1)
    num1 += num2
    num3 = 0
    for x in range(cycles - 1):
        print(num1)
        num3 = num1
        num1 += num2
        num2 = num3

def fib(num1, num2, cycles):
    num3 = 0
    for x in range(cycles):
        num3 = num1
        num1 += num2
        num2 = num3
    print(num1)

def main():
    num1 = num2 = input('Enter Starting Number: ')
    cycles = input('Enter Number of cycles: ')
    printCycles = input('Enter 1 to print every cycle: ')
    try:
        num1 = int(num1)
        num2 = int(num2)
        cycles = int(cycles)
        if printCycles == '1':
            fibPrintCycle(num1, num2, cycles)
        else:
            fib(num1, num2, cycles)
    except:
        return 0
    

if __name__ == '__main__':
    main()

# 3 2 2
# 1 2 3 