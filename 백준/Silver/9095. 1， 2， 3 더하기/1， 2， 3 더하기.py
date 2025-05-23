import sys
input = sys.stdin.readline

T = int(input())
MAX_N = 11
d = [0] * MAX_N
d[1] = 1
d[2] = 2
d[3] = 4

for _ in range(T):
    n = int(input())
    for i in range(4, n+1):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]
    print(d[n])