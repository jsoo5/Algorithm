import sys
input = sys.stdin.readline

def calc_iter(r1, r2):

    def calc_gcd(a, b):
        if a % b == 0:
            return b
        elif a % b == 1:
            return 1
        else:
            return calc_gcd(b, a % b)
    
    gcd = calc_gcd(r1, r2)
    return r1 // gcd, r2 // gcd

N = int(input().strip())
rings = list(map(int, input().split()))

for i in range(1, N):
    result = calc_iter(rings[0], rings[i])
    print(*result, sep='/')