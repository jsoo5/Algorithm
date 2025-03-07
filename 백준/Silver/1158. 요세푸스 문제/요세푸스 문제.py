import sys

N, K = map(int, sys.stdin.readline().split())
li = list(range(1, N+1))
bin = []

idx = 0
while li:
    idx = (idx + K - 1) % len(li)
    bin.append(li.pop(idx))
print(f'<{", ".join(map(str, bin))}>')