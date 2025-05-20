def num(n):
    count = 0
    while (n):
        count += 1
        n >>= 1
        print(count,"count loops")
    return count
n=int(input("Enter a number: "))
print(num(n))