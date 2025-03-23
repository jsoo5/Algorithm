import sys
input = sys.stdin.readline

MAX_N = 41
fib = [(0, 1)] * MAX_N
fib[0] = (1, 0)
fib[1] = (0, 1)
    
T = int(input())
for _ in range(T):
    n = int(input())

    for i in range(2, n + 1):
        fib[i] = (fib[i - 1][0] + fib[i - 2][0], fib[i - 1][1] + fib[i - 2][1])
    print(fib[n][0], fib[n][1])