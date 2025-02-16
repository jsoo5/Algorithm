import sys
input = sys.stdin.readline

n = int(input())
price = 0

for _ in range(n):
    changes = int(input())
    price += changes
print(max(0, price))