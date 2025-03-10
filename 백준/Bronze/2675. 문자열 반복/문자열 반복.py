import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    r, s = input().split()
    p = ''
    for ch in s:
        p += ch * int(r)
    print(p)