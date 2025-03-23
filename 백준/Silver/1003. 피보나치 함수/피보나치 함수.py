import sys
input = sys.stdin.readline

memo = {}

def fibonacci(n):    
    memo[0] = 0
    memo[1] = 1
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]
    
T = int(input())
for _ in range(T):
    n = int(input())
    
    fibonacci(n)
    if n == 0:
       print(1, 0)
    else:
        print(memo[n - 1], memo[n])
