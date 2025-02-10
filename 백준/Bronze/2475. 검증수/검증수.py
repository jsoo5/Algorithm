import sys
input = sys.stdin.readline

def calc_last_num(ns):
    num_sum = 0

    for n in ns:
        num_sum += n * n

    return num_sum % 10

numbers = list(map(int, input().strip().split()))
print(calc_last_num(numbers))