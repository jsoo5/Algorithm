import sys
input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))
m = int(input())
numbers = tuple(map(int, input().split()))
result = []

for number in numbers:
    if number in cards:
        result.append(1)
    else:
        result.append(0)
print(*result, end=' ')