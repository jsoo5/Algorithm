import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = [1] * n
d_prime = [1] * n

for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            d[i] = max(d[i], d[j] + 1)

for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if a[j] < a[i]:
            d_prime[i] = max(d_prime[i], d_prime[j] + 1)

result = 0
for i in range(n):
    result = max(result, d[i] + d_prime[i] - 1)
print(result)