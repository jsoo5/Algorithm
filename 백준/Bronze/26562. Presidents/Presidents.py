import sys
input = sys.stdin.readline

def moeny_value(name):
    if name == 'Franklin':
        return 100
    if name == 'Grant':
        return 50
    if name == 'Jackson':
        return 20
    if name == 'Hamilton':
        return 10
    if name == 'Lincoln':
        return 5
    else:
        return 1

n = int(input().strip())
for _ in range(n):
    values = 0
    presidents = list(map(str, input().split()))
    for p in presidents:
        money = moeny_value(p)
        values += money
    print(f'${values}')