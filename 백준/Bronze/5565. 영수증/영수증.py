import sys
input = sys.stdin.readline

total = int(input())
price_sum = 0

for _ in range(9):
    price_sum += int(input())
print(total - price_sum)