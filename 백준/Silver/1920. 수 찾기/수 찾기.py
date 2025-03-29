import sys
input = sys.stdin.readline

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = tuple(map(int, input().split()))

for i in range(m):
    if b[i] in a:
        print(1)
    else:
        print(0)