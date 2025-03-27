import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = [0] * n

for i in range(n):
    d[i] = max(a[i], d[i - 1] + a[i])
print(max(d))