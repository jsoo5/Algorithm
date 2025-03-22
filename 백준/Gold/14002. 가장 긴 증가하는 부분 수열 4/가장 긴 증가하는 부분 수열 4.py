import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = [1] * n
b = []

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j] + 1)
print(max(d))

max_idx = d.index(max(d))
count = max(d)
for k in range(max_idx, -1, -1):
    if  d[k] == count:
        b.append(a[k])
        count -= 1

b.reverse()
print(*b, sep=' ')