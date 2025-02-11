import sys
input = sys.stdin.readline

def calc_divisor(a, b):
    if a % b == 0:
        return b
    elif a % b == 1:
        return 1
    else:
        return calc_divisor(b, a % b)

fr1 = list(map(int, input().split()))
fr2 = list(map(int, input().split()))

fr_sum = [fr1[0] * fr2[1] + fr2[0] * fr1[1], fr1[1] * fr2[1]]
gcd = calc_divisor(fr_sum[0], fr_sum[1])
fr_sum[0] //= gcd
fr_sum[1] //= gcd

print(*fr_sum, sep=' ')