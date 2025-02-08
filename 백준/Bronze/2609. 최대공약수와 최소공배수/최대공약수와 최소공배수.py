import sys

def calc_gcd_n_lcm(int1, int2):
    bigger = max(int1, int2)
    smaller = min(int1, int2)

    if bigger % smaller == 0:
        return smaller, a * b // smaller
    
    elif bigger % smaller == 1:
        return 1, a * b
    
    else:
        return calc_gcd_n_lcm(smaller, bigger % smaller)
    
a, b = map(int, sys.stdin.readline().strip().split())
gcd, lcm = calc_gcd_n_lcm(a, b)

print(f'{gcd}\n{lcm}')