import math
n = int(input())

def isPrime(n):
    if n < 2:
        return False
       
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0:
            return False
    return True

while True:
    if str(n) == str(n)[::-1]:
        if isPrime(n):
            print(n)
            break
    n += 1