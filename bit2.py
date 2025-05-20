def setornot(number, n):
    mask = 1
    if (n & mask ) == 1 or (n & mask) == 0:
        if number & (1 << (n - 1)):
            print("The bit is set")
        else:
            print("The bit is not set")
number = int(input("Enter a number: "))
n = int(input("Enter the bit position to check: "))
setornot(number, n)