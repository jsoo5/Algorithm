import sys
input = sys.stdin.readline

N = int(input())
T = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
loser = []

i = 0
for j in range(T):
    i = (i + b[j] - 1) % len(a)
    loser.append(a[i])
print(*loser, sep=' ')