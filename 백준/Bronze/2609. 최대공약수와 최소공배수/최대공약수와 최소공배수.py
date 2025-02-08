import sys

def calc_gcd_n_lcm(int1, int2):
    bigger = max(int1, int2)
    smaller = min(int1, int2)
    remainder = bigger % smaller

    if remainder == 0:
        return smaller, a * b // smaller
    
    elif remainder == 1:
        return 1, a * b
    
    else:
        return calc_gcd_n_lcm(smaller, remainder)
    
a, b = map(int, sys.stdin.readline().strip().split())
gcd, lcm = calc_gcd_n_lcm(a, b)

print(f'{gcd}\n{lcm}')