def calc_gcd(int1, int2):
    bigger = max(int1, int2)
    smaller = min(int1, int2)
    
    while bigger % smaller > 1:
        remainder = bigger % smaller
        bigger = smaller
        smaller = remainder
    
    if bigger % smaller == 0:   
        return smaller    
    else:                       
        return 1


n = int(input())

for _ in range(n):
    int1, int2 = map(int, input().split())
    print(calc_gcd(int1, int2))