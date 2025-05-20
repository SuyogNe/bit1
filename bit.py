def numberOfBits(n):
    ones=0
    zeroes=0
    while (n):
        if (n & 1 == 1):
            ones += 1
        else:
            zeroes += 1
        n >>= 1
    print("Number of 1's: ", ones)
    print("Number of 0's: ", zeroes)

number=int(input("Enter a number: "))
numberOfBits(number)