import sys
input = sys.stdin.readline

n = int(input())
mod = 15746

d = [0] * max(3, n+1)
d[1] = 1
d[2] = 2

if n > 2:
    for i in range(3, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % mod
print(d[n])