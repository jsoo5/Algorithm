import sys

a, b = map(int, sys.stdin.readline().split())
p, q= b - a, b

if q % p == 0:
    p //= p
    q //= p

print(p, q)