import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

count_map = {}

for num in a:
    if num in count_map:
        count_map[num] += 1
    else:
        count_map[num] = 1

for target in b:
    print(count_map.get(target, 0), end=' ')