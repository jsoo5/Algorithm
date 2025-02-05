import sys

def gcd(a, b):
    max_int = max(a, b)
    min_int = min(a, b)
    
    a = max_int - min_int
    b = min_int
    return a, b

a, b = map(int, sys.stdin.readline().split())
calc_cnt = 0

while a != b:
    a, b = gcd(a, b)
    calc_cnt += 1

print(calc_cnt)