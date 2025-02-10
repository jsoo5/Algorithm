import sys
input = sys.stdin.readline

def gcd(int1, int2):
    a = max(int1, int2)
    b = min(int1, int2)

    if a % b == 0:    return b
    elif a % b == 1:  return 1
    else:             return gcd(b, a % b)

def sum_gcd(numbers):
    result = 0
    for i in range(1, numbers[0]):
        for j in range(i + 1, numbers[0] + 1):
            result += gcd(numbers[i], numbers[j]) 
    return result


t = int(input().strip())
for _ in range(t):
    n_list = list(map(int, input().split()))
    print(sum_gcd(n_list))
