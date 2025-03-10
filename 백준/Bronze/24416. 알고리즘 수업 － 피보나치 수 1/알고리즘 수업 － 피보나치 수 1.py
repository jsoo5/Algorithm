import sys
input = sys.stdin.readline

memo = {}

def fib(n):
    if n == 1 or n == 2:
        return 1  # 코드1
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
    
n = int(input())
print(fib(n), n - 2)