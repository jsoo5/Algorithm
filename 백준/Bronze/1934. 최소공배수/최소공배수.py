import sys

def calc_lcm(a, b):

    bigger = max(a, b)
    smaller = min(a, b)

    while bigger % smaller > 1:
        remainder = bigger % smaller
        
        bigger = smaller
        smaller = remainder
    
    if bigger % smaller == 0:
        print(a * b // smaller)
    else:
        print(a * b)


T = int(sys.stdin.readline().strip())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    calc_lcm(a, b)